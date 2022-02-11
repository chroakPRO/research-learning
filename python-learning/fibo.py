import time
def fibo(a=0, b=1):
    c = a + b
    time.sleep(0.05)
    print(c)
    fibo(b, c)
   
def main():
    fibo()
    
if __name__ == "__main__":
    main()
