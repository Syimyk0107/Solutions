a, b = map(int,input().split())
c = input()
if (a==b or a<b) and c == 'heat':
    print(b)
elif (a==b or a>b) and c == 'heat':
    print(a)
elif (a==b or a<b) and c == 'freeze':
    print(a)
elif (a==b or a>b) and c == 'freeze':
    print(b)
elif c == 'auto':
    print(b)
elif c == 'fan':
    print(a)