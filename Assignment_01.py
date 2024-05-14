my_list = [2,33,234,545]
print(my_list[-2])
print()
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = 0
for x in l:
    if x % 2 == 0:
        res += x
print("The sum of even values in the list ",l," is =",res)
print()
String = 'GEEKSFORGEEKS'
print(String[:3])
print(String[2:5:1])
print(String[-3:-5])
print(String[-2])
print(String[::])
print(String[::-1])
print()
d = int(input("Enter a Number=="))
print("Decimal Number==",d)
print("Binary Number==",bin(d))
print("Octal Number==",oct(d))
print("Hexadecimal Number== ",hex(d))
print()
a = float(input("Enter the Two number: "))
b = float(input())
avg = (a + b) / 2
d1 = abs(a - avg)
d2 = abs(b - avg)
print("Average==",avg)
print("Deviation of ",a," from the average==",d1)
print("Deviation of ",b," from the average==",d2)
