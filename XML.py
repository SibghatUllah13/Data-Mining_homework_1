

#1.
#Without Using Xml Tree, Just Focus that the Number of '=' would tell us in a Line how many attribute it has
# Or in Other Words, Counting the Number of  '=' would give us the Score
number_of_lines=int(input())
counter=0
for i in range(number_of_lines):
    line=list(input())
    for term in line:
        if term=="=":
            counter=counter+1
print(counter)
