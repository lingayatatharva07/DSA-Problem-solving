# mytuple = {"prashant","ashish","rahul","sandip","komal","ankush","Rajesh",23,3,15,77,"sandip"}
# # print(mytuple)
# # print(type(mytuple))

# mytuple[2]="sunil" #immutable
# print(mytuple)

# init_tuple =()
# print(init_tuple.__len__())

# init_tuple_a='a','b'
# init_tuple_b='a','b'
# print(init_tuple_a == init_tuple_b)

# init_tuple_a='1','2'
# init_tuple_b='3','4'
# print(init_tuple_a + init_tuple_b)

# l=[1,2,3]
# init_tuple = ('pyhton',)*(l.__len__() - l[::-1][0])
# print(init_tuple)

# init_tuple = ('pyhton',)*3
# print(type(init_tuple))

init_tuple = ((1,2),)*7
print(len(init_tuple[3:8]))