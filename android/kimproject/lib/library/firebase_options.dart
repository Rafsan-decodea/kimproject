// File generated by FlutterFire CLI.
// ignore_for_file: lines_longer_than_80_chars, avoid_classes_with_only_static_members
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for windows - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyBiP96UgQNqzcblfcNqmp8arneThFH7SQI',
    appId: '1:186797081014:web:d9d08d73bacdd7feb30117',
    messagingSenderId: '186797081014',
    projectId: 'kimsirproject',
    authDomain: 'kimsirproject.firebaseapp.com',
    databaseURL: 'https://kimsirproject-default-rtdb.firebaseio.com',
    storageBucket: 'kimsirproject.appspot.com',
    measurementId: 'G-Q268WWQZPN',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyALZpJoYdJMpi_RIpkRXHmGqIy0Nev5f0M',
    appId: '1:186797081014:android:eaf7b8069dededccb30117',
    messagingSenderId: '186797081014',
    projectId: 'kimsirproject',
    databaseURL: 'https://kimsirproject-default-rtdb.firebaseio.com',
    storageBucket: 'kimsirproject.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyA3kJof5aKrmBIWVu-iPUeUGmMB2xwC9II',
    appId: '1:186797081014:ios:e5297ea5a0fcb70db30117',
    messagingSenderId: '186797081014',
    projectId: 'kimsirproject',
    databaseURL: 'https://kimsirproject-default-rtdb.firebaseio.com',
    storageBucket: 'kimsirproject.appspot.com',
    iosClientId: '186797081014-pa8pc42r2hp1avmg4dr8vgfaj1jgggdg.apps.googleusercontent.com',
    iosBundleId: 'com.example.kimproject',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyA3kJof5aKrmBIWVu-iPUeUGmMB2xwC9II',
    appId: '1:186797081014:ios:e5297ea5a0fcb70db30117',
    messagingSenderId: '186797081014',
    projectId: 'kimsirproject',
    databaseURL: 'https://kimsirproject-default-rtdb.firebaseio.com',
    storageBucket: 'kimsirproject.appspot.com',
    iosClientId: '186797081014-pa8pc42r2hp1avmg4dr8vgfaj1jgggdg.apps.googleusercontent.com',
    iosBundleId: 'com.example.kimproject',
  );
}
