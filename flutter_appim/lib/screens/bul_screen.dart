import 'package:flutter/material.dart';
class BulScreen extends StatefulWidget {
  @override
  State<BulScreen> createState() => _BulScreenState();
}
class _BulScreenState extends State<BulScreen> {
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
            Center(child:
            Text("isFree= 1 & id = min değeri gelecek "))
          ],)
    );
  }
}
