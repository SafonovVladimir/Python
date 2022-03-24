import fsworks
# import os

# os_path = os.getcwd()
# print(os_path)

case = input('Do you want to make a Directory or File, or building a DirTree?\n'
             '(please enter "D" for Folder, "F" for file, "T" for Tree)\n')
if case == 'D':
    fsworks.create_dir()
elif case == 'F':
    fsworks.create_file()
elif case == 'T':
    fsworks.show_foder_tree()
else:
    print('Thank you!')