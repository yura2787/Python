given_name = 'Yurii Trufn'
given_name = given_name.title()
analize_data = given_name.split()
students = ['Vasyl' 'Anna', 'Alex']

pencils = ['grey', 'black']
crayons = ['red', 'blue', 'black', 'black']
print(id(crayons))
pencil_red = crayons[0]
pencil_red_2 = crayons[-4]


crayons.sort(reverse=True)


my_list = [9, 10, 6, 12]
my_list.append(7)

my_list.insert(2, 11)
my_list[3] = 8



# add element
crayons.append('orange')
print(id(crayons))


# merge 2 lists
# crayons.append(pencils)
crayons.extend(pencils)


# remove element
crayons.remove('black')
print(id(crayons))

crayons.pop()
crayons.pop(0)

# sort list

# what_is_list = ['Yurii', 'Trufn', 55, [556], True, False, 3.96]
print(students)

pass