import 'package:flutter/material.dart';
class OtomatikScreen extends StatefulWidget {
  @override
  State<OtomatikScreen> createState() => _OtomatikScreenState();
}
class _OtomatikScreenState extends State<OtomatikScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Colors.white,
        iconTheme: IconThemeData(color:Color(0xff4226ED),size: 30,
        ),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
        Center(child: Text("isFree=1 olanlar Buraya Listelenecek"))
      ],)
    );
  }
}
