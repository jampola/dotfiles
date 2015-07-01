#!/bin/sh
#xrandr --newmode "1368x768_60.00"   85.25  1368 1440 1576 1784  768 771 781 798 -hsync +vsync
xrandr --newmode "1280x1024_60.00"  109.00  1280 1368 1496 1712  1024 1027 1034 1063 -hsync +vsyn

#xrandr --addmode VGA1 1368x768_60.00
xrandr --addmode VGA1 1280x1024_60.00
#xrandr --output HDMI2 --mode 1920x1080 --pos 1368x0 --rotate normal --output HDMI1 --mode 1920x1080 --pos 3288x0 --rotate normal --output VGA1 --mode 1368x768_60.00 --pos 0x0 --rotate normal
xrandr --output HDMI2 --mode 1920x1080 --pos 1368x0 --rotate normal --output HDMI1 --mode 1920x1080 --pos 3288x0 --rotate normal --output VGA1 --mode 1280x1024_60.00 --pos 0x0 --rotate normal
