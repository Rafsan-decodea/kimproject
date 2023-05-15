import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class ImageCapturePopup extends StatefulWidget {
  @override
  _ImageCapturePopupState createState() => _ImageCapturePopupState();
}

class _ImageCapturePopupState extends State<ImageCapturePopup> {
  File? _image;

  Future<void> _pickImage(ImageSource source) async {
    final picker = ImagePicker();
    final pickedImage = await picker.getImage(source: source);

    if (pickedImage != null) {
      setState(() {
        _image = File(pickedImage.path);
      });
    }
    Navigator.pop(context, _image);
  }

  @override
  Widget build(BuildContext context) {
    return SimpleDialog(
      title: Text('Capture Image'),
      children: [
        if (_image != null) ...[
          Image.file(_image!),
          SizedBox(height: 16.0),
        ],
        ListTile(
          leading: Icon(Icons.camera),
          title: Text('Capture from Camera'),
          onTap: () => _pickImage(ImageSource.camera),
        ),
        ListTile(
          leading: Icon(Icons.photo_library),
          title: Text('Pick from Gallery'),
          onTap: () => _pickImage(ImageSource.gallery),
        ),
      ],
    );
  }
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Image Capture Popup Example'),
        ),
        body: Center(
          child: ElevatedButton(
            onPressed: () {
              showDialog(
                context: context,
                builder: (BuildContext context) {
                  return ImageCapturePopup();
                },
              );
            },
            child: Text('Open Image Capture'),
          ),
        ),
      ),
    );
  }
}
