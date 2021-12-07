from helpers import *
benign_count = 0
malignant_count = 0
patient_count = 0
class node:
    def __init__(self, function=None, left=None, right=None, cancer_type=None, f_id=None):
        self.function = function
        self.left = left
        self.right = right
        self.cancer_type = cancer_type
        self.f_id = f_id


def determine_cancer_type(node, patient_data):
    if node is None: return 0
    #print("node f_id " + str(node.f_id))
    #print(" patient data " + str(patient_data[node.f_id]))
    if node.function is None:
        if node.cancer_type == "B":
            global benign_count
            benign_count += 1
            return 2
        if node.cancer_type == "M":
            global malignant_count
            malignant_count += 1
            return 4
    return determine_cancer_type(node.function(node,int(patient_data[node.f_id])), patient_data)
#Build tree
malignant_node = node(None, None, None, "M", -1)
benign_node = node(None, None, None, "B", -1)
ucs2_node = node(ucs2, None, None, None, 2)
ucs3_node = node(ucs3, None, None, None, 2)
ucs4_node = node(ucs4, None, None, None, 2)
bn2_node = node(bn2, None, None, None, 6)
bn3_node = node(bn3, None, None, None, 6)
ct3_node = node(ct3, None, None, None, 1)
ct5_node = node(ct5, None, None, None, 1)
ct6_node = node(ct6, None, None, None, 1)
bc2_node = node(bc2, None, None, None, 7)
ma3_node = node(ma3, None, None, None, 4)
ma3_node_2 = node(ma3, None, None, None, 4)
ma5_node = node(ma5, None, None, None, 4)
ucshape2_node = node(ucshape2, None, None, None, 3)

# left of root
ucs2_node.left = bn3_node
bn3_node.left = benign_node
bn3_node.right = ct3_node
ct3_node.left = benign_node
ct3_node.right = bc2_node
bc2_node.left = ma3_node
ma3_node.left = malignant_node
ma3_node.right = benign_node
bc2_node.right = malignant_node

# right of root
ucs2_node.right = ucshape2_node
ucshape2_node.left = ct5_node
ct5_node.left = benign_node
ct5_node.right = malignant_node
ucshape2_node.right = ucs4_node
ucs4_node.left = bn2_node
bn2_node.left = ma3_node_2
ma3_node_2.left = benign_node
ma3_node_2.right = malignant_node
bn2_node.right = ct6_node
ct6_node.left = ucs3_node
ucs3_node.left = malignant_node
ucs3_node.right = ma5_node
ma5_node.left = benign_node
ma5_node.right = malignant_node
ct6_node.right = malignant_node
ucs4_node.right = malignant_node

# root
root = ucs2_node

# Opening file 
f = open('patient_data.csv', 'r') # Specify which file to read from here
patient_list = []

# Reading from file, and populate our patient_list
for line in f: 
    lst = line.rstrip().split(",")
    patient_list.append(lst)
f.close()

# Determine if they have the cancer b0ss
for patient in patient_list:
    node = root
    patient[-1] = determine_cancer_type(node, patient)

# Write results to file
# Write output to readme.txt
f = open('cancer_results.csv', 'w')

# First instructions
for patient in patient_list:
    patient_count += 1
    f.write(str(patient) + '\n')
f.write("Patient count: " + str(patient_count))
f.write(" Benign count: " + str(benign_count))
f.write(" Malignant count: " + str(malignant_count))
f.close()
    




