"""Application Test Suite"""

import core, os

def setup_env():
  """Creates a directory with several files"""

  test_path = os.getcwd() + '/testEnv'

  try:
    # Create test dir
    os.mkdir(test_path)
    print('Created test environment at {}'.format(test_path))
  except FileExistsError:
    # Dir exists already
    pass

  curr_dir = os.getcwd()
  os.chdir(test_path)

  # Create files to be sorted
  contents = ['C.txt', 'A.txt', 'B.txt', '50.txt', '12.txt', 'aPles.txt', 'SPAM.txt']

  # Add files to created dir
  for item in contents:
    open(item, 'a').close()

  os.chdir(curr_dir)

  return test_path

if __name__ == '__main__':
  env_path = setup_env()
  core.alphabetize(env_path)
