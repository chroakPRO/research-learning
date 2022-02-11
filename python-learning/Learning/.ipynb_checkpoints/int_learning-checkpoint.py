new_dict = dict(enumerate(plz2))
print(new_dict)

#------------------------------------------------------------------------------------------

#zip - combines two lists,

x7 = [1, 2, 3, 4]
x8 = [7, 6, 2, 1]
x9 = ['a', 'b', 'c', 'd']

for a,b in zip(x7,x8):
    print(a,b)

import
for i in zip(x7,x8,x9):
    print(i[2])
#----------------------------------------------------------------------------------------
#Generators
#Yield is used when creating generators.
def simple_gen():
    yield 'OH'
    yield 'There'
    yield 'There'

for i in simple_gen():
    print(i)
correct_combo = (37, 69, 5)

#bad - because u cant break it easily.
for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print ('The combination was {}'.format((c1,c2,c3)))
#Good
correct_combo = (37, 69, 5)
def combo_gen():
    for c1 in range(100):
        for c2 in range(100):
            for c3 in range(100):
                yield (c1, c2, c3)
for (c1, c2, c3) in combo_gen():
    if (c1, c2, c3) == correct_combo:
        print ('The combination was {}'.format((c1,c2,c3)))
        break

#------------------------------------------------------------------------------------------
#Multiprocessing with python Intro!

import multiprocessing as mp

def spawn():
    print('spawned!')

if __name__ == '__main__':
    for i in range(1):
        p = mp.Process(target=spawn, args=(i,))
        p.start()
        p.join() #Wait for process to finish. They will go in order


def job(num):
    return num * 2

p = mp.Pool(processes=20)
data = p.map(job. range(20))
p.close()
#print(data)



#-------------------------------------------------------------------------------------------















