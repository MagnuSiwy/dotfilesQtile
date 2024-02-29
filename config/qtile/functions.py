import os
import subprocess

from libqtile import hook
from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText

from colors import colors



#----------------------------------------------------------------------------
# Functions
#----------------------------------------------------------------------------

def powerMenu(qtile):
    controls = [
        PopupImage(
            filename="~/.config/qtile/images/terminal.svg",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight_border = -10,
            highlight_radius = 10,
            highlight = colors[1],
            mouse_callbacks={
                "Button1": lazy.shutdown()
            }
        ),
        PopupImage(
            filename="~/.config/qtile/images/reboot.svg",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight_border = -10,
            highlight_radius = 10,
            highlight = colors[1],
            mouse_callbacks={
                "Button1": lazy.spawn("reboot")
            }
        ),
        PopupImage(
            filename="~/.config/qtile/images/shutdown.svg",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight_border = -10,
            highlight_radius = 10,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("shutdown now")
            }
        ),
        PopupText(
            font = "Roboto",
            text="Quit Qtile",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            font = "Roboto",
            text="Reboot",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            font = "Roboto",
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        border_width = 2,
        border = colors[1],
        background=colors[0] + "95",
        initial_focus=1,
        hide_on_mouse_leave = True,
    )

    layout.show(centered=True)



#----------------------------------------------------------------------------
# Hooks
#----------------------------------------------------------------------------

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.run([script])


@hook.subscribe.screen_change
def screen_change(event):
    script = os.path.expanduser("~/.config/qtile/scripts/monitors.sh")
    subprocess.run([script])

@hook.subscribe.client_new
def center_floating_win(window):
    wm_name = window.cmd_inspect()["name"]
    if wm_name == "Calendar" or wm_name == "Available updates":
        window.toggle_floating()
        window.cmd_set_size_floating(1000, 600)