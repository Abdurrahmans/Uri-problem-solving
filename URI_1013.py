import math
a,b,c = input().split(" ")
max = (int(a)+int(b)+abs(int(a)-int(b)))/2
MaiorAB = (int(max)+int(c)+abs(int(max)-int(c)))/2

print ("{} eh o maior".format(int(MaiorAB)))