---
title: "Windows Desktop Project Setup"
date: "2016-05-25"
---

Follow these stepsÂ toÂ set up your project with the Windows DesktopÂ brainCloud C++ SDK.

Note that if you are developing a Windows Store App, you should use the Window Store brainCloud C++ SDK. This SDK is specifically for Windows Desktop apps that do not include in the Windows Store runtime.

- Create or open a Windows Desktop/Win32Â App project with Visual Studio 2013 (**or 2015 with Platform Toolset set to Visual Studio 2013**)
- Download the Windows DesktopÂ App brainCloud C++ SDK from the "Client Libs" section of the portal
- Unzip the SDK into a folder. In our case, we will unzip to a "bc" folder within the solution folder.
- Right click your project in Solution Explorer and select Properties
- Under Configuration Properties > C/C++ > Preprocessor > General > Additional Include Directories, enter the following include:
    - $(ProjectDir)..\bc\include;$(ProjectDir)..\bc\thirdparty\jsoncpp-1.0.0
    - Note that you should do this for all configurations and all platforms
- Under Configuration Properties > Linker > Input enter the following libraries:
    - brainCloud.lib;cpprest120_2_0.lib;winhttp.lib;bcrypt.lib;crypt32.lib
    - Note that you should do this for all configurations and all platforms
- Under Configuration Properties > Linker > General > Additional Library Directories, enter the following path:
    - $(ProjectDir)\..\bc\lib\win32\debug Â <--- for Win32Â | Debug
    - Note you will need to enter a unique path for each platform and configuration.Â For instance:
        - X64 | Debug: Â $(ProjectDir)\..\bc\lib\x64\debug
        - X64 | Release: Â $(ProjectDir)\..\bc\lib\x64\release
        - Win32 | Debug:Â  $(ProjectDir)\..\bc\lib\win32\debug
        - Win32Â | Release: Â $(ProjectDir)\..\bc\lib\win32\release

Done!
