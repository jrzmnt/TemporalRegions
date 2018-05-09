# Codes

This folder contains the codes used to process our datasets in order to generate temporal regions.
The description of each code is listed as follows:

#### temporal_feature_selection.py 

**Input**: 

* file_path: Path to the file containing a frame per row.
Each row consists of a path to the frame, the class value, and a sequence of features, all separated by a space.

* window_size: Number of regions.

* type_opt: Type of unification, either 'concat' or 'mean'.

* output_path: Path to the destination file. Can be None.

**Output**:

* A file containing a frame by row.
Each row consists of a path to the frame, the class value, and a sequence of features either concatenated or the mean values.