"""System utility function for sorting directory alphabetically"""

import os

def alphabetize(dir=None):
  """Alphabetically sorts path"""

  path = ''

  if not dir:
    path = os.getcwd()
  else:
    path = dir
    os.chdir(path)

  # Call system sort on current directory
  os.system('ls {} | sort -V'.format(path))

  print('Alphabetized {}'.format(path))
