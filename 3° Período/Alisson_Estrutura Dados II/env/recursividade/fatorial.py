def fatorial (n):
    #caso base
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)
    
if __name__ == "__main__":
    r = fatorial (10)
    print (r)