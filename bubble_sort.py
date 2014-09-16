def bubblesort(numbers):
    for j in range(len(numbers)-1,-1,-1):
        for i in range(j):
            if numbers[i]>numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            print(i,j)
            print(numbers)

numbers = [1,3,82,752,100,,2,100,90]
bubblesort(numbers)
