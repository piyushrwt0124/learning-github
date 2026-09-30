list = x = [0,1,2,4,'piyush', 5,24,2008]
print(list[1:4]) 
list[4]= 'kanha'
print(list)
print(x)
x.append('rawat')
print(x)
list = y = [24.555,344,343.455,445,3343.32, 4664,3223.54,42.23]
(y.sort())
print(y)
print(x.index('kanha'))
print(x.insert(4,'aayush'))
print(x)
list= fav_movie =['BLACK PANTHER', 'JUMANJI', 'CHAKRACHAL', 'GANGS OF WASEPUR', 'OBBSISION']
print(fav_movie)

list= problm = [1,2,3,2,1]
problm.reverse()
print(problm)
problm.copy()
print("yes") if problm[0:5] == problm[-5:-1] else print("no")

copy_of_list = problm.copy()
copy_of_list.reverse()

print('yes it is palindrome') if problm == copy_of_list else print('no it is not palindrome')


my_list = [1,'abc','abc',1]
copy_list1 = my_list.copy()
copy_list1.reverse()
print('yes it is palindrome') if my_list == copy_list1 else print('no it is not palindrome')

stud_grade = ['A','B','A','C','B','A','C','B']
print(type(stud_grade))

print(stud_grade.count('A'))
print(stud_grade.sort())

print(stud_grade)

stud_grade.append('F')
print(stud_grade)