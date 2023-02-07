import os, random
import shutil
import json
import time

from natsort import os_sorted

with open('input.json') as f:
    input = json.load(f)

tree = {}
number_of_files = 4

path = input['input_path']
dest_root = input['output_path']

sub_dir_name_1 = input['sub_dir_name'][0]
sub_dir_name_2 = input['sub_dir_name'][1]

folder = input['dir_name']
dest_root = input['output_path']
del_file = input['discard_folder_name']
classes = input['class_names']
delay = int(input['delay'])


def does_folder_exist(file_path):
    try:
        os.mkdir(file_path)
    except FileExistsError:
        pass


def loop_through_dirs(path):
    for relative_path, list_of_folders, list_of_files in os.walk(path, topdown=False):
        count = 0
        random_files = []

        while count < number_of_files:
            count = count + 1

            if len(list_of_files) != 0:  # checks if the folder has files
                random_file = (random.choices(
                    [file for file in os.listdir(relative_path) if os.path.isfile(os.path.join(relative_path, file))]))
                if random_file[0][-4:] == '.png' or random_file[0][-4:] == '.jpg' and del_file not in relative_path:
                    random_files.append(random_file)

        if len(random_files) != 0:
            tree[relative_path] = random_files


def create_folder():
    i = 0

    for key, value in tree.items():

        try:

            root_dirname = dest_root + '/' + folder + str(i)
            i = int(i) + 1
            os.mkdir(root_dirname)
            count = 0  # keeps a track of number of files

            for file in value:

                try:

                    sub_folder_name_1 = root_dirname + '/' + sub_dir_name_1
                    sub_folder_name_2 = root_dirname + '/' + sub_dir_name_2

                    os.mkdir(sub_folder_name_1)
                    os.mkdir(sub_folder_name_2)

                except FileExistsError:
                    pass

                src_path = os.path.join(str(key), str(file)[2:-2])

                if count < number_of_files - 1:
                    shutil.copy(src_path, sub_folder_name_1)
                    new_name = sub_folder_name_1 + '/' + folder + str(i - 1) + '_' + sub_dir_name_2 + '_' + str(
                        count) + '.png'
                    old_name = sub_folder_name_1 + '/' + str(file)[2:-2]
                    os.rename(old_name, new_name)

                elif count == number_of_files - 1:
                    shutil.copy(src_path, sub_folder_name_2)
                    new_name = sub_folder_name_2 + '/' + folder + str(i - 1) + '_' + sub_dir_name_1 + '_' + str(
                        count) + '.png'
                    old_name = sub_folder_name_2 + '/' + str(file)[2:-2]
                    os.rename(old_name, new_name)

                count = int(count) + 1
                time.sleep(delay)

        except FileExistsError:
            print(root_dirname, "already exists")


def mov_files(root_old, root_new):
    for file in os_sorted(os.listdir(root_old)):
        old_path = root_old + '/' + file
        new_path = root_new + '/' + file
        shutil.move(old_path, new_path)
    time.sleep(delay)


def create_subfolders(root):
    total = len(os.listdir(root))
    no_files_per_edge = int(total / 4)
    no_files_per_edge_class = int(no_files_per_edge / 5)

    for i in range(0, 4):
        edge_path = root + '/edge_' + str(i)
        does_folder_exist(edge_path)

        ab = edge_path + '/ab'
        so = edge_path + '/so'
        pt = edge_path + '/pt'
        fraud = edge_path + '/fraud'
        vip = edge_path + '/vip'

        does_folder_exist(so)
        does_folder_exist(ab)
        does_folder_exist(pt)
        does_folder_exist(fraud)
        does_folder_exist(vip)

        for class_name in classes:
            class_path = edge_path + '/' + class_name
            for j in range(0, no_files_per_edge_class):
                old_path = root + '/' + os.listdir(root)[i + 1]
                new_path = class_path + '/' + os.listdir(root)[i + 1]
                # print(old_path, new_path)
                shutil.move(old_path, new_path)

        time.sleep(delay)

    while len(os.listdir(root)) > 4:
        for class_name in classes:
            class_path = edge_path + '/' + class_name
            if len(os.listdir(root)) > 4:
                old_path = root + '/' + os.listdir(root)[4]
                new_path = class_path + '/' + os.listdir(root)[4]
                shutil.move(old_path, new_path)


def create_events_enrollment(path, dest_path):
    for folder in os_sorted(os.listdir(path)):
        events = os.getcwd() + '/' + dest_path + '/events/' + folder
        does_folder_exist(events)

        root_new = events
        root_old = os.path.join(path, folder, 'events')
        mov_files(root_old, root_new)

        root_new = os.getcwd() + '/' + dest_path + '/enrollments'
        root_old = os.path.join(path, folder, 'enrollments')
        mov_files(root_old, root_new)

    create_subfolders(os.path.join(dest_path, 'events'))
    create_subfolders(os.path.join(dest_path, 'enrollments'))


if __name__ == "__main__":
    does_folder_exist(dest_root)

    loop_through_dirs(path)  # loops through directories and innermost directories
    create_folder()  # creates folders for every directory encountered

    dest_path = 'data'

    does_folder_exist(dest_path)
    does_folder_exist(
        os.path.join(dest_path, 'events'))  # creates events folder at dest path, to move intermediate output
    does_folder_exist(
        os.path.join(dest_path, 'enrollments'))  # creates enrollments folder at dest path, to move intermediate output

    create_events_enrollment(dest_root, dest_path)
    shutil.rmtree(dest_root)
