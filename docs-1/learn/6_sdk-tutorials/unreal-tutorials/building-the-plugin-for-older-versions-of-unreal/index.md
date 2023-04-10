---
title: "Building The Plugin For Older Versions of Unreal"
date: "2016-07-12"
---

New versions of brainCloud will always include both C++ source code and compiled binaries forÂ the latest version of Unreal available when released. Â However, if you are required to use an older version of Unreal but need the latest brainCloud features you will need to recompile the binaries.

**NOTE:** This is only required if your project is a **Blueprint Only** project! Source code projects will automatically prompt you to recompile if the binaries do not match your engine version.

## Building The brainCloud Plugin

To begin, download the latest version of the brainCloud plugin from the Portal. Â Client downloads can be found under Core App Info | Platforms.

Once you've got the latest plugin perform these steps:

- Extract the zip
- Inside the extracted folder, find the Binaries folder under BCClient
- Delete the Binaries folder

We now need to create a project to recompile the source in.

- Open the Unreal Editor and create a newÂ **C++** project.
- Close the editor and Visual Studio/Xcode if they are open
- Navigate to the newly created project's root directory
- Create a new folder called Plugins
- Move the BCClient folder from the extracted zip into the Plugins folder

Now we're ready to recompile the binaries. Â Open the uproject file for the project and you should see this prompt:

[![unreal_plugin_build](images/unreal_plugin_build.png)](images/unreal_plugin_build.png)

Click Yes to rebuild the binaries for the plugin. Â Once the buildÂ is complete the editor will open, close the editor to continue.

Navigate to the Project Root | Plugins | BCClient folder and you should see two new folders,Â Binaries and Intermediate.

- Delete the Intermediate folder
- Copy the BCClient folder out of the build project

The new BCClient folder is now ready to be added to your blueprint only project! Â If you haven't yet installed the plugin in your project see [here for instructions](/learn/sdk-tutorials/unreal-tutorials/setting-up-the-braincloud-plugin/).
