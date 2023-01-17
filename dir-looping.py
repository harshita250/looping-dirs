import os, random
import shutil

path = r'C:\Users\harsh\anaconda3\envs\face-recognition\dataset\images'
tree = {}
dest_root = os.getcwd()


def loop_through_dirs(path):
    for relative_path, list_of_folders, list_of_files in os.walk(path, topdown=False):
        count = 0
        random_files = []

        while count < 4:
            count = count + 1
            if len(list_of_files) != 0:
                random_file = (random.choices(
                    [file for file in os.listdir(relative_path) if os.path.isfile(os.path.join(relative_path, file))]))
                if random_file[0][-4:] == '.jpg':
                    # random_file = os.path.join(str(relative_path), str(random_file)[2:-2])
                    random_files.append(random_file)

        # name = os.path.basename(relative_path)
        # print(name, ":", random_files)
        tree[relative_path] = random_files

    # print(tree)


def create_folder():
    i = 0
    for key, value in tree.items():
        try:
            root_dirname = 'folder' + str(i)
            i = int(i) + 1
            os.mkdir(root_dirname)
            count = 0
            for file in value:
                # print(file,':',count)

                try:
                    sub_dir_path = os.path.join(dest_root, root_dirname)

                    sub_folder_name_1 = sub_dir_path + '/' + 'events'
                    sub_folder_name_2 = sub_dir_path + '/' + 'enrollments'

                    os.mkdir(sub_folder_name_1)
                    os.mkdir(sub_folder_name_2)

                except FileExistsError:
                    pass

                src_path = os.path.join(str(key), str(file)[2:-2])
                # print(sub_folder_name_1)

                if count < 3:
                    # print('entered if')
                    shutil.copy(src_path, sub_folder_name_2)

                elif count == 3:
                    # print('entered else')
                    shutil.copy(src_path, sub_folder_name_2)
                count = count + 1

        except FileExistsError:
            print(root_dirname, "already exists")
        # print(key,':',value)

    # print(tree)

if __name__ == "__main__":
    loop_through_dirs(path)
    create_folder()