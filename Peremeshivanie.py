from random import randint
massiv = [1]*10
for i in range(10):
    massiv[i] *= randint(1,10)
print(massiv)
massiv2 = [1]*10
count =1
while len(massiv) > 1:
    #print(len(massiv))
    index = randint(0,len(massiv)-1)
    #print(index)
    massiv2[count] = massiv[index]
    massiv.pop(index)
    count += 1
massiv2[0]=massiv[0]
print(massiv2)