#!/bin/bash
binaries=(schedule tasks recreate_tasklist)
cd ~/bin/
rm ${binaries[@]}
cd ~/code/pomodoro
ln -r -s ${binaries[@]} ~/bin/
