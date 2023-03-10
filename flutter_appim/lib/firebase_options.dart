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
    apiKey: 'AIzaSyBaraVnOElm7ugUeD29ndw8NIoAMoxw508',
    appId: '1:718091044983:web:50eb0607b5e6489ed71e72',
    messagingSenderId: '718091044983',
    projectId: 'park-space-detection',
    authDomain: 'park-space-detection.firebaseapp.com',
    storageBucket: 'park-space-detection.appspot.com',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyBskU8VMt1zzUH4-By-IPPLZh2n63ZOBoA',
    appId: '1:718091044983:android:a8c89bbd89251290d71e72',
    messagingSenderId: '718091044983',
    projectId: 'park-space-detection',
    storageBucket: 'park-space-detection.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyD2XryZB3fvH9lLz0GJl4HV1vsokrPMRsU',
    appId: '1:718091044983:ios:007e3017f927c506d71e72',
    messagingSenderId: '718091044983',
    projectId: 'park-space-detection',
    storageBucket: 'park-space-detection.appspot.com',
    iosClientId: '718091044983-f3ucueo8gpn8j9q39l4c7oqhhubhbgjd.apps.googleusercontent.com',
    iosBundleId: 'com.example.flutterAppim',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyD2XryZB3fvH9lLz0GJl4HV1vsokrPMRsU',
    appId: '1:718091044983:ios:007e3017f927c506d71e72',
    messagingSenderId: '718091044983',
    projectId: 'park-space-detection',
    storageBucket: 'park-space-detection.appspot.com',
    iosClientId: '718091044983-f3ucueo8gpn8j9q39l4c7oqhhubhbgjd.apps.googleusercontent.com',
    iosBundleId: 'com.example.flutterAppim',
  );
}
