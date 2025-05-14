#simple args function
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

#simple kwargs function
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

#Syntax to order arguments
# 1. Formal arguments 2. *args 3. Keyword arguments 4. **kwargs
# def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):

print_values(
    name_1="Alex",
    name_2="Gray",
    name_3="Harper",
    name_4="Phoenix",
    name_5="Remy",
    name_6="Val"
)

multiply(3, 2)
multiply(5, 4, 3)
multiply(7, 7, 10, 9)