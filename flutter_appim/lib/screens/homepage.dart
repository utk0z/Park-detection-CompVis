import 'package:flutter/material.dart';
import 'package:flutter_appim/screens/bul_screen.dart';
import 'package:flutter_appim/screens/otomatik_screen.dart';
class Homepage extends StatefulWidget {
  @override
  _HomepageState createState() => _HomepageState();
}
class _HomepageState extends State<Homepage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            
            Image.asset('images/deneme.png',width: 125,height: 125,fit: BoxFit.fill,),

          SizedBox(height: 50,),
          Center(
            child:  GestureDetector(
              onTap: () => Navigator.push(context, MaterialPageRoute(builder: (context) => BulScreen() ,)),
              child: Container(padding: EdgeInsets.symmetric(horizontal: 30,vertical: 15),
                decoration: BoxDecoration(color:Colors.grey[300],borderRadius: BorderRadius.all(Radius.circular(25))),
                child: Text("Boş Park Alanı Bul",style: TextStyle(color: Color.fromARGB(255, 52, 32, 184) ,fontWeight: FontWeight.bold,fontSize: 15)),
              ),
            ),
          ),
          SizedBox(height: 20,),
          GestureDetector(
            onTap: () => Navigator.push(context, MaterialPageRoute(builder: (context) => OtomatikScreen() ,)),
            child: Container(padding: EdgeInsets.symmetric(horizontal: 30,vertical: 15),
              decoration: BoxDecoration(color:Color(0xff4226ED),borderRadius: BorderRadius.all(Radius.circular(25))),
              child: Text("Boş Park Alanları",style: TextStyle(color: Colors.white,fontWeight: FontWeight.bold,fontSize: 15)),
            ),
          ),
        ],),
      )
    );
  }
}