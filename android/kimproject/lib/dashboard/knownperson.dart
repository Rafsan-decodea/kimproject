import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:firebase_database/ui/firebase_animated_list.dart';
import 'package:kimproject/library/personcard.dart';
import '../library/firebasefile.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class KnownPerson extends StatefulWidget {
  const KnownPerson({super.key});

  @override
  State<KnownPerson> createState() => _KnownPersonState();
}

class _KnownPersonState extends State<KnownPerson> {
  Color buttonColor = Colors.blue;

  @override
  void initState() {
    super.initState();
    startColorAnimation();
  }

  void startColorAnimation() {
    Timer.periodic(Duration(seconds: 2), (timer) {
      setState(() {
        buttonColor =
            buttonColor == Color.fromARGB(255, 2, 13, 22).withOpacity(0.7)
                ? Colors.green.withOpacity(0.7)
                : Color.fromARGB(255, 198, 243, 33).withOpacity(0.7);
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //extendBodyBehindAppBar: true,
      backgroundColor: Color.fromARGB(255, 255, 254, 254),
      appBar: AppBar(
        title: const Text(
          "Known Person",
          style: TextStyle(color: Colors.black),
        ),
        backgroundColor: Colors.transparent,
      ),
      body: Stack(
        children: [
          SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                PersonalCard(
                  image:
                      "https://img.freepik.com/free-photo/young-bearded-man-with-striped-shirt_273609-5677.jpg",
                  title: "asd",
                  description: "asd",
                  additionalInfo: "asd",
                ),
                PersonalCard(
                  image:
                      "https://img.freepik.com/free-photo/young-bearded-man-with-striped-shirt_273609-5677.jpg",
                  title: "asd",
                  description: "asd",
                  additionalInfo: "asd",
                ),
                PersonalCard(
                  image:
                      "https://img.freepik.com/free-photo/young-bearded-man-with-striped-shirt_273609-5677.jpg",
                  title: "asd",
                  description: "asd",
                  additionalInfo: "asd",
                ),
                PersonalCard(
                  image:
                      "https://img.freepik.com/free-photo/young-bearded-man-with-striped-shirt_273609-5677.jpg",
                  title: "asd",
                  description: "asd",
                  additionalInfo: "asd",
                ),
                PersonalCard(
                  image:
                      "https://img.freepik.com/free-photo/young-bearded-man-with-striped-shirt_273609-5677.jpg",
                  title: "asd",
                  description: "asd",
                  additionalInfo: "asd",
                ),
              ],
            ),
          ),
          Positioned(
            bottom: 50.0,
            right: 140.0,
            child: AnimatedContainer(
              duration: Duration(milliseconds: 500),
              curve: Curves.easeInOut,
              width: 60.0,
              height: 60.0,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: buttonColor,
              ),
              child: IconButton(
                onPressed: () {
                  // Add your logic for the "Add People" button here
                },
                icon: Icon(
                  Icons.add,
                  size: 36.0,
                  color: Colors.white,
                ),
              ),
            ),
          )
        ],
      ),
    );
  }
}
