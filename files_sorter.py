import os
import shutil

def files_sorter(output_dir_path, destination_dir='dist'):
    try:
        isExist = os.path.exists(output_dir_path)
        if isExist:
            os.mkdir(destination_dir)
            for filename in os.listdir(output_dir_path):
                if os.path.isfile(f'{output_dir_path}/{filename}'):
                    ext = os.path.splitext(filename)[-1][1:]
                    if not os.path.exists(f'{destination_dir}/{ext}'):
                        os.mkdir(f'{destination_dir}/{ext}')
                    shutil.copy(f'{output_dir_path}/{filename}', f'{destination_dir}/{ext}')
                elif os.path.isdir(filename):
                    files_sorter(filename, destination_dir)
        else:
            print('Output directory does not exists')
    except FileExistsError:
        print('Can not copy to the directory, please, change the name.')
    except OSError:
        print("Could not open/read file")
    except IOError:
        print("Could not open/read file:")

files_sorter('folder1', 'folder2')