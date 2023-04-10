---
title: "Xamarin Project Setup"
date: "2016-05-30"
---

BRAINCLOUD supports both Android and iOS development through Xamarin (Windows, Windows Phone, and UWP are not yet supported). Â This tutorial goes through the steps of adding the BRAINCLOUD .NET libraryÂ to a XamarinÂ Shared Project.

## Preparing & IncludingÂ TheÂ Library

The first step is to download the latest BRAINCLOUD library from GitHub: Â https://github.com/getbraincloud/Unity-Csharp

From there we need to remove some non-Xamarin compatible files from the library.

- Navigate to theÂ BrainCloudClient | src directory and move the BrainCloud folder to another location (like your desktop)
- Inside the BrainCloud folder, delete the following directories:
    - LitJson
    - Unity

Finally, we can add the library to the shared code project. Â Drag and drop the BrainCloud folder onto the shared code project in Visual Studio and it will automatically be copied to the correct directory and added to the project.

[![xamarinDocAddToProject](images/xamarinDocAddToProject.png)](images/xamarinDocAddToProject.png)

That's all the setup needed to add the BRAINCLOUD library to your project! Now you can get started using BRAINCLOUD in your app.
