list_number = [1,-1,-9,12,-5,32,-7]
min_number = list_number[0]
for index,item in enumerate(list_number):
     if min_number > item :
         min_number = item
         min_index = index

print(min_number)
print(min_index)