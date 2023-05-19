import 'dart:async';
//import 'dart:io';
//import 'package:firebase_auth/firebase_auth.dart';
//import 'package:firebase_database/firebase_database.dart';
//import 'package:firebase_database/ui/firebase_animated_list.dart';
import 'package:firebase_database/ui/firebase_animated_list.dart';
import 'package:kimproject/library/personcard.dart';
import 'package:kimproject/library/publicvar.dart';
import '../library/capimage.dart';
import '../library/firebasefile.dart';
//import '../library/firebasefile.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
//import 'package:flutter/src/widgets/placeholder.dart';

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
      body: Column(
        children: [
          Expanded(
              child: FirebaseAnimatedList(
            query: intruderRef,
            defaultChild: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Center(
                    child: Text(
                  "Loading Data ....",
                  style: TextStyle(fontSize: 30),
                ))
              ],
            ),
            itemBuilder: (context, snapshot, animation, index) {
              return Padding(
                padding: const EdgeInsets.only(top: 6),
                child: ListTile(
                  title: Column(
                    children: [
                      PersonalCard(
                        image: snapshot.child('image_url').value.toString(),
                        title: snapshot.child('name').value.toString(),
                        description:
                            snapshot.child('degination').value.toString(),
                        additionalInfo: snapshot.child('type').value.toString(),
                      ),
                    ],
                  ),
                  subtitle: Stack(
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
                          snapshot.child('image').value.toString(),
                          fit:
                              BoxFit.cover, // set the scaling mode of the image
                        ),
                      ),
                    ],
                  ),
                  splashColor: Colors.red,
                ),
              );
            },
          )),
        ],
      ),
    );
  }
}

class PersonInfo extends StatefulWidget {
  const PersonInfo({super.key});

  @override
  State<PersonInfo> createState() => _PersonInfoState();
}

class _PersonInfoState extends State<PersonInfo> {
  @override
  Widget build(BuildContext context) {
    return ImageInfoDialog(imagePath: PubicImageStoreVar.imagePathValue.value);
  }
}
