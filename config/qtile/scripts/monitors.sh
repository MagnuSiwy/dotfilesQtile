#!/bin/bash

if [ $(xrandr | grep "connected" | wc -l) -ge 2 ]
then
    xrandr --output HDMI-1-0 --mode 1920x1080 --rate 60.00 --right-of eDP-1
fi
