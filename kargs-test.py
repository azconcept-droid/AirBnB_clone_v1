#!/usr/bin/python3
"""
Learn args and kwargs
"""

def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

my_fct()
my_fct("Best")
my_fct("Best", 89)
my_fct(name="Best")
my_fct(name="Best", number=89)
my_fct("School", 12, name="Best", number=89)

a_dict = {'name': "Best", 'age': 89}

print('---')

my_fct(a_dict)
my_fct(*a_dict)
my_fct(**a_dict)

# def greet_me(**kwargs):
#     if kwargs is not None:
#         for key, value in kwargs.iteritems():
#             print("{} == {}".format(key,value))

# greet_me(name="azeez")