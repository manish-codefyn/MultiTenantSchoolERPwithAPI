import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../features/dashboard/dashboard_screen.dart';
import '../../features/auth/presentation/login_screen.dart';
import '../../features/tenant/presentation/tenant_selection_screen.dart';
import '../../features/students/presentation/student_list_screen.dart';
import '../../features/students/presentation/student_form_screen.dart';
import '../../features/students/presentation/student_detail_screen.dart';
import '../../features/students/presentation/student_wrapper_form_screen.dart';
import '../../features/students/domain/student.dart';
import '../../features/academics/presentation/academics_dashboard_screen.dart';
import '../../features/hr/presentation/staff_list_screen.dart';
import '../../features/hr/presentation/staff_dashboard_screen.dart';
import '../../features/finance/presentation/finance_dashboard_screen.dart';
import '../../features/finance/presentation/fee_list_screen.dart';
import '../../features/attendance/presentation/screens/attendance_dashboard_screen.dart';
import '../../features/transport/presentation/transport_screen.dart';
import '../../features/transport/presentation/transport_dashboard_screen.dart';
import '../../features/transport/presentation/transport_dashboard_screen.dart';
import '../../features/events/presentation/events_dashboard_screen.dart';
import '../../features/events/presentation/event_list_screen.dart';
import '../../features/exams/presentation/exams_dashboard_screen.dart';
import '../../features/communications/presentation/communications_dashboard_screen.dart';
import '../../features/assignments/presentation/assignments_dashboard_screen.dart';
import '../../features/students/presentation/student_dashboard_screen.dart';
import '../../features/hostel/presentation/hostel_screen.dart';
import '../../features/hostel/presentation/hostel_dashboard_screen.dart';


final routerProvider = Provider<GoRouter>((ref) {
  return GoRouter(
    initialLocation: '/tenant',
    routes: [
      GoRoute(
        path: '/tenant',
        builder: (context, state) => const TenantSelectionScreen(),
      ),
      GoRoute(
        path: '/events',
        builder: (context, state) => const EventsDashboardScreen(),
        routes: [
          GoRoute(
            path: 'list',
            builder: (context, state) => const EventListScreen(),
          ),
        ],
      ),
      GoRoute(
        path: '/login',
        builder: (context, state) => const LoginScreen(),
      ),
      GoRoute(
        path: '/',
        builder: (context, state) => const DashboardScreen(),
      ),

      GoRoute(
        path: '/students',
        builder: (context, state) => const StudentDashboardScreen(),
        routes: [
           GoRoute(
            path: 'list',
            builder: (context, state) => const StudentListScreen(),
          ),
          GoRoute(
            path: 'add',
            builder: (context, state) => const StudentWrapperFormScreen(),
          ),
          GoRoute(
            path: 'detail',
            builder: (context, state) {
               // Expecting Student object in extra
               final student = state.extra as Student; 
               return StudentDetailScreen(student: student);
            },
          ),
        ],
      ),
      GoRoute(
        path: '/academics',
        builder: (context, state) => const AcademicsDashboardScreen(),
      ),
      GoRoute(
        path: '/hr/staff',
        builder: (context, state) => const StaffDashboardScreen(),
        routes: [
           GoRoute(
            path: 'list',
            builder: (context, state) => const StaffListScreen(),
          ),
        ],
      ),
      GoRoute(
        path: '/finance',
        builder: (context, state) => const FinanceDashboardScreen(),
        routes: [
          GoRoute(
            path: 'fees',
            builder: (context, state) => const FeeListScreen(),
          ),
        ],
      ),
      GoRoute(
        path: '/attendance',
        builder: (context, state) => const AttendanceDashboardScreen(),
      ),
      GoRoute(
        path: '/transport',
        builder: (context, state) => const TransportDashboardScreen(),
        routes: [
           GoRoute(
            path: 'list',
            builder: (context, state) => const TransportScreen(),
          ),
        ],
      ),
      GoRoute(
        path: '/hostel',
        builder: (context, state) => const HostelDashboardScreen(),
        routes: [
           GoRoute(
            path: 'list',
            builder: (context, state) => const HostelScreen(),
          ),
        ],
      ),
      GoRoute(
        path: '/exams',
        builder: (context, state) => const ExamsDashboardScreen(),
        routes: [
           GoRoute(
             path: 'schedule',
             builder: (context, state) => const Scaffold(body: Center(child: Text("Exam Schedule List - TODO"))), 
           )
        ]
      ),
      GoRoute(
        path: '/communications',
        builder: (context, state) => const CommunicationsDashboardScreen(),
      ),
      GoRoute(
        path: '/assignments',
        builder: (context, state) => const AssignmentsDashboardScreen(),
      ),
    ],
  );
});
