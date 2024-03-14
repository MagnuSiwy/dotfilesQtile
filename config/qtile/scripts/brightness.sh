#!/bin/bash

if [ "$#" -ne 1 ]
then
    echo "Invalid number of arguments"
    exit 1
fi

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
    xrandr --output "${primaryMonitor}" --brightness "$1"
    xrandr --output "${secondMonitor}" --brightness "$1"
else
    xrandr --output "${primaryMonitor}" --brightness "$1"
fi