from libqtile import bar, widget, qtile
from libqtile.lazy import lazy

from colors import colors
from keybinds import defaultApps



#----------------------------------------------------------------------------
# Defaults and recurring settings
#----------------------------------------------------------------------------

widget_defaults = dict(
    font="Roboto",
    fontsize=12,
    padding=5,
    background=colors[0],
    foreground=colors[1],
)

reversedColors = {
    "background": colors[3],
    "foreground": colors[0],
}

defaultRounding = {
    **reversedColors,
    "font": "Roboto Mono",
    "fontsize": 17,
    'padding': 0
}

leftRounding = {
    "text": "\ue0b6",
    **defaultRounding
}

rightRounding = {
    "text": "\ue0b4",
    **defaultRounding
}

barConfig = {
    "size":         24,
    "margin":       [4, 6, 2, 6],
    "border_width": [0, 0, 0, 0],
    "border_color": [colors[3], colors[3], colors[3], colors[3]],
    **reversedColors
}



#----------------------------------------------------------------------------
# Main bar template
#----------------------------------------------------------------------------

barWidgets = [
    widget.TextBox(
        **leftRounding
    ),
    widget.Clock(
        format = "   %d.%m.%Y",
	    mouse_callbacks={"Button1": lazy.spawn(defaultApps["terminal"] + " " + defaultApps["calendar"])}
    ),
    widget.TextBox(
        **rightRounding
    ),
    widget.Spacer(
        **reversedColors,
        length = 20
    ),
    widget.TextBox(
        **leftRounding
    ),
    widget.CPU(
        format = '   {load_percent}%',
        update_interval = 30.0
    ),
    widget.TextBox(
        **rightRounding
    ),
    widget.Spacer(
        **reversedColors,
        length = 20
    ),
    widget.TextBox(
        **leftRounding
    ),
    widget.Memory(
        format = '   {MemPercent}%',
        update_interval = 30.0
    ),
    widget.TextBox(
        **rightRounding
    ),
    widget.Spacer(
        **reversedColors,
        length = 20
    ),
    widget.WindowName(
        **reversedColors,
        format = "{name}",
    ),
    widget.Spacer(
        **reversedColors,
        length = bar.STRETCH
    ),
    widget.TextBox(
        **leftRounding
    ),
    widget.GroupBox(
        spacing = 6,
        fontsize = 14,
        margin = 3,
        borderwidth = 0,
        inactive = colors[1],
        active = colors[1],
        this_current_screen_border = '#6C7086',
        highlight_method = 'block',
        rounded = True,
    ),
    widget.TextBox(
        **rightRounding
    ),
    widget.Spacer(
        **reversedColors,
        length = bar.STRETCH
    ),
    widget.Systray(
        **reversedColors,
    ),
    widget.Spacer(
        **reversedColors,
        length = 20
    ),
    widget.TextBox(
        **leftRounding
    ),
    widget.CheckUpdates(
        distro = 'Arch_checkupdates',
        display_format = '!    {updates}',
        no_update_string = '',
        update_interval = 300,
    ),
    widget.TextBox(
        **rightRounding
    ),
    widget.Spacer(
        **reversedColors,
        length = 20
    ),
    widget.TextBox(
        **leftRounding
    ),
    widget.Volume(
        emoji = True,
        emoji_list = ['', '', '', ''],
        volume_app = defaultApps["sound"],
    ),
    widget.Volume(
        volume_app = defaultApps["sound"],
    ),
    widget.TextBox(
        **rightRounding
    ),
    widget.Spacer(
        **reversedColors,
        length = 20
    ),
    widget.TextBox(
        **leftRounding
    ),
    widget.Battery(
        charge_char = '',
        full_char = '',
        not_charging_char = '',
        discharge_char = '',
        unknown_char = '',
        format = "{char}     {percent: 2.0%}",
        max_chars = 0
    ),
    widget.TextBox(
        **rightRounding
    ),
    widget.Spacer(
        **reversedColors,
        length = 20
    ),
    widget.TextBox(
        **leftRounding
    ),
    widget.Clock(
        format = "   %H:%M",
    ),
    widget.TextBox(
        **rightRounding
    )
]



#----------------------------------------------------------------------------
# Declaration of bars
#
# System tray widget can be used only once
# It has to be deleted from the second bar
#----------------------------------------------------------------------------

mainBar = bar.Bar(barWidgets, **barConfig)
secondBar = bar.Bar(barWidgets[:18] + barWidgets[20:], **barConfig)