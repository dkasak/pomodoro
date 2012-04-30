import argparse
import subprocess

class StoreBoth(argparse.Action):
   """
   Stores both the option and the value to the destination.
   """
   def __call__(self, parser, namespace, values, option_string=None):
       setattr(namespace, self.dest, [option_string, values[0]])

def t(task_directory, task_file, *options):
    arguments = ['t', '--task-dir', task_directory, '--list', task_file]
    arguments.extend(options)
    output = subprocess.check_output(arguments).decode('ascii')
    return output
