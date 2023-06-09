---
title: "Windows Store Project Setup"
date: "2016-05-25"
---

Follow these stepsÂ toÂ set up your project with the Windows Store BRAINCLOUD C++ SDK.

Note that Microsoft also refers to this as a WinRT build. This will target Windows Store Apps using the WinRT libraries on Tablets, Windows Phone, and Windows Desktop.

- Create or open a Windows Store App project with Visual Studio 2013 or 2015
- Download the Windows Store App BRAINCLOUD C++ SDK from the "Client Libs" section of the portal
- Unzip the SDK into a folder. In our case we will unzip to a "bc" folder within the solution folder.
- Right click your project in Solution Explorer and select Properties
- Under Configuration Properties > C/C++ > Preprocessor > General > Additional Include Directories, enter the following include:
    - $(ProjectDir)..\\bc\\include;$(ProjectDir)..\\bc\\thirdparty\\jsoncpp-1.0.0
    - Note that you should do this for all configurations and all platforms
- Under Configuration Properties > Linker > Input enter the following libraries:
    - BRAINCLOUDClient.lib;cpprest120\_2\_0.lib
    - Note that you should do this for all configurations and all platforms
- Under Configuration Properties > Linker > General > Additional Library Directories, enter the following path:
    - $(ProjectDir)\\..\\bc\\lib\\win8.1\\x64\\debug Â <--- for X64 | Debug
    - Note you will need to enter a unique path for each platform and configuration. Here is the matrix for Windows 8.1 RT. For Windows Phone 8.0 and 8.1, replace the "win8.1" part of the path with "winPhone8.0" or "winPhone8.1"Â respectively.
        - ARM | Debug: Â $(ProjectDir)\\..\\bc\\lib\\win8.1\\arm\\debug
        - ARM | Release: Â $(ProjectDir)\\..\\bc\\lib\\win8.1\\arm\\release
        - X64 | Debug: Â $(ProjectDir)\\..\\bc\\lib\\win8.1\\x64\\debug
        - X64 | Release: Â $(ProjectDir)\\..\\bc\\lib\\win8.1\\x64\\release
        - Win32 | Debug:Â  $(ProjectDir)\\..\\bc\\lib\\win8.1\\win32\\debug
        - Win32Â | Release: Â $(ProjectDir)\\..\\bc\\lib\\win8.1\\win32\\release

Done!
