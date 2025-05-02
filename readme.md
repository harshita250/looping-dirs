# 📁 File Organizer for Events and Enrollments

This project automates the organization of images into a structured format within `events` and `enrollments` directories, based on edge and class-based grouping. Configuration is done through a simple JSON file. It is useful for preparing data for machine learning or distributed systems.

---

## 📌 Purpose

To take an unstructured collection of folders/files and organize them into a clean folder hierarchy:
- `events/`: Images placed in folders mimicking original structure
- `enrollments/`: Images evenly distributed across all edges and class folders

An optional intermediate output folder is used during processing, which is cleaned up after execution.

---

## 🧾 Input JSON Format

The script takes a configuration JSON file with the following structure:

```json
{
  "input_path": "path/to/source",
  "dir_name": "data",
  "sub_dir_name": ["events", "enrollments"],
  "class_names": ["class1", "class2", "class3", "class4", "class5"],
  "output_path": "intermediate_output",
  "discard_folder_name": "discard_this", 
  "delay": 2
}
````

### 💡 Explanation of Fields

| Key                   | Description                                                                  |
| --------------------- | ---------------------------------------------------------------------------- |
| `input_path`          | Directory containing the unorganized files or folders                        |
| `dir_name`            | Name of final output folder (default: `data`)                                |
| `sub_dir_name`        | Subfolders to be created under `data` (must include `events`, `enrollments`) |
| `class_names`         | List of classes to be created under each edge folder                         |
| `output_path`         | Temporary directory used for intermediate steps                              |
| `discard_folder_name` | Folder to exclude from processing. Set to `null` to keep all                 |
| `delay`               | Delay (in seconds) before the process starts                                 |

---

## 📂 Output Folder Structure

```
data/
├── events/
│   ├── edge_1/
│   │   ├── class_1/
│   │   │   └── images...
│   │   └── ...
│   └── ...
├── enrollments/
│   ├── edge_1/
│   │   ├── class_1/
│   │   │   └── images...
│   │   └── ...
│   └── ...
```

* **Events**: Preserves structure of original image folders
* **Enrollments**: Distributes images equally across edges and classes

---

## 🧠 Internal Variables

* `tree`: Dictionary mapping relative paths to associated files
* `number_of_files`: Count of total files processed

---

## ⚠️ Notes & Assumptions

* The folder to be discarded **must be named explicitly** in `discard_folder_name`, or set to `null`.
* Intermediate folder (specified by `output_path`) is automatically deleted after the process ends.
* Equal distribution of files in `enrollments` is performed programmatically.
* JSON input must contain **all** required keys.

---

## 🚀 How to Run

1. Create a configuration file (e.g., `config.json`) using the template above.
2. Run the script:

```bash
python organizer.py config.json
```

3. Wait for the specified delay (e.g., 2 seconds), and your `data` folder will be created with the specified structure.

---

## 🧹 Cleanup

* Temporary intermediate folder (`output_path`) will be deleted automatically after successful execution.

---

## 🛠️ Dependencies

No external libraries are required outside the standard Python library.

Built using:

* Python 3.x
* `os`
* `shutil`
* `time`
* `json`

