import os
import subprocess

from libqtile import hook
from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText, PopupSlider

from colors import colors


#----------------------------------------------------------------------------
# Defaults and constants
#----------------------------------------------------------------------------

# Change the SCREEN_NAME to your monitor's name

SCREEN_NAME = "eDP-1"


imageDefaults = {
    "mask": True,
    "colour": colors[1],
    "highlight_radius": 10,
    "highlight_border": -10,
}


textDefaults = {
    "font": "Roboto",
    "fontsize": 14,
    "h_align": "center",
    "foreground": colors[1],
}


layoutDefaults = {
    "border_width": 2,
    "border": colors[1],
    "background": colors[0],
    "hide_on_mouse_leave": True,
}



#----------------------------------------------------------------------------
# Functions
#----------------------------------------------------------------------------

def powerMenu(qtile):
    controls = [
        PopupImage(
            filename = "~/.config/qtile/images/terminal.svg",
            pos_x = 0.15,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {
                "Button1": lazy.shutdown()
            },
        ),
        PopupImage(
            filename = "~/.config/qtile/images/reboot.svg",
            pos_x = 0.45,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {
                "Button1": lazy.spawn("reboot")
            }
        ),
        PopupImage(
            filename = "~/.config/qtile/images/shutdown.svg",
            pos_x = 0.75,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = "A00000",
            mouse_callbacks = {
                "Button1": lazy.spawn("shutdown now")
            }
        ),
        PopupText(
            text = "Quit Qtile",
            pos_x = 0.1,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
        PopupText(
            text = "Reboot",
            pos_x = 0.4,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
        PopupText(
            text = "Shutdown",
            pos_x = 0.7,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width = 1000,
        height = 200,
        controls = controls,
        initial_focus = 1,
        opacity = 0.8,
        **layoutDefaults,
    )

    layout.show(centered=True)


def brightnessControl(qtile):
    controls = [
        PopupText(
            text = "Brightness:",
            pos_x = 0.07,
            pos_y = 0.25,
            width = 0.33,
            height = 0.5,
            can_focus = False,
            **textDefaults,
        ),
        PopupImage(
            filename = "~/.config/qtile/images/circle-regular.svg",
            pos_x = 0.47,
            pos_y = 0.25,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {"Button1": lazy.spawn("xrandr --output " + SCREEN_NAME + " --brightness 0.5")},
        ),
        PopupImage(
            filename = "~/.config/qtile/images/circle-half.svg",
            pos_x = 0.65,
            pos_y = 0.25,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {"Button1": lazy.spawn("xrandr --output " + SCREEN_NAME + " --brightness 0.75")},
        ),
        PopupImage(
            filename = "~/.config/qtile/images/circle-solid.svg",
            pos_x = 0.85,
            pos_y = 0.25,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {"Button1": lazy.spawn("xrandr --output " + SCREEN_NAME + " --brightness 1.0")},
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width = 230,
        height = 40,
        controls = controls,
        initial_focus = None,
        opacity = 0.85,
        **layoutDefaults,
    )

    layout.show(x = -25, y = 13, relative_to = 3, relative_to_bar = True)



#----------------------------------------------------------------------------
# Hooks
#----------------------------------------------------------------------------

@hook.subscribe.client_new
def center_floating_win(window):
    wm_name = window.cmd_inspect()["name"]
    if wm_name == "Calendar" or wm_name == "Available updates":
        window.toggle_floating()
        window.cmd_set_size_floating(1000, 600)
    if wm_name == "Telegram":
        window.cmd_set_size_floating(470, 620)


@hook.subscribe.screen_change
def screen_change(event):
    monitorScript = os.path.expanduser("~/.config/qtile/scripts/monitors.sh")
    subprocess.run([monitorScript])


@hook.subscribe.startup_once
def autostart():
    autostartScript = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    monitorScript = os.path.expanduser("~/.config/qtile/scripts/monitors.sh")
    subprocess.run([autostartScript])
    subprocess.run([monitorScript])