import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:kimproject/library/publicvar.dart';
import 'package:permission_handler/permission_handler.dart';

class ImageCapturePopup extends StatefulWidget {
  @override
  _ImageCapturePopupState createState() => _ImageCapturePopupState();
}

class _ImageCapturePopupState extends State<ImageCapturePopup> {
  File? _image;

  Future<void> _checkPermissionAndPickImage(ImageSource source) async {
    final PermissionStatus status = await Permission.camera.request();
    if (status.isGranted) {
      _pickImage(source);
    } else if (status.isDenied) {
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text('Permission Denied'),
            content: Text('Please grant camera permission in settings.'),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context),
                child: Text('OK'),
              ),
            ],
          );
        },
      );
    } else if (status.isPermanentlyDenied) {
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text('Permission Denied'),
            content: Text(
                'Camera permission is permanently denied. Please enable it in app settings.'),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context),
                child: Text('OK'),
              ),
            ],
          );
        },
      );
    }
  }

  Future<void> _pickImage(ImageSource source) async {
    final picker = ImagePicker();
    final pickedImage = await picker.getImage(source: source);

    if (pickedImage != null) {
      setState(() {
        _image = File(pickedImage.path);
        PubicImageStoreVar.updateImagePathValue(
            File(pickedImage.path).toString());

        // print(PublicValue.imagePathValue.value);
      });
    }
    Navigator.pop(context, _image);
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text('Capture Image'),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          ElevatedButton.icon(
            onPressed: () => _checkPermissionAndPickImage(ImageSource.camera),
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
    );
  }
}

class ImageInfoDialog extends StatefulWidget {
  final String imagePath;

  ImageInfoDialog({required this.imagePath});

  @override
  _ImageInfoDialogState createState() => _ImageInfoDialogState();
}

class _ImageInfoDialogState extends State<ImageInfoDialog> {
  String infoText = '';
  File? capturedImage;

  @override
  void initState() {
    super.initState();
    capturedImage = File(widget.imagePath);
  }

  void showImage() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          content: Container(
            width: double.maxFinite,
            height: 200,
            decoration: BoxDecoration(
              image: DecorationImage(
                image: FileImage(capturedImage!),
                fit: BoxFit.cover,
              ),
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text('Close'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text('Image Information'),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (capturedImage != null)
            GestureDetector(
              onTap: showImage,
              child: Container(
                width: 200,
                height: 200,
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: FileImage(capturedImage!),
                    fit: BoxFit.cover,
                  ),
                ),
              ),
            ),
          TextField(
            onChanged: (value) {
              setState(() {
                infoText = value;
              });
            },
            decoration: InputDecoration(
              hintText: 'Enter necessary information',
            ),
          ),
        ],
      ),
      actions: [
        TextButton(
          onPressed: () {
            // Process the captured image and information here
            // You can save the image, store the information, etc.

            // Close the dialog
            Navigator.pop(context);
          },
          child: Text('Save'),
        ),
        TextButton(
          onPressed: () {
            // Close the dialog
            Navigator.pop(context);
          },
          child: Text('Cancel'),
        ),
      ],
    );
  }
}
