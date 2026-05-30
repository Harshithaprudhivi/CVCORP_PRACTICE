# def display(n,a,b):
#     print(f"name:{n}")
#     print(f"age:{a}")
#     print(f"branch:{b}")
# display("harshi",20,"data science")
#

# def fun(*a):
#     print(a)
#     print(*a)
# fun(10,20)

# def fun2(**b):
#     print(b)
#     print(**b)
# fun2(a=76,b=30,c=40,d=70)

# def fun3(a,b,c,d):
#     print(a,b,c,d)
# fun3(a=10,b=20,c=30,d=40)

def fun6(*a):
    i = 0
    s = 0
    while i < len(a):
        if a[i] % 2 == 0:
            s += a[i]git
        i+=1
    print(s)
fun6(1,2,3,4,5,6)