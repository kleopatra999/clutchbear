def bubblesort(numbers):
    for j in range(len(numbers)-1,-1,-1):
        for i in range(j):
            if numbers[i]>numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            print(i,j)
            print(numbers)

numbers = [10,5,3,82,752,100,20,10001,90,100]
bubblesort(numbers)
