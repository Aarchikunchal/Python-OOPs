# lst=[1,2,3]
# my_str="Hello"
# my_init=155
# # print(type(lst))
# # lst.clear()
# print(lst)


# #modular coding
from oops_proj import chatbook
user1=chatbook()
print(user1.id)

#using static method directly by class rather thn obj
chatbook.set_id(10)

user2=chatbook()
print(user2.id)

user3=chatbook()
print(user3.id)





# user1=chatbook()
# print(user1.id)


# user2=chatbook()
# print(user2.id)

# user3=chatbook()
# print(user3.id)






#GETTER AND SETTER
print(user1.get_name())
user1.set_name("aarchi")
print(user1.get_name())

# ENCAPSULATION
# print(user1._chatbook__name) #python do not provid high security to method or attribute
# print(user1.__name) 




# #func vs method 
# lst=[1,2,3]
# #funct
# a1=len(lst)
# print(a1)

# #this is how we call a method
# user1=chatbook()
# user1.sent_message()

