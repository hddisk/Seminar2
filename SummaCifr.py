x=int(input("Введите целое X "))
x2 = x
count = 0
while (x2 > 1):
    x2 /= 10
    count += 1
#print(count)
summa = 0
x2=x
for i in range(0, count):
    step = int(x2 / 10**(count-1-i))
    #print(step)
    summa += step
    #print(summa)
    x2 -= step*10**(count-1-i)
    #print(x2)
print(summa)