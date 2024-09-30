def my_function(*args):
    for arg in args:
        print(arg)


my_function(1, 2, 3, "hello")


def my_function2(**args):
    for key, value in args.items():
        print(key, value)


my_function2(a=1, b=2, c=3, message="hello")


def modify_immutable(arg):
    arg += 1


value = 10
modify_immutable(value)
print(value)  # Output: 10


def modify_mutable(arg):
    arg.append(4)


my_list = [1, 2, 3]
modify_mutable(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

# x = object()
# >>> sys.getrefcount(x)
# 2
# >>> y = x
# >>> sys.getrefcount(x)
# 3
# >>> del y
# >>> sys.getrefcount(x)
# 2
