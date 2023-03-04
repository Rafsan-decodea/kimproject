import 'dart:async';

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
  final auth = FirebaseAuth.instance;
  final ref = FirebaseDatabase.instance.ref("users");
  Future<Object?> getData() async {
    DataSnapshot snapshot = (await ref.once()) as DataSnapshot;
    Object? data = snapshot.value;
    return data;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //extendBodyBehindAppBar: true,
      backgroundColor: Color.fromARGB(255, 255, 254, 254),
      appBar: AppBar(
        title: Text("Known Person"),
      ),
      body: Column(
        children: [
          Expanded(
              child: FirebaseAnimatedList(
            query: ref,
            defaultChild: Text("loading"),
            itemBuilder: (context, snapshot, animation, index) {
              return ListTile(
                title: Text(snapshot.child('date').value.toString()),
                subtitle: Text(snapshot.child('image').value.toString()),
              );
            },
          )),
          
        ],
      ),
    );
  }
}
