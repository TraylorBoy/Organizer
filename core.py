"""System utility functions for manipulating directory and file organization"""

import os, shutil

def get_contents(dir=None):
  """Returns the contents of the directory to be sorted alphabetically"""
  path = ''

  if not dir:
    path = input('Path to directory to be sorted: ')
  else:
    path = dir

  return [x for x in os.listdir(path) if not x.startswith('.') and not x.startswith('__')]

def alphabetize(dir=None):
  """Alphabetically sorts path"""

  sorted_path = dir + '/sorted'
  contents = sorted(get_contents(dir))

  try:
    # Make new dir
    os.mkdir(sorted_path)
  except FileExistsError:
    # Dir already exists
    pass

  os.chdir(dir)

  for item in contents:
    # Copy items to new directory
    if item != 'sorted':
      shutil.copy2(item, sorted_path)

  # Call system sort on new directory
  os.system('ls sorted | sort -V')

  print('Alphabetized {} in dir {}'.format(dir, sorted_path))
