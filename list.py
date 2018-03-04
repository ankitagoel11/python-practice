a = [1,2,3,45,4,3,4,2]
new_list =[]
checker = int(input("please enter a number "))
for i in a:
    if i < checker:
        new_list.append(i)
print (new_list)
