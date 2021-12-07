#Uniformity of Cell Size Functions
def ucs2(node, data):
    if data <= 2: return node.left
    return node.right
def ucs3(node, data):
    if data <= 3: return node.left
    return node.right
def ucs4(node, data):
    if data <= 4: return node.left
    return node.right
# END Uni.CSF
# Bare Nuclei Functions
def bn2(node, data):
    if data <= 2: return node.left
    return node.right
def bn3(node, data):
    if data <= 3: return node.left
    return node.right
# End BNF
# Clump Thickness Functions
def ct3(node, data):
    if data <= 3: return node.left
    return node.right
def ct5(node, data):
    if data <= 5: return node.left
    return node.right
def ct6(node, data):
    if data <= 6: return node.left
    return node.right
# End CT
# Bland Chromatin Functions
def bc2(node,data):
    if data <= 2: return node.left
    return node.right
# END BCF
# Marginal Adhesion Functions
def ma3(node,data):
    if data <= 3: return node.left
    return node.right
def ma5(node,data):
    if data <= 5: return node.left
    return node.right
# END MAF
# Uniformity of Cell Shape Functions
def ucshape2(node, data):
    if data <= 2: return node.left
    return node.right
# END Cell shape functions
