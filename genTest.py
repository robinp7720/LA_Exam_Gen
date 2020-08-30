import numpy as np
import os, subprocess


"""task setup"""
#Determinant task
mat_a1 = np.random.random_integers(-4,4,(6,3))#Based on old exams: factors between -4 and +4, 3x3 matrices, polynomials of deg. 1: generate 2*3=6 factors per row
mat_a1=mat_a1.flatten()
for i in range(len(mat_a1)):#Based on old exams: chance of a factor being zero is relatively high:
    if np.random.randint(0,5) <2:#but less than 50%
        mat_a1[i]=0
    #TODO: maybe make zeros in main diagonal less likely so the tasks doesnt get too easy
mat_a1 = mat_a1.astype(str)#final matrix for factors for polynomial

#Characteristic polynomial task
mat_a2 = np.random.random_integers(-40,40,(4,4))#Based on old exams: Numbers between -40, 40
mat_a2=mat_a2.flatten()
for i in range(len(mat_a2)):
    if np.random.randint(0,7) <=2:
        mat_a2[i]=0


mat_a2 = mat_a2.astype(str)



#numbers to put into laTex document tasks everytime "LA" is written in there
nums=list()
nums.extend(mat_a1)
nums.extend(mat_a2)


#numbers to put into laTex document solutions everytime "LA" is written in template.txt
sols=list()
sols.extend(mat_a1)
sols.extend(mat_a2)

#solutions are the last numbers to be embedded in the laTex document
nums.extend(sols)
print(nums)
"""LaTex generation"""

filename = "LA_Det_test.tex"



def replace_LA(ar):#replace "LA" in the template with the next number in nums
    #"LA" is starting symbol of contextfree grammar-inspired insertion mechanism for random numbers: it is replaced with nums[i]
    res_strs=list()
    cntr = 0
    for e in ar:
        for subs in range(e.count("LA")):
            print(subs, " num")
            e = e.replace("LA", str(nums[cntr]),1)
            cntr +=1
            print(e, "next LA replaced")
        res_strs.append(e)

    return res_strs


def w(ar):#write .tex document
    with open(filename, 'w') as f:
        ar = replace_LA(ar)
        for e in ar:
            #polynomial formatting. Related to polynomials being specified as LAa+LA in template.txt
            #example 0: "LAa+LA" -> "0a+-3" -> "-3"
            #example 1: "LAa+LA" -> "2a+0" -> "2a"

            e=e.replace("0a+0","0")
            e=e.replace("0a+","")
            e=e.replace("+0","")
            e=e.replace("+-","-")
            
            #write to .tex
            f.write(e)

            

template=open("./template.txt", "r") #open laTex template
print(template)
ar = replace_LA(template)
w(ar)

process = subprocess.Popen("pdflatex "+filename, stdout=subprocess.PIPE, shell=True) #turn .tex into pdf
errorc = process.communicate()[0].decode('ascii')

#subprocess.Popen("cp LA_Det_test.pdf path/backup.pdf", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True) 
#print("\n\n\ncopying completed")



