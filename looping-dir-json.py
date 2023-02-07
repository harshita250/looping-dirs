import os, random
import shutil
import json
import time

with open('input.json') as file:
    input = json.load(file)

path = input['input_path']
dest_root = input['output_path']
folder = input['dir_name']
del_file = input['discard_folder_name']
delay = int(input['delay'])
n = 4
tree_files = {}
tree_folders = {}


def does_file_exist(file_path):
    try:
        os.mkdir(file_path)
    except FileExistsError:
        pass


def loop_through_dirs(path, file):
    for relative_path, list_of_folders, list_of_files in os.walk(path, topdown=False):
        files = []
        print(relative_path)

        tree_folders[relative_path] = list_of_folders

        index = (relative_path.split('\\')[-2]).find('@')
        # print(index)
        if index != -1:
            file = relative_path.split('\\')[-2][index + 1:]

        if file != relative_path.split('\\')[-1] and len(list_of_files) != 0:
            for f in list_of_files:
                if f[-4:] == '.png':
                    files.append(f)
            tree_files[relative_path] = files
        time.sleep(delay)

    #print(tree_files)


def test(index, files, old_path, dest_path, no_of_files_edge_class):
    # no_of_files_edge_class = index + no_of_files_edge_class
    # print(index, ':', no_of_files_edge_class)

    for index in range(index, no_of_files_edge_class):
        # print(index)
        src_path = old_path + '/' + files[index]
        new_path = dest_path + '/' + files[index]
        shutil.copy(src_path, new_path)

    # return index


def create_subfolders(sub_folder_name, name):
    ab = sub_folder_name + '/' + name + '/' + 'ab'
    so = sub_folder_name + '/' + name + '/' + 'so'
    pt = sub_folder_name + '/' + name + '/' + 'pt'
    fraud = sub_folder_name + '/' + name + '/' + 'fraud'
    vip = sub_folder_name + '/' + name + '/' + 'vip'

    does_file_exist(os.path.join(sub_folder_name, name))

    does_file_exist(ab)
    does_file_exist(so)
    does_file_exist(pt)
    does_file_exist(fraud)
    does_file_exist(vip)


def create_folders_events():
    i = -1
    index = 0
    for key, value in tree_files.items():
        i = int(i) + 1

        root_dirname = dest_root + '/' + folder + str(i)
        does_file_exist(root_dirname)

        no_of_files = len(value)
        no_of_files_edge = int(no_of_files / 4)
        no_of_files_edge_class = int(no_of_files_edge / 5)
        # print(no_of_files,':', no_of_files_edge, no_of_files_edge_class)

        sub_folder_name_1 = root_dirname + '/' + input['sub_dir_name'][0]
        sub_folder_name_2 = root_dirname + '/' + input['sub_dir_name'][1]

        does_file_exist(sub_folder_name_1)
        does_file_exist(sub_folder_name_2)

        x = 0
        for j in range(0, n):
            x = j + 1

            name = 'edge_' + str(x)

            create_subfolders(sub_folder_name_1, name)
            create_subfolders(sub_folder_name_2, name)

            # print(root_dirname)

            if j == 0:
                index = 0
                stop = no_of_files_edge
                # print('Iteration 0:', index, stop)

            elif j == 1:
                index = stop
                stop = no_of_files_edge * 2
                # print('Iteration 1:', index, stop)

            elif j == 2:
                index = stop
                stop = no_of_files_edge * 3
                # print('Iteration 2:', index, stop)

            else:
                index = stop
                stop = no_of_files_edge * 4
                # print('Iteration 3:', index, stop)

            ab = sub_folder_name_1 + '/' + name + '/' + 'ab'
            so = sub_folder_name_1 + '/' + name + '/' + 'so'
            pt = sub_folder_name_1 + '/' + name + '/' + 'pt'
            fraud = sub_folder_name_1 + '/' + name + '/' + 'fraud'
            vip = sub_folder_name_1 + '/' + name + '/' + 'vip'

            stop = no_of_files_edge_class * ((5 * j) + 1)
            test(index, value, str(key), ab, stop)
            index = stop
            stop = stop * 2

            stop = no_of_files_edge_class * ((5 * j) + 2)
            test(index, value, str(key), so, stop)
            index = stop
            stop = stop * 3

            stop = no_of_files_edge_class * ((5 * j) + 3)
            test(index, value, str(key), pt, stop)
            index = stop
            stop = stop * 4

            stop = no_of_files_edge_class * ((5 * j) + 4)
            test(index, value, str(key), fraud, stop)
            index = stop
            stop = stop * 5

            stop = no_of_files_edge_class * ((5 * j) + 5)
            test(index, value, str(key), vip, stop)

        time.sleep(delay)


if __name__ == "__main__":
    does_file_exist(dest_root)
    loop_through_dirs(path, file)
    create_folders_events()
    print(tree_files)
    print(tree_folders)
    # rename folder - then add that name in discard folder in json
