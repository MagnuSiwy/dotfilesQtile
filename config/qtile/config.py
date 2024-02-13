import os
import subprocess

from libqtile import layout, hook
from libqtile.config import Match, Screen

from bars import widget_defaults, mainBar, secondBar
from colors import colors
from keybinds import *



#----------------------------------------------------------------------------
# Hooks and other functions
#----------------------------------------------------------------------------

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])



#----------------------------------------------------------------------------
# Layout settings
#----------------------------------------------------------------------------
    
layoutTheme = {
    "border_focus": colors[-2], 
    "border_normal": colors[0], 
    "border_width": 2, 
    "margin": 3
}


layouts = [
    layout.Columns(**layoutTheme),
]


floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="lutris"),
        Match(wm_class="gnome-disks"),
        Match(wm_class="prismlauncher"),
        Match(wm_class="telegram-desktop"),
        Match(wm_class="discord"),
        Match(wm_class="epicgameslauncher.exe"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="caprine"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="amazon games ui.exe"),
	Match(wm_class="steam"),
	Match(wm_class="whatsdesk"),
    ],
    **layoutTheme
)



#----------------------------------------------------------------------------
# Screens settings
#----------------------------------------------------------------------------

screens = [
    Screen(
        top=mainBar,
    ),
    Screen(
        #top=secondBar,
    ),
]



#----------------------------------------------------------------------------
# Miscelanous settings
#----------------------------------------------------------------------------

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False

# If something Java related is not working, set this to "LG3D"
wmname = "Qtile"


