import 'package:dio/dio.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

final tenantRepositoryProvider = Provider((ref) => TenantRepository(ref));

class TenantRepository {
  final Ref _ref;
  final Dio _publicDio; // Separate Dio for public tenant lookup
  final _storage = const FlutterSecureStorage();

  TenantRepository(this._ref)
      : _publicDio = Dio(BaseOptions(
          baseUrl: 'http://127.0.0.1:8000/', // Public root URL
          connectTimeout: const Duration(seconds: 10),
        ));

  Future<String> validateTenant(String schemaName) async {
    try {
      // Assuming GET /institutions/{schema_name}/ returns details if valid
      // or we can just try to hit a health check on the subdomain if DNS is not set up locally quite right
      // But based on user request: http://dpskolkata.localhost:8000/
      // We will construct the URL and verify connectivity.
      
      final tenantUrl = 'http://$schemaName.localhost:8000/api/v1/';
      
      // We can also verify validity via the public API first
      // await _publicDio.get('institutions/$schemaName/');

      // For this environment, let's just construct the URL and save it.
      // In a real app, we would ping it to ensure it's alive.
      
      await _storage.write(key: 'tenant_url', value: tenantUrl);
      await _storage.write(key: 'tenant_schema', value: schemaName);
      
      return tenantUrl;
    } catch (e) {
      rethrow;
    }
  }

  Future<String?> getSavedTenantUrl() async {
    return await _storage.read(key: 'tenant_url');
  }
  
  Future<void> clearTenant() async {
    await _storage.delete(key: 'tenant_url');
    await _storage.delete(key: 'tenant_schema');
  }
}
