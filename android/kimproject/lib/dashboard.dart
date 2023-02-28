import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:sliding_sheet/sliding_sheet.dart';

class Dashboard extends StatefulWidget {
  const Dashboard({Key? key}) : super(key: key);

  @override
  State<Dashboard> createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> {
  aboutAchivements(num, type) {
    return Row(
      children: [
        Text(
          num,
          style: TextStyle(
            fontSize: 30,
            fontWeight: FontWeight.bold,
            fontFamily: "Soho",
          ),
          textAlign: TextAlign.center,
        ),
        Container(
            margin: EdgeInsets.only(top: 10),
            child: Text(
              type,
              style: TextStyle(
                fontFamily: "Soho",
              ),
            ))
      ],
    );
  }

  mySpec(icon, text, link) {
    return Container(
      child: Card(
        margin: EdgeInsets.all(0),
        color: Color(0xff252525),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15),
        ),
        child: Container(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              IconButton(
                splashColor: Colors.green,
                icon: Icon(
                  icon,
                  color: Colors.white,
                ),
                onPressed: () {
                  Navigator.pushNamed(context, link);
                },
              ),
              SizedBox(
                height: 10,
              ),
              Text(
                text,
                style: const TextStyle(
                    fontSize: 16, fontFamily: "Soho", color: Colors.white),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      ),
      height: 115,
      width: 105,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      backgroundColor: Colors.black,
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Colors.transparent,
        leading: PopupMenuButton(
            color: Colors.white,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(7),
            ),
            icon: Icon(Icons.menu),
            itemBuilder: (context) => [
                  // PopupMenuItem(
                  //   child: TextButton(
                  //       child: Text(
                  //         'Projects',
                  //         style: TextStyle(
                  //           color: Color.fromARGB(255, 8, 8, 8),
                  //         ),
                  //       ),
                  //       onPressed: () {
                  //         Navigator.pushNamed(context, '/project');
                  //       }),
                  //   value: 1,
                  // ),
                  PopupMenuItem(
                    child: TextButton(
                        child: Text(
                          'About Me',
                          style:
                              TextStyle(color: Color.fromARGB(255, 17, 17, 17)),
                        ),
                        onPressed: () {
                          Navigator.pushNamed(context, '/about');
                        }),
                    value: 2,
                  )
                ]),
      ),
      body: SlidingSheet(
        elevation: 8,
        cornerRadius: 50,
        snapSpec: const SnapSpec(
          // Enable snapping. This is true by default.
          snap: true,
          // Set custom snapping points.
          snappings: [0.38, 0.7, 1.0],
          // Define to what the snappings relate to. In this case,
          // the total available space that the sheet can expand to.
          positioning: SnapPositioning.relativeToAvailableSpace,
        ),
        // The body widget will be displayed under the SlidingSheet
        // and a parallax effect can be applied to it.
        body: Container(
          child: Stack(
            children: [
              Container(
                margin: EdgeInsets.only(top: 35),
                child: ShaderMask(
                  shaderCallback: (rect) {
                    return LinearGradient(
                      begin: Alignment.center,
                      end: Alignment.bottomCenter,
                      colors: [Colors.black, Colors.transparent],
                    ).createShader(
                        Rect.fromLTRB(0, 0, rect.width, rect.height));
                  },
                  blendMode: BlendMode.dstIn,
                  child: Padding(
                    padding: const EdgeInsets.only(left: 25),
                    child: Image.asset(
                      'assests/rafsan.png',
                      height: 400,
                      fit: BoxFit.contain,
                    ),
                  ),
                ),
              ),
              Container(
                alignment: Alignment.center,
                margin: EdgeInsets.only(
                    top: MediaQuery.of(context).size.height * 0.49),
                child: Column(
                  children: [
                    Text('Your Company name',
                        style: TextStyle(
                            fontFamily: "Soho",
                            color: Colors.white,
                            fontSize: 35,
                            fontWeight: FontWeight.bold)),
                    SizedBox(
                      height: 2,
                    ),
                    Text(
                      'Rafsan Software Developer',
                      style: TextStyle(
                          color: Colors.white,
                          fontFamily: "Soho",
                          fontSize: 20),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
        builder: (context, state) {
          // This is the content of the sheet that will get
          // scrolled, if the content is bigger than the available
          // height of the sheet.
          return Container(
            margin: EdgeInsets.only(left: 20, top: 30, right: 20),
            height: 1000,
            child: Container(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      aboutAchivements('100%', ' Quality'),
                      aboutAchivements('100%', ' Clients Satisfaction'),
                    ],
                  ),
                  SizedBox(
                    height: 30,
                  ),
                  const Text(
                    'Check Out Our Detailes',
                    style: TextStyle(
                        fontSize: 20,
                        fontFamily: "Soho",
                        fontWeight: FontWeight.bold),
                  ),
                  SizedBox(
                    height: 10,
                  ),
                  Column(
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          mySpec(FontAwesomeIcons.home, 'Home\nDelivary',
                              '/homedelivary'),
                          mySpec(FontAwesomeIcons.checkCircle,
                              'Client\nSatisfied', '/clientsatisfied'),
                          mySpec(FontAwesomeIcons.flag, 'AboutUS', '/aboutus'),
                        ],
                      ),
                    ],
                  )
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
