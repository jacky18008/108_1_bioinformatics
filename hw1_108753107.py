# pandas for reading the txt file 
import pandas as pd

# numpy for the matrix multiplication
import numpy as np 

# reset print options to avoid scientific notation.
# np.set_printoptions(suppress=True)

# I use the simplest way to read such txt file,
# however, the table uses different number of space as a seperate unit,
# so I use regex(regular expression) to represent those space. 
data = pd.read_csv("pam1.txt", header=1, sep="\s+") 


# After loading it, we convert it from a dataframe to a numpy array,
# which is a useful data structure on scientific computing. 
pam_1 = data.values 

# PAMx = multiplied PAM1 by itself 
# round for 四捨五入
def pam_n(pam_1, n):
    pam_n = np.zeros(shape=pam_1.shape)
    l = np.arange(len(pam_1))           
    pam_n[l, l] = 1
    for i in range(n-1):
        print(pam_n)
        pam_n = np.dot(pam_n, pam_1)
    return pam_n
    
pam_250 = pam_n(pam_1, 250)

#pam_250 = np.round(np.log(pam_1**250))

#print("column shape: ", np.expand_dims(data.columns, axis=0).shape)
#print("pam_250 shape: ", pam_250.shape)
#pam_data = np.concatenate([np.expand_dims(data.columns, axis=0), pam_250], axis=0)

np.savetxt("pam250.txt", pam_250, delimiter=" ")
 

