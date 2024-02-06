# import json
# class A:
#     def __init__(self):
#         self.a = "aa"
#         self.b = "bb"

#     def __str__(self):
#         return str(self.__dict__)

#     def __repr__(self):
#         return self.__str__()

# class B:
#     def __init__(self):
#         self.c = "aa"
#         self.d = A()
#     def __str__(self):
#         return str(self.__dict__)

#     def __repr__(self):
#         return self.__str__()

# class MyClass:
#     def __init__(self, key1, key2, key3):
#         self.key1 = key1
#         self.key2 = key2
#         self.key3 = key3
#         self.key4 = B()

#     def __str__(self):
#         return str(self.__dict__)

#     def __repr__(self):
#         # return json.dumps(self.__str__())
#         return self.__str__()

# # Example usage
# my_instance = MyClass(key1="value1", key2="value2", key3="value3")
# print(my_instance)


import json
 
# Creating a dictionary
Dictionary ={1:'Welcome', 2:'to',
            3:'Geeks', 4:{"A":"aa"},
            5:'Geeks'}
  
# Converts input dictionary into
# string and stores it in json_string
json_string = json.dumps(Dictionary)
print(json_string)