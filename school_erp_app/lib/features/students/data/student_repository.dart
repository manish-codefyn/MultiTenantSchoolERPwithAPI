import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../../core/network/api_client.dart';
import '../domain/student.dart';

final studentRepositoryProvider = Provider((ref) => StudentRepository(ref));

class StudentRepository {
  final Ref _ref;

  StudentRepository(this._ref);

  Future<List<Student>> getStudents() async {
    final dio = _ref.read(apiClientProvider).client;
    try {
      final response = await dio.get('students/');
      // Assuming standard DRF paginated response or list
      // For now handling direct list or "results" key
      final data = response.data;
      if (data is Map && data.containsKey('results')) {
        return (data['results'] as List).map((e) => Student.fromJson(e)).toList();
      } else if (data is List) {
        return data.map((e) => Student.fromJson(e)).toList();
      }
      return [];
    } catch (e) {
      rethrow;
    }
  }
}
