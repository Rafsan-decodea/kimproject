import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:firebase_storage/firebase_storage.dart';

final auth = FirebaseAuth.instance;
final ref = FirebaseDatabase.instance.ref("intruder");

void deleteData(dynamic key, dynamic imageURL) {
  final ref = FirebaseDatabase.instance.ref("intruder");
  final storageRef = FirebaseStorage.instance.refFromURL(imageURL);

  storageRef.delete().then((_) {
    print("Storage data deleted successfully");
  }).catchError((error) {
    print("Failed to delete storage data: $error");
  });

  ref.child(key).remove();
}
