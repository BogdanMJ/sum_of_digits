
x = int(input("Give me a number: "))
XY = str(x)
sum = 0
for i in XY:
    digit = int(i)
    sum = sum + digit
A = 1
list = []
for i in range(0, len(XY), A):
    list.append(int(XY[i : i + A]))
ED = []
ON = []
for num in list:
    if num % 2 == 0:
        ED.append(num)
    if num % 2 != 0:
        ON.append(num)
avg_ED = sum(ED) / len(ED)
avg_ON = sum(ON) / len(ON)
st_ED_ON = avg_ED / avg_ON

print(f"The sum of the digits of {x} is: {sum}. The arithmetic mean of the even digits of the given number is: {avg_ED}, and the odd numbers {avg_ON}. The ratio of the averages is {st_ED_ON}")
