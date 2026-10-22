# Client nedds Math Package

# from package_name.module_name import function_name

from mathpackage.add import msg,add_fun
print(msg)
print("Sum of two numbers: ", add_fun(10,20))

print("=" * 30)

from mathpackage import mul
print(mul.msg)
print("Product of two numbers: ", mul.mul_fun(10,20))