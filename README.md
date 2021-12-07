# Cancer-Classification-BT

Simple python implementation that demonstrates basic file I/O and binary decision trees.

Program reads in a .csv file containing patient data, and by utilizing a binary tree, classifies patient tumour data in either being Benign or Malignant.

Cancer.py contains a node class which is used to construct a static binary tree, created also in cancer.py

Helpers.py contains functions for decisions to determine if the tree should be recursed on the left or right child (this decision is dependant on patient data passed to the helper function based on which type of tumour/cancer the specific node in the tree represents)

The program returns the patient data but with a count totalling both the number of patients with Malignant and Benign tumour types, as classified by the algorithm.
