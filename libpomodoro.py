import argparse
import subprocess

class StoreBoth(argparse.Action):
   """
   Stores both the option and the value to the destination.
   """
   def __call__(self, parser, namespace, values, option_string=None):
       setattr(namespace, self.dest, [option_string] + values)

class AppendBoth(argparse.Action):
   """
   Append both the option and the value to the destination.
   If the destination is not a list, initialize it to an empty one first.
   """
   def __call__(self, parser, namespace, values, option_string=None):
       if type(getattr(namespace, self.dest)) != list:
           setattr(namespace, self.dest, [])
           getattr(namespace, self.dest).append("{} {}".format(option_string, str(values)))

def t(task_directory, task_file, *options):
    arguments = ['t', '--task-dir', task_directory, '--list', task_file]
    arguments.extend(options)
    output = subprocess.check_output(arguments).decode('ascii')
    return output

