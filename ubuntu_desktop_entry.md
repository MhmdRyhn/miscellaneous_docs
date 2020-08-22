# Ubuntu Desktop Entry
Sometimes it happens that an application has been installed but the desktop shortcut has not been created. In those 
cases, we can create desktop entry by our own. To do that we need to create a file with extension `.desktop`, e.g., 
**PyCharm.desktop** for PyCharm. Then add the following content to the file. Make sure {xxxxx} are replaced with 
actual value. And, also make sure that the **Shebang** path for `xdg-open` is correct.

```text
#!/usr/bin/xdg-open

[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec={/path/to/the/executable}
Name={ApplicationName}
Comment={Some comment about the application}
Icon={/path/to/the/application/image}
```
After adding the content to the file save it and then allow the executable permission to the .desktop file.
```shell script
sudo chmod +x /apth/to/the/Application.desktop
```
Now, open the application by double clicking the .desktop file. It'll show a dialog box saying **Untrusted 
Application Launcher**. Click **Trust and Launch** button it'll convert the .desktop file into a desktop 
entry with the icon and launch the application.
