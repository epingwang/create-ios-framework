create-iOS-framework
---

> create-ios-framework is a simple cli tool to create an iOS framework.

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

![usage gif](https://raw.githubusercontent.com/epingwang/create-ios-framework/master/images/2017-03-21%2016.12.12.gif)

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
AwesomeSDK						# root folder
├── AwesomeSDK					# sdk development folder
│   ├── AwesomeSDK				# source folder
│   │   ├── AwesomeSDK.h
│   │   ├── AwesomeClass.h
│   │   ├── AwesomeClass.m
│   ├── AwesomeSDK.bundle		# resource bundle
│   ├── AwesomeSDK.xcodeproj	# project file
├── AwesomeSDK.xcworkspace		# workspace file
│   ├── AwesomeSDKDemo			# demo project folder
...
│   │   ├── Podfile				# cocoapods podfile
│   │   ├── AwesomeSDK.podspec

```