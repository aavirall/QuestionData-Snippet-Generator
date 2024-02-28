import re
from Questions import q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30

questions = [q1.rep,q2.rep,q3.rep,q4.rep,q5.rep,q6.rep,q7.rep,q8.rep,q9.rep,q10.rep,q11.rep,q12.rep,q13.rep,q14.rep,q15.rep,q16.rep,q17.rep,q18.rep,q19.rep,q20.rep,q21.rep,q22.rep,q23.rep,q24.rep,q25.rep,q26.rep,q27.rep,q28.rep,q29.rep,q30.rep]
# questions = [q3.rep]
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
    for ele in questions:
        templ = re.sub("INDEX", str(i), templ)
        if i != len(questions):
            templ = re.sub("QUESTION", str(ele)+",\n\t\t"+'"INDEX":QUESTION', templ)
        else:
            templ = re.sub("QUESTION", str(ele), templ)
        i+=1
    
    with open("out.txt", "w") as f:
        f.write(templ)

