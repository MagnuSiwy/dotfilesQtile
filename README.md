# Dotfiles for [Qtile](https://github.com/qtile/qtile/) Tiling Window Manager (only for Arch based distros)
Made to look like Hyprland with the gaming experience of Xorg (perfect for nvidia laptops). **The config will only work with _Xorg_.**

## The dotfiles haven't been updated after Qtile v0.24.0. Some things might not work!!!

# Installation
To use the dotfiles you need some packages (some of them listed below with a short explanation why you need them). All of the packages can be installed using the `install.sh` script that can be found in the _scripts_ folder. Qtile and qtile-extras are NOT included since the config is using git versions of these packages - the config will NOT work on the official releases of qtile + qtile-extras. **THIS MEANS YOU HAVE TO INSTALL YAY, QTILE-GIT, QTILE-EXTRAS-GIT AND XORG.SERVER FIRST**. Packages installed with pacman are what you need for most of the functionalities in the system to work + qt6ct and kvantum to change the qt theme. Yay installs mostly some additional look related stuff like icon theme, cursor theme and nwg-look which will help you set the GTK theme.

If you want to use the released qtile and qtile-extras packages, you have to duplicate the code for the bar to use it on the second monitor. Regular copy and deepcopy are not going to work.

To get the WM to  work properly you need to copy/link the files to coresponding directories:
 - Insides of the _config_ folder => `~/.config/`
 - Files in _xorgConfig_ folder => `~/`

To get catppuccin grub theme to work (with some changes I like - restart/shutdown buttons, changed position of the menu) you need to replicate these steps:
 - Place catppuccin-mocha theme folder in either `/boot/grub/themes/` or `/usr/share/grub/themes/`
 - Edit the theme in `/etc/default/grub/` file by adding a path to the `theme.txt` file from freshly moved _catppuccin-mocha_ folder
 - Move/copy/link the `40_custom` file to `/etc/grub.d/` folder
 - Update the grub

 You have to seperately install Roboto Mono Nerd Font, since it is used in the rofi config.

In the _scripts_ folder you will also find `additional_apps.sh` script. This script will install some additional, not required, applicaitons that I like to use in my system.


# Packages explained (apart from qtile and Xorg):
 - [qtile-extras](https://github.com/elParaguayo/qtile-extras) (a package used for widget decorations and power menu)
 - [picom](https://github.com/yshui/picom) (compositor)
 - [rofi](https://github.com/davatorium/rofi) (dmenu - Roboto Mono Nerd Font needed)
 - [dunst](https://github.com/dunst-project/dunst) (notifications)
 - [kitty](https://github.com/kovidgoyal/kitty) (terminal)
 - [polkit-kde-agent](https://github.com/KDE/polkit-kde-agent-1) (graphical authentication thingy - can be changed in autostart.sh)
 - [nwg-look](https://github.com/nwg-piotr/nwg-look) (GUI to set the GTK theme)
 - [flameshot](https://github.com/flameshot-org/flameshot) (screenshot utility - you can disable the tray icon in settings)
 - [calcurse](https://github.com/lfos/calcurse) (terminal calendar)
 - [blueman](https://github.com/blueman-project/blueman) (GUI for handling bluetooth devices - to disable the tray icon go to View->Plugins and disable StatusIcon)
 - qt6ct, kvantum (GUI's to set the QT theme)
 - pacman-contrib (needed for checkupdates widget)


# Some additional info
The bar itself is divided into segments:
 - LEFT: PowerMenu, Calendar, CPU usage, RAM usage, Updates Checker (pacman-contrib has to be installed), Window name
 - MIDDLE: Workspaces
 - RIGHT: System Tray, Sound, Bluetooth, WiFi, Battery, Clock

The sound widget opens the _pavucontrol_ app on mouse right click. You can change the volume with mouse scroll and mute the sound with left click. WiFi and bluetooth widgets work similarly. The first one opens _nm-connectino-editor_ on right click and the second one opens _blueman-manager_ on left click. Also calendar widget opens _calcurse_ and checkupdates widget opens your terminal with _checkupdates_ program.

There are three widgets that open popups from _qtile-extras_. PowerMenu opens power menu, bluetooth widgets opens a popup with some options and devices, battery widget open brightness options **(Beware that you might have to change one variable in brightness.sh or monitors.sh scripts - Instructions can be found in the files)**.

The terminal I'm using is Kitty but it can be changed to anything else thanks to qtile's guess_terminal(). Not all of the widgets and keybinds might work properly since kitty might have some specific options/arguments used in the config.

Hope you like it as a base for your own rice or even as a ready to go config. I'm trying to update this config regularly since Xorg is the only option that works properly with nvidia laptops for gaming right now.


# Themes used:
 - [Catppuccin](https://github.com/catppuccin) Mocha Lavender (GTK and QT/Kvantum)
 - [Bibata Original Classic](https://github.com/ful1e5/Bibata_Cursor) Cursor Theme
 - [Tela Black Dark](https://github.com/vinceliuice/Tela-icon-theme) Icon theme


# Screenshots

![Screenshot](/screenshots/NewBarWholeFloatingV2.png)
![Screenshot](/screenshots/NewBarWholeEmptyV2.png)
![Screenshot](/screenshots/NewBarWholeTiledV2.png)
![Screenshot](/screenshots/WholePowerMenu.png)
