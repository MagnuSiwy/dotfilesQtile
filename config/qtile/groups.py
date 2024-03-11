from libqtile.config import Group, Match



#----------------------------------------------------------------------------
# Groups
#----------------------------------------------------------------------------

groups = [
    Group("1",matches = [Match(wm_class = "code"), Match(wm_class = "lutris"), Match(wm_class = "steam"), Match(wm_class = "leagueclientux.exe")]),
    Group("2", matches = [Match(wm_class = "firefox"), Match(wm_class = "telegram-desktop"), Match(wm_class = "discord"), Match(wm_class = "whatsdesk")]),
    Group("3", matches = [Match(wm_class = "spotify")]),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
    Group("0"),
]