data = []
import math
import pygame
def calc2(x, i, v):
    
    for p in range(x):
        x2 = (1 + i)**1 * v
        v = x2
        data.append(x2)

def main():
    calc2(10, 0.02, 1000)
    print(data)
if __name__ == '__main__':
    main()
