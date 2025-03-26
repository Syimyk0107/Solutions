# n = int(input())
# while(n>0):
#     s = str(input())  
#     while ((len(s)) % 3 > 0):
#         s = '0'+s
#     while(s>''):
#         x = x+s[i]*4+s[i+1]*2+s[i+2]
#         s.delete(1,3)
#         if(x % 7 == 0):
#             print('Yes') 
#         else: print('No')
    
n = int(input())
while(n>0):
    s = str(input())  
    x=0 
    while(len(s)%3!=0):
        s="0"+s
        i=0
        while i<len(s):
            i+=3
            x+=(s[i]-'0')*4+(s[i+1]-'0')*2+(s[i+2]-'0')
            if(x%7==0):
                print("Yes")    
            if(x%7!=0):
                print("No")
 
