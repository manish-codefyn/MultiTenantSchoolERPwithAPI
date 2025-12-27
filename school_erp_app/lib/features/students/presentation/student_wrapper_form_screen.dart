import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:google_fonts/google_fonts.dart';
import '../domain/student.dart';
import '../data/student_repository.dart';

class StudentWrapperFormScreen extends ConsumerStatefulWidget {
  final Student? student;
  const StudentWrapperFormScreen({super.key, this.student});

  @override
  ConsumerState<StudentWrapperFormScreen> createState() => _StudentWrapperFormScreenState();
}

class _StudentWrapperFormScreenState extends ConsumerState<StudentWrapperFormScreen> {
  int _currentStep = 0;
  final _formKey = GlobalKey<FormState>();
  
  // Controllers
  final _firstNameCtrl = TextEditingController();
  final _lastNameCtrl = TextEditingController();
  final _admissionCtrl = TextEditingController();
  final _emailCtrl = TextEditingController();
  final _phoneCtrl = TextEditingController();
  
  String _gender = 'M';
  DateTime _dob = DateTime(2015, 1, 1);
  String _address = '';
  
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    if (widget.student != null) {
      _firstNameCtrl.text = widget.student!.firstName;
      _lastNameCtrl.text = widget.student!.lastName;
      _admissionCtrl.text = widget.student!.admissionNumber ?? '';
      _emailCtrl.text = widget.student!.email ?? '';
      _phoneCtrl.text = widget.student!.mobilePrimary ?? '';
      // We would load other fields appropriately here
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.student == null ? 'New Admission' : 'Edit Student'),
      ),
      body: Form(
        key: _formKey,
        child: Stepper(
          type: StepperType.horizontal,
          currentStep: _currentStep,
          onStepContinue: () {
            if (_currentStep < 2) {
              setState(() => _currentStep += 1);
            } else {
              _submitForm();
            }
          },
          onStepCancel: () {
            if (_currentStep > 0) {
              setState(() => _currentStep -= 1);
            } else {
              Navigator.pop(context);
            }
          },
          controlsBuilder: (context, details) {
            return Padding(
              padding: const EdgeInsets.only(top: 20),
              child: Row(
                children: [
                  Expanded(
                    child: ElevatedButton(
                      onPressed: details.onStepContinue,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Theme.of(context).primaryColor,
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 16),
                      ),
                      child: Text(_currentStep == 2 ? 'SUBMIT' : 'NEXT'),
                    ),
                  ),
                  const SizedBox(width: 12),
                  if (_currentStep > 0)
                    TextButton(
                      onPressed: details.onStepCancel,
                      child: const Text('BACK'),
                    ),
                ],
              ),
            );
          },
          steps: [
            Step(
              title: const Text('Personal'),
              isActive: _currentStep >= 0,
              state: _currentStep > 0 ? StepState.complete : StepState.indexed,
              content: Column(
                children: [
                   TextFormField(
                     controller: _firstNameCtrl,
                     decoration: const InputDecoration(labelText: 'First Name', border: OutlineInputBorder()),
                     validator: (v) => v!.isEmpty ? 'Required' : null,
                   ),
                   const SizedBox(height: 16),
                   TextFormField(
                     controller: _lastNameCtrl,
                     decoration: const InputDecoration(labelText: 'Last Name', border: OutlineInputBorder()),
                     validator: (v) => v!.isEmpty ? 'Required' : null,
                   ),
                   const SizedBox(height: 16),
                   DropdownButtonFormField<String>(
                     value: _gender,
                     decoration: const InputDecoration(labelText: 'Gender', border: OutlineInputBorder()),
                     items: const [
                       DropdownMenuItem(value: 'M', child: Text('Male')),
                       DropdownMenuItem(value: 'F', child: Text('Female')),
                     ],
                     onChanged: (v) => setState(() => _gender = v!),
                   ),
                ],
              ),
            ),
            Step(
              title: const Text('Contact'),
              isActive: _currentStep >= 1,
              state: _currentStep > 1 ? StepState.complete : StepState.indexed,
              content: Column(
                children: [
                  TextFormField(
                     controller: _emailCtrl,
                     decoration: const InputDecoration(labelText: 'Email', border: OutlineInputBorder(), prefixIcon: Icon(Icons.email)),
                     validator: (v) => v!.isEmpty ? 'Required' : null,
                   ),
                   const SizedBox(height: 16),
                   TextFormField(
                     controller: _phoneCtrl,
                     decoration: const InputDecoration(labelText: 'Phone', border: OutlineInputBorder(), prefixIcon: Icon(Icons.phone)),
                     validator: (v) => v!.isEmpty ? 'Required' : null,
                   ),
                   const SizedBox(height: 16),
                   TextFormField(
                     maxLines: 3,
                     decoration: const InputDecoration(labelText: 'Address', border: OutlineInputBorder(), prefixIcon: Icon(Icons.home)),
                     onChanged: (v) => _address = v,
                   ),
                ],
              ),
            ),
            Step(
              title: const Text('Academic'),
              isActive: _currentStep >= 2,
              content: Column(
                children: [
                   TextFormField(
                     controller: _admissionCtrl,
                     decoration: const InputDecoration(labelText: 'Admission Number', border: OutlineInputBorder()),
                     validator: (v) => v!.isEmpty ? 'Required' : null,
                   ),
                   const SizedBox(height: 16),
                   // Placeholder for Class/Section Dropdowns
                   Container(
                     padding: const EdgeInsets.all(16),
                     decoration: BoxDecoration(color: Colors.grey[100], borderRadius: BorderRadius.circular(8)),
                     child: const Center(child: Text('Class & Section Selection Override')),
                   ),
                   const SizedBox(height: 16),
                   Container(
                     padding: const EdgeInsets.all(16),
                     decoration: BoxDecoration(color: Colors.blue[50], borderRadius: BorderRadius.circular(8)),
                     child: Row(
                       children: [
                         const Icon(Icons.info_outline, color: Colors.blue),
                         const SizedBox(width: 8),
                         const Expanded(child: Text('Student will be admitted to current active academic year.')),
                       ],
                     ),
                   )
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future<void> _submitForm() async {
    if (!_formKey.currentState!.validate()) return;
    
    // Logic similar to original form but cleaner
    final data = {
        'first_name': _firstNameCtrl.text,
        'last_name': _lastNameCtrl.text,
        'admission_number': _admissionCtrl.text,
        'personal_email': _emailCtrl.text,
        'mobile_primary': _phoneCtrl.text,
        'gender': _gender,
        'status': 'ACTIVE',
        'academic_year': '2c95558f-f77f-4193-9f77-ea6cc5868390', // Hardcoded
    };

    try {
       await ref.read(studentRepositoryProvider).createStudent(data);
       if (mounted) {
         ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Success')));
         Navigator.pop(context);
         ref.invalidate(studentListProvider);
       }
    } catch (e) {
      if (mounted) ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(e.toString())));
    }
  }
}
