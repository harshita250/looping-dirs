Input is taken from a json file with fields:
1. input_path: Path to input directory (Can contain folders or files)
2. dir_name: Name of the folders to be created
3. sub_dir_name: Events and Enrollments
4. class_names: Name of classes
5. output_path: Name of intermediate output folder to be created
6. discard_folder_name: Name of the folder to be discarded. It should be set to none, if no file is to be discarded.
7. delay: Delay in seconds


Output: Folder named data, consists of events and enrollments sub-folders. Each of these sub-folders consist of 4 edges, followed by 5 classes. Events consists of folders 
which then consists of images, where as enrollments consists of images which is distributed equally amongst all edges and classes

Variables:

1. tree : A dictionary that stores the relative path and files associated with it.
2. number_of_files : Number of files to be moved to enrollments and events

Note:

1. Files can't be discarded if the name of the file isn't known.
2. Intermediate output, is deleted once the code is executed completely.