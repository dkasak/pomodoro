import sys
import os
from os import sep
from os.path import join
from os.path import expanduser as expand

script_dir = os.path.dirname(os.path.abspath(__file__))
t_dir = os.path.join(script_dir, "t")
sys.path.append(t_dir)

settings = {}
settings["SESSION_FILE"] = ".pomodoro_session"
settings["SESSION_DIR"] = expand("~/.pomodoro/")

settings["TASK_DIR"] = expand("~/.pomodoro/")
settings["INVENTORY_FILE"] = "tasks"
settings["SCHEDULE_FILE_PREFIX"] = "todo"
settings["CURRENT_TASK_FILE"] = "current"

try:
    with open(expand("~/.pomodororc"), "r") as f:
        user_settings = {}
        for line in f:
            # skip comments and empty lines
            if line.strip().startswith('#') or not line.strip():
                continue
            setting, value = line.split('=')
            setting = setting.strip()
            value = value.strip()
            # expand user directories in paths
            if "DIR" in setting:
                value = expand(value)
                # create directories that don't exist
                try:
                    os.makedirs(value)
                except OSError:
                    pass
            user_settings[setting] = value
            settings.update(user_settings)
except IOError:
    pass

SESSION_DIR = settings["SESSION_DIR"]
SESSION_FILE = settings["SESSION_FILE"]
TASK_DIR = settings["TASK_DIR"]
INVENTORY_FILE = settings["INVENTORY_FILE"]
SCHEDULE_FILE_PREFIX = settings["SCHEDULE_FILE_PREFIX"]
CURRENT_TASK_FILE = settings["CURRENT_TASK_FILE"]
