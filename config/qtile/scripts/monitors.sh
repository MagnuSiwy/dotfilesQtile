#!/bin/bash

primaryMonitor=$(xrandr | grep "connected" | head -n 1 | cut -d " " -f 1)
secondMonitor=$(xrandr | grep "connected" | tail -n 1 | cut -d " " -f 1)

if [ $(xrandr | grep " connected" | wc -l) -ge 2 ]
then
    xrandr --output "${secondMonitor}" --mode 1920x1080 --rate 60.00 --right-of "${primaryMonitor}"
else
    xrandr --output "${secondMonitor}" --off
fi
