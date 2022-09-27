n=int(input("Введите целое n "))
massiv = [1]*n
for i in range(1,n):
    massiv[i] *= massiv[i-1]*(i+1)
print(massiv)