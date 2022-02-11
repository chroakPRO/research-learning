# String Concatenation / Formatting

import multiprocessing as mp
import sys
import argparse
names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = ' '.join(['Hello there', name])
    print(statement)

# use join when there are more then three.
names = ['Jeff', 'Gary', 'Jill', 'Samantha']
print(', '.join(names))

# Correct
# Can also use indexes instead in the {}
who = 'Gary'
how_many = 12

print('{} bought {} apples today!'.format(who, how_many))

# -------------------------------------------------------------------------------
# ArgParse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()
# -------------------------------------------------------------------------------
# List comprehension


xyz = (i for i in range(50000000))
print(list(xyz)[:5])
int()
xyz = [i for i in range(50000000)]
print(xyz[:5])

[print(i) for i in range(5)]

[[print(i, ii) for ii in range(3)] for i in range(5)]


input_list = [5, 6, 2, 1, 6, 7, 10, 12]
asd.upper()


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))
print(list(xyz))


# -------------------------------------------------------------------------------
# Timeit module
print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = list(i for i in input_list if div_by_two(i))
''', number=50000))


print(timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = [i for i in input_list if div_by_two(i)]''', number=50000))
# -------------------------------------------------------------------------------
# Enumerate


example = ['left', 'right', 'up', 'down']
for i in range(len(example)):
    print(i, example[i])

# Instead, you can do:

for i, j in enumerate(example):
    print(i, j)

That iterable can be a dict:

example_dict = {'left': '<', 'right': '>', 'up': '^', 'down': 'v', }
[print(i, j) for i, j in enumerate(example_dict)]

new_dict = dict(enumerate(example))
print(new_dict)

# -------------------------------------------------------------------------------
# Enumerate


new_dict = dict(enumerate(plz2))
print(new_dict)

# ------------------------------------------------------------------------------------------

# zip - combines two lists,

x7 = [1, 2, 3, 4]
x8 = [7, 6, 2, 1]
x9 = ['a', 'b', 'c', 'd']

for a, b in zip(x7, x8):
    print(a, b)

for i in zip(x7, x8, x9):
    print(i[2])
# ----------------------------------------------------------------------------------------
# Generators
# Yield is used when creating generators.


def simple_gen():
    yield 'OH'
    yield 'There'
    yield 'There'


for i in simple_gen():
    print(i)
correct_combo = (37, 69, 5)

# bad - because u cant break it easily.
for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print('The combination was {}'.format((c1, c2, c3)))
# Good
correct_combo = (37, 69, 5)


def combo_gen():
    for c1 in range(100):
        for c2 in range(100):
            for c3 in range(100):
                yield (c1, c2, c3)


for (c1, c2, c3) in combo_gen():
    if (c1, c2, c3) == correct_combo:
        print('The combination was {}'.format((c1, c2, c3)))
        break

# ------------------------------------------------------------------------------------------
# Multiprocessing with python Intro!


def spawn():
    print('spawned!')


if __name__ == '__main__':
    for i in range(1):
        p = mp.Process(target=spawn, args=(i,))
        p.start()
        p.join()  # Wait for process to finish. They will go in order


def job(num):
    return num * 2


p = mp.Pool(processes=20)
data = p.map(job. range(20))
p.close()
# print(data)
h


# -------------------------------------------------------------------------------------------
