ia,date1=input().split()
date1 = int(date1)
h1,m1,s1=input().split(":")
h1 = int(h1)
m1 = int(m1)
s1 = int(s1)
dia,date2=input().split()
date2 = int(date2)
h2,m2,s2=input().split(":")
h2 = int(h2)
m2 = int(m2)
s2 = int(s2)

count_passed_second = (h1*60*60)+(m1*60)+s1
count_remain_second1 = (86400-count_passed_second)
count_remain_second2 = (h2*60*60)+(m2*60)+s2
date = (date2-1)-date1
count_date_second = date*86400
total_second = count_remain_second1+count_remain_second2+count_date_second


D = total_second/86400
total_second = total_second%86400
H = total_second/3600
total_second = total_second%3600
M = total_second/60
total_second = total_second%60
S = total_second
print("%i dia(s)"%D)
print("%i hora(s)"%H)
print("%i minuto(s)"%M)
print("%i segundo(s)"%S)