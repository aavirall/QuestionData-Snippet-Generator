import re,q1,q2,q3,q4,q5,q6,q7,q8,q15,q16

from Question import *

arr = [q1.rep, q2.rep, q3.rep, q4.rep, q5.rep, q6.rep, q7.rep, q8.rep, q15.rep, q16.rep]


#-----------------------------------------------------------------------------------#
templ = """
{
    "request_list": {
        "INDEX":QUESTION
    }
}
"""
if __name__ == "__main__":
    i = 1
    for ele in arr:
        templ = re.sub("INDEX", str(i), templ)
        if i != len(arr)-1:
            templ = re.sub("QUESTION", str(ele)+",\n\t\t"+'"INDEX":QUESTION', templ)
        else:
            templ = re.sub("QUESTION", str(ele), templ)
        i+=1
    
    with open("out.txt", "w") as f:
        f.write(templ)

