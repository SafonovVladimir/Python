import os
import zipfile

# name = os.listdir(path='folder')
# print(name)

folder_path = 'C:\\Users\\restg\\PycharmProjects\\pythonProject\\folder'
zip_path = 'C:\\Users\\restg\\PycharmProjects\\pythonProject\\folder\\test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

# my_zip.write(f'{folder_path}\\1.txt', arcname='new.txt', compress_type=zipfile.ZIP_DEFLATED)

for folder, subfolder, files in os.walk(folder_path):
    # print(folder, files)
    for file in files:
        if file == zip_name:
            continue
        my_zip.write(os.path.join(folder, file),
        os.path.relpath(os.path.join(folder, file), folder_path),
        compress_type=zipfile.ZIP_DEFLATED)


    # with zipfile('lesson48.zip', 'w') as myzip:
    #     myzip.write('files')


my_zip.close()