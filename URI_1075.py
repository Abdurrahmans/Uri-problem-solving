number = int(input())
if number<10000:
    for i in range(1,10000):
        if i%number==2:
            print(i)