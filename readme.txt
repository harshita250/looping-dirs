# 📁 File Organizer for Events and Enrollments

This project organizes a directory of images into a structured output format with `events` and `enrollments` subdirectories. It supports class-wise and edge-wise grouping and is configurable through a JSON input file.

---

## 📌 Purpose

To automate the organization of image data from a source directory into a `data` folder with separate `events` and `enrollments` folders, structured by edges and classes, with optional support for discarding specific folders.

---

## 🧾 Input JSON Format

The script takes a JSON input file with the following structure:

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
