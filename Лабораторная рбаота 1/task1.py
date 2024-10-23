numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


i=0
j=0
sum=0
for i in range(len(numbers)):
    if numbers[i]==None:
        j=i
    else:
        sum=sum+numbers[i]
srednee=sum/len(numbers)
numbers[j]=srednee


print("Измененный список:", numbers)