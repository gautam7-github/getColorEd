import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:url_strategy/url_strategy.dart';

void main() {
  setPathUrlStrategy();
  runApp(const BaseApp());
}

class BaseApp extends StatelessWidget {
  const BaseApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
        color: Colors.deepPurple,
        debugShowCheckedModeBanner: false,
        title: 'getColorEd',
        home: HomePage());
  }
}

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  Widget? myImage;
  bool? imageDone = false;
  final ImagePicker _picker = ImagePicker();
  void pickOneImage() async {
    final XFile? image = await _picker.pickImage(source: ImageSource.gallery);
    Widget? finalImage = Image.memory(
      await image!.readAsBytes(),
    );
    setState(() {
      imageDone = true;
      myImage = finalImage;
    });
  }

  Widget? buildImage() {
    if (imageDone == false) {
      return const Text("No Image Selected..");
    } else {
      return myImage;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              buildImage()!,
              MaterialButton(
                onPressed: pickOneImage,
                color: Colors.purple,
                padding: const EdgeInsets.all(12),
                child: const Text(
                  "Pick an Image",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 36,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
