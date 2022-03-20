import os


def create_dir():
    # Enter dir
    path_parent_folder = input('Enter the path for creating folder: ')
    # os.chdir(path_parent_folder)

    # Enter the Dir name
    folder_name = input('Enter the Folder name: ')

    # Path
    path = os.path.join(path_parent_folder, folder_name)

    # newpath = fr'{path_parent_folder}"\{folder_name}"'
    if not os.path.exists(path):
        os.makedirs(path)
    print(f'Folder {folder_name} is created in PATH {path_parent_folder}')
    # return path


def create_file():
    # Enter the Path
    path_parent_folder = input('Enter the path for creating folder: ')

    # Enter File Name
    filename = input('Enter the File name: ')

    # Create file with name == file_name
    file = open(os.path.join(path_parent_folder, filename), 'x')

    print(f'File with name {filename} is created in PATH {path_parent_folder}')
    # return filename


def show_foder_tree():
    #Вводим стартовый путь
    startpath = input('Enter the path for showing folder tree: ')
    for root, dirs, files in os.walk(startpath):
        #считаем количество директорий и файлов
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
