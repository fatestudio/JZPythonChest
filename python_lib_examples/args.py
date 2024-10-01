def my_function(*args):
    for arg in args:
        print(arg)


def my_function2(**args):
    for key, value in args.items():
        print(key, value)


def modify_immutable(arg):
    arg += 1


def modify_mutable(arg):
    arg.append(4)


if __name__ == '__main__':

    my_function(1, 2, 3, "hello")

    my_function2(a=1, b=2, c=3, message="hello")

    value = 10
    modify_immutable(value)
    print(value)  # Output: 10

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
