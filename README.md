# dotfilesQtile (Arch)
Simple dotfiles for Qtile - Linux Tiling Window Manager. Made to look like Hyprland with the gaming experience of Xorg. **The config will only work with _Xorg_.**

# Installation
To use the dotfiles you need some packages (some of them listed below with a short explanation why you need them). All of the packages can be installed using the `install.sh` script that can be found in the _scripts_ folder (qtile included) (YOU HAVE TO INSTALL YAY  AND XORG.SERVER FIRST). Packages installed with pacman are what you need for most of the functionalities in the system to work + qt5ct and kvantum to change the qt theme. Yay installs some additional look related stuff like icon theme, cursor theme and nwg-look which will help you set the GTK theme.

To get the WM to  work properly you need to copy the files to coresponding directories:
 - Insides of the _config_ folder => `~/.config/`
 - Files in _xorgConfig_ folder => `~/`

To get catppuccin grub theme to work (with some changes I like - restart/shutdown buttons, changed position of the menu) you need to replicate these steps:
 - Place catppuccin-mocha theme folder in either `/boot/grub/themes/` or `/usr/share/grub/themes/`
 - Edit the theme in `/etc/default/grub/` file by adding a path to the `theme.txt` file from freshly moved _catppuccin-mocha_ folder
 - Move the `40_custom` file to `/etc/grub.d/` folder
 - Update the grub

In the _scripts_ folder you will also find `additional_apps.sh` script. This script will install some additional, not required, applicaitons that I like to use in my system.


# Packages explained (apart from qtile and Xorg):
 - picom (compositor)
 - nitrogen (wallpaper utility)
 - pacman-contrib (needed for checkupdates widget)
 - rofi (dmenu)
 - dunst (notifications)
 - kitty (terminal)
 - polkit-kde-agent (graphical authentication thingy - can be changed in autostart.sh)
 - nwg-look (GUI to set the GTK theme)
 - qt5ct, kvantum (GUI's to set the QT theme)


# Some additional info
The bar itself is divided into segments:
LEFT: Calendar, CPU usage, RAM usage, Window name
MIDDLE: Workspaces
RIGHT: system tray, checkupdates widget (pacman-contrib has to be installed), sound, battery, clock

The sound widget opens the _pavucontrol_ app on mouse left click. You can change the volume with mouse scroll and mute the sound with right click.

Terminal used is Kitty but can be changed to anything else thanks to qtile's guess_terminal().

Hope you like it as a base for your own rice or even as a ready to go config. I'm definitely going to update this config since Xorg is the only option for nvidia laptop gaming now and qtile seems to be a really nice WM


# Themes used:
 - [Catppuccin](https://github.com/catppuccin) Mocha Lavender (GTK and QT/Kvantum)
 - [Bibata Original Classic](https://github.com/ful1e5/Bibata_Cursor) Cursor Theme
 - [Tela Black Dark](https://github.com/vinceliuice/Tela-icon-theme) Icon theme


# Some ScreenShots

![Screenshot](/screenshots/WholeFloating.png)
![Screenshot](/screenshots/WholeEmpty.png)
![Screenshot](/screenshots/WholeTiled.png)
