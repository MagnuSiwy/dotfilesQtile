from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from functions import powerMenu
from groups import groups



#----------------------------------------------------------------------------
# Default apps and the mod key
#----------------------------------------------------------------------------

mod = "mod4"
defaultApps = {
    "terminal": guess_terminal(),
    "browser": "firefox",
    "fileMan": "ranger",
    "calendar": "calcurse",
    "sound": "pavucontrol",
    "network": "nm-connection-editor",
    "bluetooth": "blueman-manager",
}



#----------------------------------------------------------------------------
# Keybinds for window management and opening apps 
#----------------------------------------------------------------------------
    
keys = [
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "k", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "v", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "s", lazy.window.move_down(), desc="Bring the window down"),
    Key([mod], "w", lazy.window.move_up(), desc="Bring the window up"),
    Key([mod], "q", lazy.window.move_to_top(), desc="Bring the window to the top"),
    Key([mod], "a", lazy.window.move_to_bottom(), desc="Bring the window to the bottom"),

    Key([mod], "Return", lazy.spawn(defaultApps["terminal"]), desc="Launch the terminal"),
    Key([mod], "f", lazy.spawn(defaultApps["browser"]), desc="Launch the browser"),
    Key([mod], "e", lazy.spawn(defaultApps["terminal"] + " " + defaultApps["fileMan"]), desc="Launch the file manager"),
    Key([mod, "shift"], "Print", lazy.spawn("flameshot gui"), desc="Choose the part of the screen for a screenshot"),
    Key([mod], "Print", lazy.spawn("flameshot screen"), desc="Screenshot of the entire screen"),
    Key([mod, "control"], "Print", lazy.spawn("flameshot full"), desc="Screenshot of all of the monitors"),

    Key([mod], "comma", lazy.prev_screen(), desc="Change focus to the previous screen"),
    Key([mod], "period", lazy.next_screen(), desc="Change focus to the next screen"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.function(powerMenu), desc="Show Power Menu"),
    Key([mod], "r", lazy.spawn('rofi -show drun -theme ~/.config/rofi/config.rasi'), desc="Launch rofi menu"),
]



#----------------------------------------------------------------------------
# Keybinds for groups
#----------------------------------------------------------------------------

for i in groups:  
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod, "control"], i.name, lazy.window.togroup(i.name), desc="Move focused window to group {}".format(i.name)),
    ])



#----------------------------------------------------------------------------
# Drag floating layouts
#----------------------------------------------------------------------------

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]