from types import DynamicClassAttribute

def my_func(*thing, other_thing="lol"):
    x = 2
    return x

code_type = my_func.__code__

print("co_argcount: ",code_type.co_argcount)
print("co_cellvars: ",code_type.co_cellvars)
print("co_code: ",code_type.co_code)
print("co_consts: ",code_type.co_consts)
print("co_filename: ",code_type.co_filename)
print("co_firstlineno: ",code_type.co_firstlineno)
print("co_flags: ",code_type.co_flags)
print("co_freevars: ",code_type.co_freevars)
print("co_kwonlyargcount: ",code_type.co_kwonlyargcount)
print("co_lnotab: ",code_type.co_lnotab)
print("co_name: ",code_type.co_name)
print("co_names: ",code_type.co_names)
print("co_nlocals: ",code_type.co_nlocals)
print("co_posonlyargcount: ",code_type.co_posonlyargcount)
print("co_stacksize: ",code_type.co_stacksize)
print("co_varnames: ",code_type.co_varnames)

print(code_type.__dir__())

for att in code_type.__dir__():
    print(att+": ", getattr(code_type, att),": ", type(getattr(code_type, att)))

dict()._get_mixins_()