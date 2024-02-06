xrandr &
xrdb -merge ~/.Xresources &
/usr/lib/polkit-kde-authentication-agent-1 &

if [ $(systemctl list-unit-files --state=enabled | grep bluetooth | wc -l) ] 
then
	blueman-applet &
fi

exec qtile start
