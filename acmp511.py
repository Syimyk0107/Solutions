a = int(input())
if a > 145:
    print('NO')
if((a<=144)and(a % 2 == 0)): 
    x = ((((a // 2)-1)*10+5) // 60)
if((a<=144)and(a % 2 != 0)): 
    y = ((((a // 2)-1)*10+10) % 60)
    
print(x, y)
