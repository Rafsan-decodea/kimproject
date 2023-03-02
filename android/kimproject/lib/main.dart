import 'dart:async';
import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:kimproject/dashboard/dashboard.dart';
import 'package:kimproject/login.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'library/firebase_options.dart';
import 'about.dart';

import 'package:kimproject/library/notification.dart';

main() {
  WidgetsFlutterBinding.ensureInitialized();
  Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  runApp(const MyApp());
}

class SplashScreen extends StatelessWidget {
  // Space Screen For Automatice Redirect
  const SplashScreen({super.key});
  void _redirect(BuildContext context) {
    Timer(const Duration(seconds: 5), () {
      Navigator.pushReplacement(
        context,
        PageRouteBuilder(
          pageBuilder: (context, animation, secondaryAnimation) =>
              const MyLogin(),
          transitionsBuilder: (context, animation, secondaryAnimation, child) {
            return SlideTransition(
              position: Tween<Offset>(
                begin: const Offset(1.0, 0.0),
                end: Offset.zero,
              ).animate(animation),
              child: child,
            );
          },
        ),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    _redirect(context);
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              height: 200, // Set the height of the container
              width: 200,
              // decoration: const BoxDecoration(
              //   image: DecorationImage(
              //     image: AssetImage("images/cctv.png"),
              //     fit: BoxFit.cover,
              //   ),
              // ),
              child: const FadeInImage(
                placeholder: AssetImage('images/cctv.png'),
                image: AssetImage('images/cctv.png'),
                fadeInDuration: Duration(milliseconds: 1500),
                fadeInCurve: Curves.easeIn,
                fit: BoxFit.cover,
              ),
            ),
            Container(
                child: AnimatedTextKit(
              animatedTexts: [
                TypewriterAnimatedText(
                  'Face Recognization Project',
                  textStyle: const TextStyle(
                    fontSize: 25.0,
                    fontWeight: FontWeight.bold,
                  ),
                  speed: const Duration(milliseconds: 100),
                ),
              ],
              totalRepeatCount: 1,
              pause: const Duration(milliseconds: 100),
              displayFullTextOnTap: true,
              stopPauseOnTap: true,
            ))
          ],
        ),
      ),
    );
  }
}

//Entry Point
class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final auth = FirebaseAuth.instance;
  final ref = FirebaseDatabase.instance.ref("users");
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: SplashScreen(),
      routes: {
        '/about': (context) => const AboutUs(),
        '/logout': (context) => const MyLogin(),
      },
    );
  }
}
