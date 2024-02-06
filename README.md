# dotfilesQtile (Arch)
Simple dotfiles for Qtile - Linux Tiling Window Manager. Made to look like Hyprland with the gaming experience of Xorg.

# Needed packages (apart from qtile and Xorg):
 - picom (compositor)
 - nitrogen (wallpaper utility)
 - pacman-contrib (needed for checkupdates widget)
 - rofi (dmenu)
 - dunst (notifications)
 - kitty (terminal)
 - polkit-kde-agent (graphical authentication thingy - can be changed in autostart.sh)


**The config will only work with _Xorg_.**

# Some additional info
The bar itself is divided into segments:
LEFT: Calendar, CPU usage, RAM usage, Window name
MIDDLE: Workspaces
RIGHT: system tray, checkupdates widget (pacman-contrib has to be installed), sound, battery, clock

The sound widget opens the pavucontrol app on mouse left click. You can change the volume with mouse scroll and mute the sound with right click.

Terminal used is Kitty but can be changed to anything else thanks to qtile's guess_terminal().

Hope you like it as a base for your own rice. I'm definitely going to update this config since Xorg is the only option for nvidia laptop gaming now and qtile seems to be a really nice WM


# Themes used:
 - Catppuccin Mocha Lavender (GTK and QT/Kvantum)
 - Bibata Original Classic Cursor Theme
 - Tela Black Dark Icon theme
