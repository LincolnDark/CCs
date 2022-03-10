string = ["hi", "dee", "hi", "how", "are", "you", "mr", "dee"]
d={}
for i in range(len(string)-1):
    x=string[i]
    c=0
    for j in range(i,len(string)):
        if string[j]==string[i]:
            c=c+1
    count=dict({x:c})
    if x not in d.keys():
        d.update(count)
print (d)
# source https://www.tutorialsteacher.com/articles/how-to-count-occurences-of-list-items-in-python

#AD Code failed, error below
# Traceback (most recent call last):
#   File "C:/Data/Students_2022/Dark/Coding_Challenge_2/Occurence.py", line 9, in <module>
#     if x not in d.keys():
# NameError: name 'd' is not defined