#!/bin/bash
binaries=(schedule tasks)
cd ~/bin/
rm ${binaries[@]}
cd ~/code/pomodoro
ln -r -s ${binaries[@]} ~/bin/
