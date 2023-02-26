import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class Dashboard extends StatelessWidget {
  const Dashboard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(child: const Text("Dashboard")),
        actions: [
          PopupMenuButton(
            itemBuilder: (BuildContext context) => [
              PopupMenuItem(
                child: Text('Option 1'),
              ),
              PopupMenuItem(
                child: Text('Option 2'),
              ),
              PopupMenuItem(
                child: Text('Option 3'),
              ),
            ],
          ),
        ],
      ),
      body: Column(
        children: const [
          Text("Hello"),
        ],
      ),
    );
  }
}
