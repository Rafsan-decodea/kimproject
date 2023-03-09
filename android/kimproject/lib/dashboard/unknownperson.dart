import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:firebase_database/ui/firebase_animated_list.dart';
import '../library/firebasefile.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class UnknownPerson extends StatefulWidget {
  const UnknownPerson({super.key});

  @override
  State<UnknownPerson> createState() => _UnknownPersonState();
}

class _UnknownPersonState extends State<UnknownPerson> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //extendBodyBehindAppBar: true,
      backgroundColor: Color.fromARGB(255, 255, 254, 254),
      appBar: AppBar(
        title: const Text(
          "UnKnown Person",
          style: TextStyle(color: Colors.black),
        ),
        backgroundColor: Colors.transparent,
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
