#!/bin/bash

# Change this to the position of your monitor in xrandr
# eg. In my xrandr output it's:
# eDP-1 <some-other-info>
# HDMI-1-0 <some-other-info>
# My second monitor is on the 2nd position, so that's what I put here
whichIsSecond=2

primaryMonitor=$(xrandr | grep "connected" | head -n 1 | cut -d " " -f 1)
secondMonitor=$(xrandr | grep "connected" | head -n ${whichIsSecond} | tail -n 1 | cut -d " " -f 1)

if [ $(xrandr | grep " connected" | wc -l) -ge 2 ]
then
    xrandr --output "${secondMonitor}" --mode 1920x1080 --right-of "${primaryMonitor}"
else
    xrandr --output "${secondMonitor}" --off
fi
