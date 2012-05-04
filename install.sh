#!/bin/bash
binaries=(pomodoro schedule tasks recreate_tasklist t/t.py)
code_dir=~/code/pomodoro
ln -r -s --force $code_dir/${binaries[@]} ~/bin/
