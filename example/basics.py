

def list_basics():
    # basic list in Python
    l = []
    for i in range(10):
        l.append(i)
    print(f'l:{l}')
    l = sorted(l, reverse=True)
    print(f'l:{l}')
    l.sort()
    print(f'l:{l}')

    l.pop()
    print(f'l:{l}')

    l.extend([11, 12])
    print(f'l:{l}')

    # Questions
    # is l.remove('abc') O(n) ?
    # is l.pop(0) O(1) ?
    # is list double sided list?

    res = zip([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
    for i in res:
        print(f'i:{i}')

    for i in enumerate(['a', 'b', 'c', 'd', 'e']):
        print(f'i:{i}')


def dict_basics():
    d = {}
    for i in range(10):
        d[i] = str(i)

    for k, v in d.items():
        print(f'k:{k}, v:{v}')
    d[8] = '80'
    print(f'd[8]:{d[8]}')
    d.pop(9)
    print(d)
    print(d.keys())
    print(d.values())


def calculators():  # Q: what is the precise name?
    a0 = 123 & 456
    a1 = 123 | 456
    a2 = 123 ^ 456
    a3 = 123 ** 456
    a4 = 123 % 456
    a5 = 123 / 456
    a6 = 123 // 456
    a = [a0, a1, a2, a3, a4, a5, a6]
    print(f'a:{a}')


def str_basics():
    s = 'abc'
    s += 'def'
    print(f's:{s}')
    print('a' in s)
    print('ab' in s)
    s2 = ".".join(['a', 'b', 'c'])
    print(f's2:{s2}')

    s3 = 'this is an apple.'
    print(s3.split(' '))
    print(s3.startswith('t'))
    s4 = s3.replace('th', 'ht')
    print(f's4:{s4}')
    print(s4.capitalize())
    print(s4.lower())
    print(s4.count('s'))
    print(s4.upper())
    print(s4.isalpha())
    print(s4.isspace())
    print(s4.strip())


if __name__ == '__main__':
    # benefit of if __name__ == '__main__':
    # this section won't run if basics.py is imported as a module and not run as main program.

    #list_basics()
    #dict_basics()
    #calculators()
    str_basics()

    # TODO: __main__, and what else? what about other global variables?
