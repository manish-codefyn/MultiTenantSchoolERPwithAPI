from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.core.api.views import (
    BaseListCreateAPIView, BaseRetrieveUpdateDestroyAPIView
)
from apps.academics.models import StudentAttendance
from apps.hr.models import StaffAttendance
from apps.hostel.models import HostelAttendance
from apps.transportation.models import TransportAttendance
from apps.attendance.api.serializers import (
    StudentAttendanceSerializer, StaffAttendanceSerializer,
    HostelAttendanceSerializer, TransportAttendanceSerializer
)

# ============================================================================
# STUDENT ATTENDANCE VIEWS
# ============================================================================

class StudentAttendanceListCreateAPIView(BaseListCreateAPIView):
    model = StudentAttendance
    serializer_class = StudentAttendanceSerializer
    search_fields = ['student__first_name', 'student__admission_number']
    filterset_fields = ['date', 'status', 'class_name', 'section', 'student']
    roles_required = ['admin', 'teacher', 'student', 'parent']

class StudentAttendanceDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = StudentAttendance
    serializer_class = StudentAttendanceSerializer
    roles_required = ['admin', 'teacher']

from apps.hr.models import Staff
from apps.students.models import Student
from django.utils import timezone
import re

class MarkQRAttendanceAPIView(APIView):
    """
    Mark attendance via QR Scan.
    Payload: 
      - qr_text: "Admission No: 123" OR "EMP001"
      - type: "student" (default) | "staff" | "transport"
      - trip_type: "PICKUP" | "DROP" (optional, for transport)
    """
    def post(self, request, *args, **kwargs):
        qr_text = request.data.get('qr_text', '').strip()
        att_type = request.data.get('type', 'student') 
        
        if not qr_text:
             return Response({"error": "No QR text provided."}, status=status.HTTP_400_BAD_REQUEST)

        # ---------------------------------------------------------
        # 1. STAFF ATTENDANCE
        # ---------------------------------------------------------
        if att_type == 'staff':
            # Assume QR contains Employee ID directly or prefixes
            emp_id = qr_text
            if "Employee ID:" in qr_text:
                emp_id = qr_text.split("Employee ID:")[1].strip()
            
            try:
                staff = Staff.objects.get(employee_id=emp_id)
            except Staff.DoesNotExist:
                return Response({"error": f"Staff with ID '{emp_id}' not found."}, status=status.HTTP_404_NOT_FOUND)

            today = timezone.now().date()
            now_time = timezone.now().time()
            
            # Create or Get Attendance
            attendance, created = StaffAttendance.objects.get_or_create(
                staff=staff,
                date=today,
                defaults={
                    'status': 'PRESENT',
                    'check_in': now_time,
                    'marked_by': request.user if request.user.is_authenticated else None
                }
            )
            
            if not created:
                if not attendance.check_out:
                     attendance.check_out = now_time
                     attendance.save()
                     msg = f"Check-out marked for {staff.full_name}"
                else:
                     msg = f"Attendance already marked for {staff.full_name}"
            else:
                msg = f"Check-in marked for {staff.full_name}"

            return Response({
                "message": msg,
                "student_name": staff.full_name, # reuse key for frontend compat
                "status": "PRESENT",
                "photo_url": staff.profile_image.url if staff.profile_image else None
            })

        # ---------------------------------------------------------
        # 2. STUDENT / TRANSPORT ATTENDANCE
        # ---------------------------------------------------------
        # Parse Admission Number
        match = re.search(r'Admission No:\s*([^\\s\\n]+)', qr_text)
        if not match:
            # Try matching raw if regex fails
            admission_number = qr_text
        else:
            admission_number = match.group(1)

        try:
             student = Student.objects.get(admission_number=admission_number)
             if hasattr(request, 'tenant') and request.tenant and student.tenant != request.tenant:
                 return Response({"error": "Student not found in this school."}, status=status.HTTP_404_NOT_FOUND)
        except Student.DoesNotExist:
             msg = f"Student with Admission No/Roll '{admission_number}' not found."
             return Response({"error": msg}, status=status.HTTP_404_NOT_FOUND)

        today = timezone.now().date()
        
        # TRANSPORT MARKING
        if att_type == 'transport':
            trip_type = request.data.get('trip_type')
            if not trip_type:
                trip_type = 'PICKUP' if timezone.now().hour < 12 else 'DROP'
            
            t_att, created = TransportAttendance.objects.update_or_create(
                student=student,
                date=today,
                trip_type=trip_type,
                defaults={
                    'status': 'PRESENT',
                    'actual_time': timezone.now().time(),
                    'marked_by': request.user if request.user.is_authenticated else None
                }
            )
            return Response({
                "message": f"Transport {trip_type} marked for {student.first_name}",
                "student_name": student.full_name,
                "status": "PRESENT",
                "photo_url": student.get_photo().file.url if student.get_photo() and student.get_photo().file else None
            })

        # HOSTEL ATTENDANCE
        if att_type == 'hostel':
            h_att, created = HostelAttendance.objects.update_or_create(
                student=student,
                date=today,
                defaults={
                    'status': 'PRESENT',
                    'check_in_time': timezone.now().time(),
                    'marked_by': request.user if request.user.is_authenticated else None,
                    'remarks': 'QR Scan'
                }
            )
            return Response({
                "message": f"Hostel attendance marked for {student.first_name}",
                "student_name": student.full_name,
                "status": "PRESENT",
                "photo_url": student.get_photo().file.url if student.get_photo() and student.get_photo().file else None
            })

        # REGULAR STUDENT ATTENDANCE (Default)
        att, created = StudentAttendance.objects.update_or_create(
            student=student,
            date=today,
            defaults={
                'status': 'PRESENT',
                'class_name': student.current_class,
                'section': student.section,
                'marked_by': request.user if request.user.is_authenticated else None
            }
        )
        
        photo_doc = student.get_photo()
        photo_url = photo_doc.file.url if photo_doc and photo_doc.file else None

        return Response({
            "message": f"Present marked for {student.first_name}",
            "student_name": student.full_name,
            "roll_number": student.roll_number,
            "status": "PRESENT",
            "photo_url": photo_url
        })


# ============================================================================
# STAFF ATTENDANCE VIEWS
# ============================================================================

class StaffAttendanceListCreateAPIView(BaseListCreateAPIView):
    model = StaffAttendance
    serializer_class = StaffAttendanceSerializer
    search_fields = ['staff__first_name', 'staff__employee_id']
    filterset_fields = ['date', 'status', 'staff']
    roles_required = ['admin', 'hr_manager', 'principal']

class StaffAttendanceDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = StaffAttendance
    serializer_class = StaffAttendanceSerializer
    roles_required = ['admin', 'hr_manager', 'principal']


# ============================================================================
# HOSTEL ATTENDANCE VIEWS
# ============================================================================

class HostelAttendanceListCreateAPIView(BaseListCreateAPIView):
    model = HostelAttendance
    serializer_class = HostelAttendanceSerializer
    search_fields = ['student__first_name', 'student__admission_number']
    filterset_fields = ['date', 'status', 'student']
    roles_required = ['admin', 'hostel_warden', 'student', 'parent']

class HostelAttendanceDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = HostelAttendance
    serializer_class = HostelAttendanceSerializer
    roles_required = ['admin', 'hostel_warden']





class MarkFaceAttendanceAPIView(APIView):
    """
    Mark attendance via Face Recognition.
    Payload:
      - image: Base64 string
      - type: "student" (default) | "staff" | "transport"
    """
    def post(self, request, *args, **kwargs):
        import base64
        import numpy as np
        
        # 1. Parse Image
        image_data = request.data.get('image')
        att_type = request.data.get('type', 'student')
        
        if not image_data:
            return Response({"error": "No image data provided"}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            format, imgstr = image_data.split(';base64,')
            data = base64.b64decode(imgstr)
        except Exception:
             # Try raw decode if format is missing
             try:
                 data = base64.b64decode(image_data)
             except:
                return Response({"error": "Invalid base64 image"}, status=status.HTTP_400_BAD_REQUEST)

        # 2. Try Real Face Rec (Simulated fallback)
        try:
            import face_recognition
            import cv2
            
            # Save tmp file for CV2 (or decode buffer)
            nparr = np.frombuffer(data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Detect
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_encodings = face_recognition.face_encodings(rgb_img)
            
            if not face_encodings:
                return Response({"error": "No face detected in image."}, status=status.HTTP_400_BAD_REQUEST)
                
            uploaded_encoding = face_encodings[0]
            
            # 3. Match Logic based on Type
            matched_object = None
            
            if att_type == 'staff':
                # Iterate Active Staff
                staff_qs = Staff.objects.filter(employment_status='ACTIVE')
                for staff in staff_qs:
                    try:
                        # Check user avatar first
                        if staff.user and staff.user.avatar:
                            known_image = face_recognition.load_image_file(staff.user.avatar.path)
                            known_encoding = face_recognition.face_encodings(known_image)
                            if known_encoding:
                                match = face_recognition.compare_faces([known_encoding[0]], uploaded_encoding, tolerance=0.5)
                                if match[0]:
                                    matched_object = staff
                                    break
                        # Check photograph document
                        else:
                            photo_doc = staff.documents.filter(document_type='PHOTOGRAPH').first()
                            if photo_doc and photo_doc.file:
                                known_image = face_recognition.load_image_file(photo_doc.file.path)
                                known_encoding = face_recognition.face_encodings(known_image)
                                if known_encoding:
                                    match = face_recognition.compare_faces([known_encoding[0]], uploaded_encoding, tolerance=0.5)
                                    if match[0]:
                                        matched_object = staff
                                        break
                    except Exception:
                        continue
            else:
                # Student / Transport
                # Iterate Active Students
                student_qs = Student.objects.filter(status='ACTIVE')
                
                for student in student_qs:
                    photo_doc = student.get_photo()
                    if photo_doc and photo_doc.file:
                        try:
                            known_image = face_recognition.load_image_file(photo_doc.file.path)
                            known_encodings = face_recognition.face_encodings(known_image)
                            if known_encodings:
                                match = face_recognition.compare_faces([known_encodings[0]], uploaded_encoding, tolerance=0.5)
                                if match[0]:
                                    matched_object = student
                                    break
                        except Exception:
                            continue

            if matched_object:
                # Mark it
                return self.mark_found_object(request, matched_object, att_type)
            else:
                 return Response({"error": "Face not recognized."}, status=status.HTTP_404_NOT_FOUND)

        except ImportError:
            # ==========================================
            # FALLBACK DEMO MODE (For Windows without Dlib)
            # ==========================================
            # Simulate a match
            import random
            
            if att_type == 'staff':
                candidates = []
                for s in Staff.objects.filter(employment_status='ACTIVE'):
                    try:
                        # Check if staff has user with avatar or has photograph document
                        has_photo = False
                        if s.user and s.user.avatar:
                            has_photo = True
                        elif s.documents.filter(document_type='PHOTOGRAPH').exists():
                            has_photo = True
                        
                        if has_photo:
                            candidates.append(s)
                    except Exception:
                        continue
                
                if not candidates:
                     return Response({"error": "(DEMO) No staff with photos found to simulate match."}, status=status.HTTP_404_NOT_FOUND)
                
                matched_object = random.choice(candidates)
            else:
                candidates = []
                for s in Student.objects.filter(status='ACTIVE'):
                    if s.get_photo(): candidates.append(s)
                
                if not candidates:
                     return Response({"error": "(DEMO) No students with photos found to simulate match."}, status=status.HTTP_404_NOT_FOUND)
                
                matched_object = random.choice(candidates)
                
            return self.mark_found_object(request, matched_object, att_type, is_demo=True)
            
    def mark_found_object(self, request, obj, att_type, is_demo=False):
        today = timezone.now().date()
        msg_prefix = "(DEMO) " if is_demo else ""
        
        if att_type == 'staff':
            # Obj is Staff
            attendance, created = StaffAttendance.objects.get_or_create(
                staff=obj,
                date=today,
                defaults={
                    'status': 'PRESENT',
                    'check_in': timezone.now().time(),
                    'remarks': f"{msg_prefix}Face Scan",
                    'marked_by': request.user if request.user.is_authenticated else None
                }
            )
            return Response({
                "message": f"{msg_prefix}Marked Present: {obj.full_name}",
                "student_name": obj.full_name,
                "status": "PRESENT",
                "photo_url": obj.profile_image.url if obj.profile_image else None
            })
            
        elif att_type == 'transport':
            # Obj is Student
            trip = 'PICKUP' if timezone.now().hour < 12 else 'DROP'
            TransportAttendance.objects.update_or_create(
                student=obj,
                date=today,
                trip_type=trip,
                defaults={
                    'status': 'PRESENT',
                    'actual_time': timezone.now().time(),
                    'remarks': f"{msg_prefix}Face Scan",
                    'marked_by': request.user if request.user.is_authenticated else None
                }
            )
            return Response({
                "message": f"{msg_prefix}Transport {trip} Marked: {obj.first_name}",
                "student_name": obj.full_name,
                "status": "PRESENT",
                "photo_url": obj.get_photo().file.url if obj.get_photo() else None
            })
            
        elif att_type == 'hostel':
            # Obj is Student - Mark Hostel Attendance
            HostelAttendance.objects.update_or_create(
                student=obj,
                date=today,
                defaults={
                    'status': 'PRESENT',
                    'check_in_time': timezone.now().time(),
                    'remarks': f"{msg_prefix}Face Scan",
                    'marked_by': request.user if request.user.is_authenticated else None
                }
            )
            return Response({
                "message": f"{msg_prefix}Hostel Attendance Marked: {obj.first_name}",
                "student_name": obj.full_name,
                "status": "PRESENT",
                "photo_url": obj.get_photo().file.url if obj.get_photo() else None
            })
            
        else:
            # Student
            StudentAttendance.objects.update_or_create(
                student=obj,
                date=today,
                defaults={
                    'status': 'PRESENT',
                    'class_name': obj.current_class,
                    'section': obj.section,
                    'remarks': f"{msg_prefix}Face Scan",
                    'marked_by': request.user if request.user.is_authenticated else None
                }
            )
            return Response({
                "message": f"{msg_prefix}Marked Present: {obj.first_name}",
                "student_name": obj.full_name,
                "status": "PRESENT",
                "photo_url": obj.get_photo().file.url if obj.get_photo() else None
            })


# ============================================================================

class TransportAttendanceListCreateAPIView(BaseListCreateAPIView):
    model = TransportAttendance
    serializer_class = TransportAttendanceSerializer
    search_fields = ['student__first_name', 'student__admission_number']
    filterset_fields = ['date', 'status', 'trip_type', 'student']
    roles_required = ['admin', 'transport_manager', 'driver', 'student', 'parent']

class TransportAttendanceDetailAPIView(BaseRetrieveUpdateDestroyAPIView):
    model = TransportAttendance
    serializer_class = TransportAttendanceSerializer
    roles_required = ['admin', 'transport_manager']


# ============================================================================
# BULK / MANUAL ATTENDANCE APIS
# ============================================================================

from apps.academics.models import SchoolClass, Section

class StudentListByClassAPIView(APIView):
    """
    Get list of students for a class/section with their attendance status for TODAY.
    Query Params: class_id, section_id (optional)
    """
    def get(self, request):
        class_id = request.query_params.get('class_id')
        section_id = request.query_params.get('section_id')

        if not class_id:
             return Response({"error": "class_id is required"}, status=status.HTTP_400_BAD_REQUEST)
             
        students = Student.objects.filter(current_class_id=class_id, status='ACTIVE')
        if section_id:
            students = students.filter(section_id=section_id)
            
        students = students.order_by('roll_number', 'first_name')
        
        # Get today's attendance map
        today = timezone.now().date()
        attendance_map = {
            att.student_id: att.status 
            for att in StudentAttendance.objects.filter(date=today, student__in=students)
        }

        data = []
        for s in students:
            # Determine status: Default to ABSENT or PRESENT? 
            # Usually if no record, it's "Not Marked" (Gray).
            # If user clicks, it becomes Present (Green).
            current_status = attendance_map.get(s.id, 'NOT_MARKED')
            
            # Simple photo URL logic
            photo_doc = s.get_photo()
            photo_url = photo_doc.file.url if photo_doc and photo_doc.file else None

            data.append({
                'id': s.id,
                'name': s.full_name,
                'roll_number': s.roll_number,
                'admission_number': s.admission_number,
                'photo_url': photo_url,
                'status': current_status
            })
            
        return Response(data)

class BulkAttendanceUpdateAPIView(APIView):
    """
    Update attendance for a specific student or bulk.
    Payload: { "student_id": "uuid", "status": "PRESENT" }
    """
    def post(self, request):
        student_id = request.data.get('student_id')
        new_status = request.data.get('status') # PRESENT, ABSENT
        date_str = request.data.get('date')
        
        if not student_id or not new_status:
             return Response({"error": "student_id and status required"}, status=status.HTTP_400_BAD_REQUEST)

        today = timezone.now().date()
        if date_str:
            # Parse if needed, but defaulting to today for quick manual mode
            pass 

        student = get_object_or_404(Student, id=student_id)
        
        # Update or Create
        attendance, created = StudentAttendance.objects.update_or_create(
            student=student, 
            date=today,
            defaults={
                'status': new_status,
                'marked_by': request.user if request.user.is_authenticated else None,
                'class_name': student.current_class,
                'section': student.section,
                'tenant': student.tenant if hasattr(student, 'tenant') else None
            }
        )
        

# ============================================================================
# DASHBOARD & REPORTING APIs
# ============================================================================

class AttendanceStatsAPIView(APIView):
    """
    GET /api/v1/attendance/stats/
    Returns aggregated stats for a specific date (defaults to today).
    Filters: class_id, section_id
    """
    def get(self, request):
        date_str = request.query_params.get('date')
        if date_str:
            try:
                target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date format (YYYY-MM-DD)'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            target_date = timezone.now().date()
            
        class_id = request.query_params.get('class_id')
        section_id = request.query_params.get('section_id')
        
        # Base Query
        queryset = StudentAttendance.objects.filter(date=target_date)
        
        # Tenant Filter
        if hasattr(request, 'tenant') and request.tenant:
            queryset = queryset.filter(tenant=request.tenant)
            
        if class_id:
            queryset = queryset.filter(class_name_id=class_id)
        if section_id:
            queryset = queryset.filter(section_id=section_id)
            
        # Aggregation
        total = queryset.count()
        present = queryset.filter(status='PRESENT').count()
        absent = queryset.filter(status='ABSENT').count()
        late = queryset.filter(status='LATE').count()
        half_day = queryset.filter(status='HALFDAY').count()
        
        return Response({
            "date": target_date,
            "total_marked": total,
            "present": present,
            "absent": absent,
            "late": late,
            "half_day": half_day,
            "attendance_percentage": round((present / total * 100), 1) if total > 0 else 0.0
        })

class AttendanceHistoryListAPIView(BaseListCreateAPIView):
    """
    GET /api/v1/attendance/history/
    Filterable history of student attendance.
    """
    model = StudentAttendance
    serializer_class = StudentAttendanceSerializer
    search_fields = ['student__first_name', 'student__admission_number', 'remarks']
    filterset_fields = ['date', 'status', 'class_name', 'section', 'student']
    roles_required = ['admin', 'teacher', 'principal', 'parent', 'student']
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        # Date Range Filter
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        
        if start_date:
            qs = qs.filter(date__gte=start_date)
        if end_date:
            qs = qs.filter(date__lte=end_date)
            
        # Role-based restriction fallback
        user = self.request.user
        if user.role == 'student' and hasattr(user, 'student_profile'):
             qs = qs.filter(student=user.student_profile)
        elif user.role == 'parent':
             # TODO: Filter by parent's children if applicable
             pass
             
        return qs.order_by('-date', 'student__first_name')


class AttendanceExportAPIView(APIView):
    """
    GET /api/v1/attendance/export/
    Export attendance records to CSV.
    """
    def get(self, request):
        import csv
        from django.http import HttpResponse

        # Reuse filter logic (simplified)
        queryset = StudentAttendance.objects.all()
        if hasattr(request, 'tenant') and request.tenant:
            queryset = queryset.filter(tenant=request.tenant)
            
        # Apply filters
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        class_id = request.query_params.get('class_id')
        
        if start_date: queryset = queryset.filter(date__gte=start_date)
        if end_date: queryset = queryset.filter(date__lte=end_date)
        if class_id: queryset = queryset.filter(class_name_id=class_id)
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="attendance_report_{timezone.now().date()}.csv"'

        writer = csv.writer(response)
        writer.writerow(['Date', 'Student Name', 'Admission No', 'Class', 'Status', 'Remarks'])

        for att in queryset.select_related('student', 'class_name'):
            writer.writerow([
                att.date,
                att.student.full_name if att.student else 'N/A',
                att.student.admission_number if att.student else 'N/A',
                f"{att.class_name.name} {att.section.name}" if att.class_name else 'N/A',
                att.status,
                att.remarks
            ])

        return response
