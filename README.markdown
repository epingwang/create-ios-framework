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
AwesomeSDK                    # root folder
├── AwesomeSDK                # sdk development folder
│   ├── AwesomeSDK            # source folder
│   │   ├── AwesomeSDK.h
│   │   ├── AwesomeClass.h
│   │   ├── AwesomeClass.m
│   ├── AwesomeSDK.bundle     # resource bundle
│   ├── AwesomeSDK.xcodeproj  # project file
├── AwesomeSDK.xcworkspace    # workspace file
│   ├── AwesomeSDKDemo        # demo project folder
...
│   │   ├── Podfile           # cocoapods podfile
│   │   ├── AwesomeSDK.podspec

```

License
---

create-iOS-framework is available under the MIT license. See the LICENSE file for more info.