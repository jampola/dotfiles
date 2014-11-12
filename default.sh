#!/bin/sh
xrandr --output LVDS1 --off
xrandr --output HDMI1 --mode 1920x1080 --pos 1080x184 --rotate normal --output LVDS1 --off --output DP1 --off --output VGA1 --mode 1920x1080 --pos 0x0 --rotate right
