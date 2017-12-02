import numpy as np
import matplotlib.pyplot as plt

# reading the expression file
file = open("leukemia.txt", "r")
content = file.readlines()
file.close()

patients = [] # patients category (ALL or AML)
genes = [] # name of the genes (headers)
expr = [] # table with expression levels
patients = content[0].split()[1:]
for line in content[1:] :
    genes.append(line.split()[0])
    expr.append([int(value) for value in line.split()[1:]])

print("Expression levels of", len(genes), "genes for",len(patients), "patients")
data = np.matrix(expr)

# reading the patwhays file
file = open("pathways.txt", "r")
content = file.readlines()
file.close()

MIN_SIZE = 15
pathways = [] # name of the pathways
genes_sets = [] # name of the genes implicated in each pathway
# NOTE : we keep only the genes sets with at least MIN_SIZE (15) genes for which we have expression data
for line in content :
    genes_implicated = [g for g in line.split()[1:] if g in genes]
    if len(genes_implicated) >= MIN_SIZE :
        pathways.append(line.split()[0])
        genes_sets.append(genes_implicated)

print(len(pathways),"sets of genes used of the analysis")