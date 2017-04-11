create-iOS-framework
---

> Create an iOS framework project with a single command.

Why might you need this?
---

If you are looking to create an iOS framework project, you need to at least create two projects (a framework project and a demo project), add dependencies using some scripts in Build Phases and create a resource bundle for some pictures and localization strings. Setting this up is time-consuming.

This is where this tool comes in. It creates a boilerplate with all the best practices. Happy hacking with your iOS framework.

If something doesn’t work please [file an issue](https://github.com/epingwang/create-ios-framework/issues/new).

Install
---

```bash
$ pip install create-ios-framework
```

Usage
---

```bash
$ create-ios-framework
```

![usage gif](https://raw.githubusercontent.com/epingwang/files/master/2017-04-11%2011.10.07.gif)

Configuration
---

You can write your own config file to generate your awesome framework.

```
[create_framework_config]
projectName=AwesomeSDK
prefix=com.awesome
organizationName=Awesome Kit
```

Save the content above in config.cfg and then

```bash
$ create-ios-framework -f config.cfg
```

Framework project structure
---

```
├── AwesomeSDK                          # sdk development folder
│   ├── AwesomeSDK                      # source folder
│   │   ├── AwesomeSDK.h
│   │   ├── AwesomeSDKViewController.h
│   │   ├── AwesomeSDKViewController.m
│   │   └── Info.plist
│   ├── AwesomeSDK.bundle               # resource bundle
│   │   ├── en.lproj                    # localizations
│   │   │   └── Localizable.strings
│   │   ├── somepic@2x.png
│   │   └── zh-Hans.lproj
│   │       └── Localizable.strings
│   └── AwesomeSDK.xcodeproj
├── AwesomeSDK.xcworkspace
└── AwesomeSDKDemo                      # demo project folder
    ├── AwesomeSDK.bundle               # copied resource bundle from SDK project
    │   ├── en.lproj
    │   │   └── Localizable.strings
    │   └── zh-Hans.lproj
    │       └── Localizable.strings
    ├── AwesomeSDK.podspec              # podspec
    ├── AwesomeSDKDemo
    ├── AwesomeSDKDemo.xcodeproj
    ├── Podfile
    └── Pods
```

License
---

create-iOS-framework is available under the MIT license. See the LICENSE file for more info.