import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../shared/widgets/stats_card.dart';
import '../../core/theme/app_theme.dart';
import 'package:google_fonts/google_fonts.dart';
import 'presentation/dashboard_controller.dart';
import '../../core/theme/theme_controller.dart';
import '../auth/presentation/auth_controller.dart'; // From features/dashboard to features/auth

class DashboardScreen extends ConsumerWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final statsAsync = ref.watch(dashboardStatsProvider);

    return Scaffold(
      backgroundColor: AppTheme.bodyBackground,
      drawer: Drawer(
        elevation: 0,
        shape: const RoundedRectangleBorder(
              borderRadius: BorderRadius.only(topRight: Radius.circular(0), bottomRight: Radius.circular(0)),
        ),
        backgroundColor: Colors.white,
        child: Column(
          children: [
             // Rocker Sidebar Header
             Container(
               height: 60,
               padding: const EdgeInsets.symmetric(horizontal: 16),
               decoration: const BoxDecoration(
                 border: Border(bottom: BorderSide(color: AppTheme.borderColor)),
               ),
               child: Row(
                 children: [
                   Image.asset('assets/images/app_logo.png', height: 30, errorBuilder: (_,__,___) => const Icon(Icons.school, color: AppTheme.primaryBlue, size: 30)),
                   const SizedBox(width: 10),
                   Expanded(
                     child: Text(
                       statsAsync.value?['tenantName'] ?? 'School ERP', 
                       style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppTheme.primaryBlue),
                       overflow: TextOverflow.ellipsis,
                     ),
                   ),
                   // Toggle Icon (Visual only)
                   const Icon(Icons.arrow_back, size: 18, color: AppTheme.primaryBlue),
                 ],
               ),
             ),
             
             Expanded(
               child: SingleChildScrollView(
                 padding: const EdgeInsets.only(top: 10),
                 child: Column(
                   children: [
                     _buildDrawerItem(context, 'Dashboard', Icons.home_filled, onTap: () {}), // Current
                     _buildDrawerItem(context, 'Students', Icons.people_outline_rounded, onTap: () => context.push('/students')),
                     _buildDrawerItem(context, 'Academics', Icons.school_outlined, onTap: () => context.push('/academics')),
                     _buildDrawerItem(context, 'Staff', Icons.badge_outlined, onTap: () => context.push('/hr/staff')),
                     _buildDrawerItem(context, 'Attendance', Icons.calendar_today_outlined, onTap: () => context.push('/attendance')),
                     _buildDrawerItem(context, 'Finance', Icons.account_balance_wallet_outlined, onTap: () => context.push('/finance')),
                     _buildDrawerItem(context, 'Transport', Icons.directions_bus_outlined, onTap: () => context.push('/transport')),
                     _buildDrawerItem(context, 'Hostel', Icons.bed_outlined, onTap: () => context.push('/hostel')),
                     _buildDrawerItem(context, 'Events', Icons.event_outlined, onTap: () => context.push('/events')),
                     _buildDrawerItem(context, 'Exams', Icons.assignment_outlined, onTap: () => context.push('/exams')),
                     _buildDrawerItem(context, 'Communications', Icons.chat_bubble_outline_rounded, onTap: () => context.push('/communications')),
                     _buildDrawerItem(context, 'Assignments', Icons.assignment_ind_outlined, onTap: () => context.push('/assignments')),
                   ],
                 ),
               ),
             )
          ],
        ),
      ),
      body: statsAsync.when(
        data: (stats) => CustomScrollView(
          physics: const BouncingScrollPhysics(),
          slivers: [
            SliverAppBar(
              pinned: true,
              floating: true,
              backgroundColor: Colors.white,
              elevation: 4,
              shadowColor: const Color(0xffdadafd).withOpacity(0.5),
              leading: Builder(
                builder: (context) => IconButton(
                  icon: const Icon(Icons.menu, color: AppTheme.primaryBlue),
                  onPressed: () => Scaffold.of(context).openDrawer(),
                ),
              ),
              title: Text(
                'Dashboard', 
                style: GoogleFonts.roboto(color: AppTheme.textColor, fontWeight: FontWeight.bold),
              ),
              actions: [
                 IconButton(
                  icon: const Icon(Icons.search, color: Color(0xFF5F5F5F)),
                  onPressed: () {},
                ),
                 IconButton(
                  icon: const Icon(Icons.notifications_outlined, color: Color(0xFF5F5F5F)),
                  onPressed: () {},
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8.0),
                  child: CircleAvatar(
                    radius: 16,
                    backgroundColor: Colors.grey[200],
                    child: const Icon(Icons.person, color: Colors.grey),
                  ),
                ),
              ],
            ),
            SliverPadding(
              padding: const EdgeInsets.all(24), // Rocker has good padding
              sliver: SliverToBoxAdapter(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    if (stats['tenantName'] != null)
                      Padding(
                        padding: const EdgeInsets.only(bottom: 24),
                        child: Text(
                          'Welcome back, ${stats['tenantName']}',
                          style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                                color: AppTheme.textColor,
                                fontWeight: FontWeight.w500,
                              ),
                        ),
                      ),
                    
                    Text(
                      "Overview".toUpperCase(),
                      style: GoogleFonts.roboto(fontSize: 14, fontWeight: FontWeight.w500, color: const Color(0xFFB0AFAF), letterSpacing: 0.5),
                    ),
                    const SizedBox(height: 16),
                  ],
                ),
              ),
            ),
            SliverPadding(
              padding: const EdgeInsets.symmetric(horizontal: 24),
              sliver: SliverGrid.count(
                crossAxisCount: 2,
                crossAxisSpacing: 24,
                mainAxisSpacing: 24,
                childAspectRatio: 1.1,
                children: [
                  StatsCard(
                    title: 'Students',
                    value: stats['studentCount'].toString(),
                    icon: Icons.people_outline,
                    onTap: () => context.push('/students'),
                    // Rocker Style Cards are white with shadow, handled by Theme, no gradient by default usually, but we keep gradient if user likes it or keep it white?
                    // User said "same style". Rocker cards in widgets.html typically white.
                    // Let's rely on updated CardTheme but StatsCard might need adjustment.
                  ),
                  StatsCard(
                    title: 'Staff',
                    value: stats['staffCount'].toString(),
                    icon: Icons.badge_outlined,
                     gradient: const LinearGradient(colors: [Color(0xFF17A00E), Color(0xFF24C41A)]), // Custom Green
                    onTap: () => context.push('/hr/staff'),
                  ),
                  StatsCard(
                    title: 'Attendance',
                    value: '92%',
                    icon: Icons.check_circle_outline,
                     gradient: const LinearGradient(colors: [Color(0xFFF41127), Color(0xFFFF4D60)]), // Custom Red
                    onTap: () => context.push('/attendance'),
                  ),
                  StatsCard(
                    title: 'Fees',
                    value: stats['feeCollection'].toString(),
                    icon: Icons.attach_money,
                    gradient: const LinearGradient(colors: [Color(0xFFFFC107), Color(0xFFFFD555)]), // Custom Yellow
                    onTap: () => context.push('/finance'),
                  ),
                ],
              ),
            ),
            SliverPadding(
              padding: const EdgeInsets.all(24),
              sliver: SliverList(
                delegate: SliverChildListDelegate([
                   const SizedBox(height: 24),
                   Text(
                      "Analysis".toUpperCase(),
                      style: GoogleFonts.roboto(fontSize: 14, fontWeight: FontWeight.w500, color: const Color(0xFFB0AFAF), letterSpacing: 0.5),
                    ),
                   const SizedBox(height: 16),
                   _buildAnalysisChart(context),
                   const SizedBox(height: 24),
                   Text(
                      "Quick Actions".toUpperCase(),
                      style: GoogleFonts.roboto(fontSize: 14, fontWeight: FontWeight.w500, color: const Color(0xFFB0AFAF), letterSpacing: 0.5),
                    ),
                   const SizedBox(height: 16),
                   _buildManagementTile(context, 'Academics', 'Classes, Subjects & TimeTable', Icons.school_outlined, Colors.indigo, () => context.push('/academics')),
                   _buildManagementTile(context, 'Transport', 'Routes, Vehicles & Drivers', Icons.directions_bus_outlined, Colors.blue, () => context.push('/transport')),
                   _buildManagementTile(context, 'Hostel', 'Rooms & Allocations', Icons.bed_outlined, Colors.teal, () => context.push('/hostel')),
                   const SizedBox(height: 40),
                ]),
              ),
            ),
          ],
        ),
        loading: () => const Scaffold(body: Center(child: CircularProgressIndicator())),
        error: (err, stack) => Scaffold(body: Center(child: Text('Error: $err'))),
      ),
    );
  }

  Widget _buildDrawerItem(BuildContext context, String title, IconData icon, {required VoidCallback onTap}) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 2),
      child: ListTile(
        onTap: () {
          Navigator.pop(context);
          onTap();
        },
        leading: Icon(icon, color: const Color(0xFF5f5f5f), size: 22), // Rocker icon color
        title: Text(title, style: const TextStyle(color: Color(0xFF5f5f5f), fontSize: 15)),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(4)),
        hoverColor: AppTheme.primaryBlue.withOpacity(0.05),
        // Note: Flutter standard ListTile hover doesn't support changing Icon color easily without state. 
        // For strict adherence we'd need a custom stateful widget, but this is close.
      ),
    );
  }

  Widget _buildAnalysisChart(BuildContext context) {
    return Card(
      elevation: 0,
       shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(20),
        side: BorderSide(color: Colors.grey.shade200),
      ),
      child: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text("Fee Collection", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                  decoration: BoxDecoration(
                    color: Theme.of(context).primaryColor.withOpacity(0.1),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Text(
                    "This Year",
                    style: TextStyle(color: Theme.of(context).primaryColor, fontWeight: FontWeight.bold, fontSize: 12),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 30),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                _buildBar(context, "Jan", 0.4),
                _buildBar(context, "Feb", 0.6),
                _buildBar(context, "Mar", 0.8),
                _buildBar(context, "Apr", 0.5),
                _buildBar(context, "May", 0.7),
                _buildBar(context, "Jun", 0.9),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildBar(BuildContext context, String label, double pct) {
    return Column(
      children: [
        Container(
          width: 12,
          height: 120 * pct,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(6),
            gradient: AppTheme.primaryGradient,
            boxShadow: [
              BoxShadow(
                color: Theme.of(context).primaryColor.withOpacity(0.3),
                blurRadius: 4,
                offset: const Offset(0, 2),
              )
            ],
          ),
        ),
        const SizedBox(height: 12),
        Text(label, style: TextStyle(fontSize: 12, color: Colors.grey[600], fontWeight: FontWeight.w500)),
      ],
    );
  }

  Widget _buildManagementTile(BuildContext context, String title, String subtitle, IconData icon, Color color, VoidCallback onTap) {
    return Card(
      elevation: 0,
      margin: const EdgeInsets.only(bottom: 12),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(color: Colors.grey.shade100),
      ),
      child: ListTile(
        contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
        leading: Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: color.withOpacity(0.1),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Icon(icon, color: color, size: 24),
        ),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        subtitle: Padding(
          padding: const EdgeInsets.only(top: 4),
          child: Text(subtitle, style: TextStyle(color: Colors.grey[600], fontSize: 13)),
        ),
        trailing: Icon(Icons.chevron_right_rounded, color: Colors.grey[400]),
        onTap: onTap,
      ),
    );
  }
}

