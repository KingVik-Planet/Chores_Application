FILEPATH = "chores_list.py"
def get_chores(filepath: object = FILEPATH) -> object:
  """
  Read a the file and print list of Chores
  Reading includes:
  1. show to show/view the list of the chores existing in the chore list
  """
  with open(filepath, 'r') as file_local:
    chores_local = file_local.readlines()
  return chores_local


def write_chores(chores_arg, filepath=FILEPATH):
  """
  Write to a the file and print list of Chores,
  Writing includes:
  1. add edit to Edit the chores list
  2. completed to Remove Chore from list
  3. exit to end thee process
  """
  """
  Link
  """
  with open(filepath, 'w') as file:
    file.writelines(chores_arg)
