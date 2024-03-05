#Let's go learn about variables.

#The object of the left hand is known as identifying sign, the symbol of the half is called 
#allocation symbol due to it allocates to the memory space, identified
#with the name of the variable, the value that is in the right hand.

x = 200

print(x + 2)

#There are four types of variables: string, integer, float and boolean. 
#They are known as primary data. For instand:

name = 'Estiben' #String(str)
age = 20 #integer (int)
height = 1.99 #Float 
is_student = True #Boolean (bool)

#We can make operations with string type variables. For example:
# 1) Linking string variables.
last_name = 'Gonzalez'
whole_name = name + ' ' + last_name
print(whole_name)

# 2) Multiplying string variables.
print(5 * name)

#Let's try a function

def sum(a, b):
    """ This function is adding up two numbers"""
    return a + b

print(sum(2,2))

def multiply(a, b):
    """ This function is multiplying two numbers"""
    return a * b

print(multiply(3,2))

#Now, we are going to practice with lists: a list is an object that contains
#different types of variables and is organized in an specific order; its order starts in 0.

list_1 = [1, 'value', True, height]

print(list_1[3])

#To know the length of a list we can use the function len(). For example:

print(len(list_1))

#To add a new variable or object in a list we use the function .append(). For instand:

list_1.append(name)
print(list_1)

#There is a similar object to the lists: the tuple. The difference
#with regard to the list is that the tuple cannot be modified. 
#The tuples are useful to keep information that will not change since
#they will not spend so much memory. Let's see an example:

tuple_1 = (height, age, True, whole_name)

for value in tuple_1:
    print(value)

#Now, we have the sets: they don't have any repeated objects, they are not ordered.
    
set_1 = {1, 2, name, height, last_name, name}
print(set_1)    

#Exercise: Given a list, in which there are some repeated objects, creates
#a new list without repeated objects. (hint: use the function list and set)

def delete_repeated_objects_from_a_list(list_in):
    return list(set(list_in))

list_exercise = [1,1,1,1,1,2,2,2,2,3,4,4,5,5,5,5]
print(delete_repeated_objects_from_a_list(list_exercise))

#Diccionaries: they have the same syntax from sets, but follow a specific
#layout given by key:valuy where the key is the 

dict_1 = {
    'name': name,
    'last_name': last_name,
    'occupation': 'Student'
}
for key in dict_1.keys():
    print(key)


for key, value in dict_1.items():
    print(key+':',value)

