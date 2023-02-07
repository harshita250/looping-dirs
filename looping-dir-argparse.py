import os, random
import shutil
import argparse

parser = argparse.ArgumentParser(description='Code to loop through directories and files of n level')

parser.add_argument("--data_root", help="Path to dataset", required=True)
parser.add_argument("--dest_path", help="Path to Destination Folder")
args = parser.parse_args()

# print(args.data_root)

path = args.data_root
tree = {}
dest_root = args.dest_path
if dest_root is None:
    dest_root = os.getcwd()
number_of_files = 4


def loop_through_dirs(path):
    for relative_path, list_of_folders, list_of_files in os.walk(path, topdown=False):
        count = 0
        random_files = []

        while count < number_of_files:
            count = count + 1

            if len(list_of_files) != 0:  # checks if the folder has files
                random_file = (random.choices(
                    [file for file in os.listdir(relative_path) if os.path.isfile(os.path.join(relative_path, file))]))
                if random_file[0][-4:] == '.png':
                    # random_file = os.path.join(str(relative_path), str(random_file)[2:-2])
                    random_files.append(random_file)

        # name = os.path.basename(relative_path)
        # print(name, ":", random_files)
        if len(random_files) != 0:
            tree[relative_path] = random_files

    # print(tree)


def create_folder():
    i = 0

    for key, value in tree.items():

        try:

            root_dirname = dest_root + '/' + 'folder' + str(i)
            os.mkdir(root_dirname)
            count = 0  # keeps a track of number of files

            for file in value:
                # print(file,':',count)

                try:
                    # sub_dir_path = os.path.join(dest_root, root_dirname)
                    # #if you want to save the files in current working directory then use the commented code and change dest_path

                    # sub_folder_name_1 = sub_dir_path + '/' + 'events'
                    # sub_folder_name_2 = sub_dir_path + '/' + 'enrollments'

                    sub_folder_name_1 = root_dirname + '/' + 'events'
                    sub_folder_name_2 = root_dirname + '/' + 'enrollments'

                    os.mkdir(sub_folder_name_1)
                    os.mkdir(sub_folder_name_2)

                except FileExistsError:
                    pass

                src_path = os.path.join(str(key), str(file)[2:-2])
                # print(sub_folder_name_1)

                if count < number_of_files - 1:
                    # print('entered if')
                    shutil.copy(src_path, sub_folder_name_1)
                    new_name = sub_folder_name_1 + '/' + 'folder' + str(i) + '_events_' + str(count) + '.png'
                    old_name = sub_folder_name_1 + '/' + str(file)[2:-2]
                    os.rename(old_name, new_name)

                elif count == number_of_files - 1:
                    # print('entered else')
                    shutil.copy(src_path, sub_folder_name_2)
                    new_name = sub_folder_name_2 + '/' + 'folder' + str(i) + '_enrollments_' + str(
                        number_of_files - count - 1) + '.png'
                    old_name = sub_folder_name_2 + '/' + str(file)[2:-2]
                    os.rename(old_name, new_name)

                count = int(count) + 1

            i = int(i) + 1

        except FileExistsError:
            print(root_dirname, "already exists")
        # print(key,':',value)

    # print(tree)


if __name__ == "__main__":
    loop_through_dirs(path)
    create_folder()
    # print(tree)
