#  this is a list 
list = [94, 90, 80, 100, 70, 50, 87]

# adding something to a list 
list.append(30)
print (list)
# to print each element 
for element in list: 
    print(element)

# calculate grade 
lengthOfList = len(list)
grade = sum(list)/lengthOfList
# print (grade)
# practice conditional 
if grade >= 90: 
    print('A')
elif grade >=80: 
    print('B')
elif grade >=70: 
    print('C')
elif grade >=60: 
    print('D')
else: 
    print('F')
