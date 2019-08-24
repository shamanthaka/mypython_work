def square_numbers(nums):
    lists =[]
    for i in nums:
        lists.append(i * i)
    return lists

if __name__ == '__main__':
    nums_of_squares = square_numbers([1,2,3,4,5,6])
    for num in nums_of_squares:
        print(num)