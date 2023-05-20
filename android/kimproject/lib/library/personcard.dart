//import 'dart:async';

//import 'package:firebase_auth/firebase_auth.dart';
//import 'package:firebase_database/firebase_database.dart';
//import 'package:firebase_database/ui/firebase_animated_list.dart';
//import '../library/firebasefile.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
//import 'package:flutter/src/widgets/placeholder.dart';

class PersonalCard extends StatefulWidget {
  final String image;
  final String title;
  final String description;
  final String additionalInfo;

  PersonalCard({
    required this.image,
    required this.title,
    required this.description,
    required this.additionalInfo,
  });

  @override
  State<PersonalCard> createState() => _PersonalCardState();
}

class _PersonalCardState extends State<PersonalCard> {
  @override
  Widget build(BuildContext context) {
    return IntrinsicHeight(
      child: Card(
        elevation: 4.0,
        margin: const EdgeInsets.all(16.0),
        child: Row(
          children: [
            Expanded(
              flex: 2,
              child: Stack(
                alignment: Alignment.center,
                children: [
                  CircularProgressIndicator(), // show the progress indicator
                  Container(
                    decoration: BoxDecoration(
                      border: Border.all(
                        color: Color.fromARGB(255, 131, 11, 243),
                        width: 2.0,
                      ),
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                    padding: EdgeInsets.all(5.0),
                    child: Image.network(
                      widget.image,
                      fit: BoxFit.cover,
                      height: 100.0,
                      width: 130.0, // set the scaling mode of the image
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              flex: 2,
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      widget.title,
                      style: const TextStyle(
                        fontSize: 20.0,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 8.0),
                    Text(
                      widget.description,
                      style: const TextStyle(fontSize: 16.0),
                    ),
                    const SizedBox(height: 8.0),
                    Text(
                      widget.additionalInfo,
                      style: const TextStyle(fontSize: 16.0),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}


 // PersonalCard(
                                //   image: snapshot
                                //       .child('image_url')
                                //       .value
                                //       .toString(),
                                //   title:
                                //       snapshot.child('name').value.toString(),
                                //   description: snapshot
                                //       .child('degination')
                                //       .value
                                //       .toString(),
                                //   additionalInfo:
                                //       snapshot.child('type').value.toString(),
                                // ),