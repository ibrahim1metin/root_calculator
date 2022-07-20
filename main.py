def f(x,n,m):
    return (x**m)-n
def f_prime(x,m):
    return m*(x**(m-1))
a=1
for i in range(1,100000):
    a-=f(a,5,8)/f_prime(a,8)
print(a)
#The code utilises the newtons technic to reach the nearest rational number. n represents the number ,root of which is going to be calculated. M represents the degree of the root.
