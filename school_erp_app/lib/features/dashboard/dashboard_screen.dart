import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../auth/presentation/auth_controller.dart';

class DashboardScreen extends ConsumerWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('School ERP'),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
              ref.read(authControllerProvider.notifier).logout();
              context.go('/login');
            },
          ),
        ],
      ),
      drawer: NavigationDrawer(
        onDestinationSelected: (index) {
          // Handle navigation
          switch (index) {
            case 0:
              context.pop(); // Close drawer
              break;
              context.push('/students');
              break;
            case 2:
              context.push('/academics');
              break;
            case 3:
              context.push('/hr/staff');
              break;
            case 5: // Finance is at index 5 in the list below
              context.push('/finance/fees');
              break;
            case 4: 
              context.push('/attendance');
              break;
            case 6: 
              context.push('/transport');
              break;
            case 7: 
              context.push('/hostel');
              break;
            // Add other cases for more modules
          }
        },
        children: const [
          NavigationDrawerDestination(
            icon: Icon(Icons.dashboard),
            label: Text('Dashboard'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.people),
            label: Text('Students'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.school),
            label: Text('Academics'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.people),
            label: Text('Staff'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.class_),
            label: Text('Classes'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.event),
            label: Text('Attendance'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.payment),
            label: Text('Finance'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.library_books),
            label: Text('Library'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.directions_bus),
            label: Text('Transport'),
          ),
          NavigationDrawerDestination(
            icon: Icon(Icons.bed),
            label: Text('Hostel'),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Overview',
              style: Theme.of(context).textTheme.headlineSmall,
            ),
            const SizedBox(height: 16),
            const Row(
              children: [
                _StatCard(title: 'Total Students', value: '1,234', color: Colors.blue),
                SizedBox(width: 16),
                _StatCard(title: 'Teachers', value: '56', color: Colors.orange),
              ],
            ),
            const SizedBox(height: 16),
            const Row(
              children: [
                _StatCard(title: 'Present Today', value: '95%', color: Colors.green),
                SizedBox(width: 16),
                _StatCard(title: 'Fees Collected', value: '\$50k', color: Colors.purple),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class _StatCard extends StatelessWidget {
  final String title;
  final String value;
  final Color color;

  const _StatCard({required this.title, required this.value, required this.color});

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Card(
        elevation: 2,
        color: color.withOpacity(0.1),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title, style: TextStyle(color: color, fontWeight: FontWeight.bold)),
              const SizedBox(height: 8),
              Text(
                value,
                style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                  color: color,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
