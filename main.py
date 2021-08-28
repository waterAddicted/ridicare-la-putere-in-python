def ridicare_la_putere(x,p):
    r=1
    while p != 0:
        if p % 2 == 1:
            r = r * x
        x = x * x
        p //= 2
    return r
    



x = int(input())
p = int(input())
print(x,"la",p,"=",ridicare_la_putere(x,p))