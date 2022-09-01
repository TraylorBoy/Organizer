"""Application Test Suite"""

import core, os

def setup_env():
  """Creates a directory with several files"""

  test_path = os.getcwd() + '/testEnv'
  print(test_path)

  try:
    # Create test dir
    os.mkdir(test_path)
  except FileExistsError:
    # Dir exists already
    pass

  curr_dir = os.getcwd()
  os.chdir(test_path)

  # Create files to be sorted
  contents = ['C.txt', 'A.txt', 'B.txt']

  # Add files to created dir
  for item in contents:
    open(item, 'a').close()

  os.chdir(curr_dir)

  return test_path

def check_contents(path):
  print(core.get_contents(path))

if __name__ == '__main__':
  env_path = setup_env()
  check_contents(env_path)
  core.alphabetize(env_path)
