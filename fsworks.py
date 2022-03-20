import  os


def create_folder():
    #Enter dir
    path_parent_folder = input('Enter the path for creating folder: ')
    # os.chdir(path_parent_folder)

    # Enter the Dir name
    folder_name = input('Enter the Folder name: ')

    #Path
    path = os.path.join(path_parent_folder, folder_name)

    # newpath = fr'{path_parent_folder}"\{folder_name}"'
    if not os.path.exists(path):
        os.makedir(path)
    print(f'Folder {folder_name} is created in PATH {path_parent_folder}')
    return path



def create_file():
    return path


def show_foder_tree():
    folder_tree = os.listdir(input('Enter the path for watching folder tree: '))
    return folder_tree






