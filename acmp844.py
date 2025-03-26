import math
a,b = map(int,input().split()) 
print( int((a*b)**0.5) if (a*b)**0.5 == int((a*b)**0.5) else 0)