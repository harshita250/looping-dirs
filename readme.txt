# 📁 File Organizer for Events and Enrollments

This project organizes a directory of images into a structured output format with `Events` and `Enrollments` subdirectories. It supports class-wise and edge-wise grouping and is configurable through a JSON input file.

---

## 📌 Purpose

To automate the organization of image data from a source directory into a `data` folder with separate `events` and `enrollments` folders, structured by edges and classes, with optional support for discarding specific folders.

---

## 🧾 Input JSON Format

The script takes a JSON input file with the following structure:

json
{
  "input_path": "path/to/source",
  "dir_name": "data",
  "sub_dir_name": ["events", "enrollments"],
  "class_names": ["class1", "class2", "class3", "class4", "class5"],
  "output_path": "intermediate_output",
  "discard_folder_name": "discard_this" or null,
  "delay": 2
}


### 💡 Explanation of Fields

* **`input_path`**: Directory containing files and/or folders to be organized.
* **`dir_name`**: Name of the final output directory (`data`).
* **`sub_dir_name`**: Must include `"events"` and `"enrollments"`.
* **`class_names`**: List of class folder names (typically 5).
* **`output_path`**: Temporary directory for intermediate operations.
* **`discard_folder_name`**: Name of folder to exclude. Use `null` if nothing to discard.
* **`delay`**: Delay in seconds before execution starts.

---

## 📂 Output Folder Structure


data/
├── events/
│   ├── edge_1/
│   │   └── class_1/
│   │       └── images...
│   └── ...
├── enrollments/
│   ├── edge_1/
│   │   ├── class_1/
│   │   └── class_2/
│   └── ...
```

* **Events**: Files are grouped in folders and subfolders as per source folder structure.
* **Enrollments**: Images are evenly distributed across all edges and classes.

---

## 📦 Variables in Code

* `tree`: Dictionary mapping folder paths to their image files.
* `number_of_files`: Count of files being processed.

---

## ⚠️ Notes & Assumptions

* Files cannot be discarded unless the exact folder name is provided in `discard_folder_name`.
* Intermediate `output_path` is removed upon successful execution.
* Images in `enrollments` are equally distributed.
* Requires all expected keys to be present in the JSON config file.

---

## 🚀 How to Run

1. Create the input JSON configuration file.
2. Run the script:

   bash
   python organizer.py config.json
   
3. After completion, check the `data` folder for the output structure.

---

## 🧹 Cleanup

The intermediate output directory defined in `output_path` will be automatically deleted after the operation.

---

## 🛠️ Dependencies

* Python 3.x
* `os`, `shutil`, `time`, `json`

---
