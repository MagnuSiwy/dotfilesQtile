from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from colors import colors
from keybinds import defaultApps



#----------------------------------------------------------------------------
# Defaults and recurring settings
#----------------------------------------------------------------------------

widget_defaults = dict(
    font = "Roboto",
    fontsize = 12,
    padding = 10,
    background = colors[3],
    foreground = colors[0],
)

widgetDecorations = {
    "background": colors[0],
    "foreground": colors[1],
    "decorations": [
        RectDecoration(use_widget_background = True, radius = 12, filled = True, group = True),
    ],
}

barConfig = {
    "size":         24,
    "margin":       [4, 6, 2, 6],
    "border_width": [0, 0, 0, 0],
    "border_color": [colors[3], colors[3], colors[3], colors[3]],
    "background": colors[3]
}



#----------------------------------------------------------------------------
# Main bar template
#----------------------------------------------------------------------------

barWidgets = [
    widget.Clock(
        format = "   %d.%m.%Y",
	    mouse_callbacks={"Button1": lazy.spawn(defaultApps["terminal"] + " " + defaultApps["calendar"])},
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.CPU(
        format = '    {load_percent}%',
        update_interval = 5.0,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.Memory(
        format = '    {MemPercent}%',
        update_interval = 5.0,
        **widgetDecorations
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.CheckUpdates(
        distro = 'Arch_checkupdates',
        display_format = '!    {updates}',
        no_update_string = '    Updated',
        update_interval = 30,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.WindowName(
        format = "{name}",
    ),
    widget.Spacer(
        length = bar.STRETCH,
    ),
    widget.GroupBox(
        spacing = 6,
        padding_x = 5,
        margin_x = 10,
        fontsize = 14,
        borderwidth = 0,
        inactive = colors[1],
        active = colors[1],
        this_current_screen_border = '#6C7086',
        highlight_method = 'block',
        rounded = True,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = bar.STRETCH,
    ),
    widget.Systray(
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.Volume(
        emoji = True,
        emoji_list = ['', '', '', ''],
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["sound"])},
        **widgetDecorations,
    ),
    widget.Spacer(
        length = -6,
        padding = 0,
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["sound"])},
        **widgetDecorations
    ),
    widget.Volume(
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["sound"])},
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.Bluetooth(
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["bluetooth"])},
        default_text = "   {num_connected_devices} {connected_devices}",
        default_show_battery = True,
        opacity = 0.85,
        highlight_radius = 8,
        menu_background = colors[0],
        menu_border = colors[1],
        menu_border_width = 2,
        menu_foreground = colors[1],
        menu_foreground_highlighted = colors[0],
        menu_font = "Roboto",
        menu_offset_y = 10,
        **widgetDecorations  
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.WiFiIcon(
        mouse_callbacks={"Button1": lazy.spawn(defaultApps["wifi"])},
        active_colour = colors[1],
        show_ssid = True,
        interface = "wlp4s0",
        padding_y = 7,
        update_interval = 5,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.Battery(
        charge_char = '',
        full_char = '',
        not_charging_char = '',
        discharge_char = '',
        unknown_char = '',
        format = "{char}    {percent: 2.0%}",
        max_chars = 0,
        **widgetDecorations,
    ),
    widget.Spacer(
        length = 15,
    ),
    widget.Clock(
        format = "   %H:%M",
        **widgetDecorations,
    ),
]



#----------------------------------------------------------------------------
# Declaration of bars
#
# System tray widget can be used only once
# It has to be deleted from the second bar
#----------------------------------------------------------------------------

mainBar = bar.Bar(barWidgets, **barConfig)
# secondBar = bar.Bar(barWidgets, **barConfig)