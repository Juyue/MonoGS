#!/bin/bash
sudo x11vnc -storepasswd 3284 /home/ubuntu/.x11vnc/passwd
sudo Xvfb :99 -screen 0 2560x1920x24 -ac +extension GLX +render +extension RANDR -noreset &
export DISPLAY=:99
sudo x11vnc -q -nopw -ncache 10 -forever -rfbauth /home/ubuntu/.x11vnc/passwd -display :99 -rfbport 5901 &
