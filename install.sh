#!/bin/bash
binaries=(pomodoro distract schedule tasks recreate_tasklist t/t.py)
code_dir=~/code/pomodoro

for file in ${binaries[@]}
do
    rm ~/bin/${file#*/} -f 
    ln -r -s $code_dir/$file ~/bin/
done
