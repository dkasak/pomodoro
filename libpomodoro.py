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

def t(task_directory, task_file, *options, verbose=False):
    arguments = ['t', '--task-dir', task_directory, '--list', task_file]
    arguments.extend(options)
    if verbose:
        arguments.append('--verbose')
    output = subprocess.check_output(arguments).decode('ascii')
    return output

def get_task_text(task_directory, task_file, id):
    output = t(task_directory, task_file)
    for line in output.split("\n"):
        tid, _, text = line.partition('-')
        tid = tid.strip()
        if id == tid:
            return text.strip()
    return None

def get_full_id(task_directory, task_file, id):
    output = t(task_directory, task_file, verbose=True)
    print(output)
    for line in output.split("\n"):
        full_id, _, text = line.partition('-')
        full_id = full_id.strip()
        if full_id.startswith(id):
            return full_id
    return None

def find_task_by_text(task_directory, task_file, text):
    output = t(task_directory, task_file)
    for line in output.split("\n"):
        id, _, desc = line.partition('-')
        if desc == text:
            return id
    return None
