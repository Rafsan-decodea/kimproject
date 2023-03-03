import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:firebase_database/ui/firebase_animated_list.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class KnownPerson extends StatefulWidget {
  const KnownPerson({super.key});

  @override
  State<KnownPerson> createState() => _KnownPersonState();
}

class _KnownPersonState extends State<KnownPerson> {
  @override
  Widget build(BuildContext context) {
    // final auth = FirebaseAuth.instance;
    // final ref = FirebaseDatabase.instance.ref("users");
    //  snapshot.child('date').value.toString(),
    return Scaffold(
      extendBodyBehindAppBar: true,
      backgroundColor: Color.fromARGB(255, 255, 254, 254),
      appBar: AppBar(
        title: Text("Known Person"),
      ),
      body: Column(
        children: [Text("data")],
      ),
    );
  }
}
