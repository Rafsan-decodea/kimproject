import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class ImageCaptureDialog extends StatefulWidget {
  @override
  _ImageCaptureDialogState createState() => _ImageCaptureDialogState();
}

class _ImageCaptureDialogState extends State<ImageCaptureDialog> {
  late File? _image;

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
    return AlertDialog(
      title: Text('Image Capture'),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (_image != null) ...[
            Image.file(_image!),
            SizedBox(height: 16.0),
          ],
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              ElevatedButton.icon(
                onPressed: () => _pickImage(ImageSource.camera),
                icon: Icon(Icons.camera),
                label: Text('Capture from Camera'),
              ),
              ElevatedButton.icon(
                onPressed: () => _pickImage(ImageSource.gallery),
                icon: Icon(Icons.photo_library),
                label: Text('Pick from Gallery'),
              ),
            ],
          ),
        ],
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context, null),
          child: Text('Cancel'),
        ),
      ],
    );
  }
}

void _showImageCaptureDialog(BuildContext context) async {
  final image = await showDialog<File>(
    context: context,
    builder: (BuildContext context) {
      return ImageCaptureDialog();
    },
  );

  if (image != null) {
    // Perform desired actions with the captured image
    // such as uploading, processing, etc.
  }
}
