import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../data/student_repository.dart';
import '../domain/student.dart';

final studentListProvider = FutureProvider.autoDispose<List<Student>>((ref) async {
  return ref.watch(studentRepositoryProvider).getStudents();
});

class StudentListScreen extends ConsumerWidget {
  const StudentListScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final studentsAsync = ref.watch(studentListProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('Students')),
      body: studentsAsync.when(
        data: (students) => ListView.builder(
          itemCount: students.length,
          itemBuilder: (context, index) {
            final student = students[index];
            return ListTile(
              leading: CircleAvatar(child: Text(student.firstName[0])),
              title: Text('${student.firstName} ${student.lastName}'),
              subtitle: Text(student.admissionNumber),
              trailing: const Icon(Icons.chevron_right),
            );
          },
        ),
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (err, stack) => Center(child: Text('Error: $err')),
      ),
    );
  }
}
