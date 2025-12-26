import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../../core/network/api_client.dart';

final academicsRepositoryProvider = Provider((ref) => AcademicsRepository(ref));

class AcademicsRepository {
  final Ref _ref;

  AcademicsRepository(this._ref);

  Future<Map<String, dynamic>> getDashboardStats() async {
    try {
      final client = _ref.read(apiClientProvider).client;
      final response = await client.get('academics/dashboard/');
      return response.data;
    } catch (e) {
      rethrow;
    }
  }
}

final dashboardStatsProvider = FutureProvider.autoDispose((ref) async {
  return ref.watch(academicsRepositoryProvider).getDashboardStats();
});
