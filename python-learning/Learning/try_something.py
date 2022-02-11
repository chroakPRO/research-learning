'''def rb(v):
    return pack("<B", v[0])[0]
with open("Loggbok.dll", "rb") as f:
    data = f.read()[0xa2080:0xa3200]'''

def job(num):
    return num * 2

import multiprocessing as mp


if __name__ == '__main__':
    p = mp.Pool(processes=20)
    data = p.map(job, range(20))
    p.close()
    print(data)
