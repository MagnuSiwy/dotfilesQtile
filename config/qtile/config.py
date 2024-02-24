import os
import subprocess

from libqtile import layout, hook
from libqtile.config import Match, Screen
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText

from bars import widget_defaults, mainBar#, secondBar
from colors import colors
from keybinds import *



#----------------------------------------------------------------------------
# Hooks and other functions
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


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
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
        Match(wm_class="gnome-disks"),
        Match(title="calcurse"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="nm-connection-editor"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="amazon games ui.exe"),
        Match(wm_class="steam"),
        Match(wm_class="lutris"),
        Match(wm_class="epicgameslauncher.exe"),
        Match(wm_class="prismlauncher"),
        Match(wm_class="telegram-desktop"),
        Match(wm_class="whatsdesk"),
        Match(wm_class="caprine"),
        Match(wm_class="discord"),
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