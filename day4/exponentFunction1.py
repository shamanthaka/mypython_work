
print(9**2)

my_num = 123456
sum = 0

while True:
    if my_num == 0:
        break
    remainder = my_num % 10
    sum = sum + remainder
    my_num = int(my_num/10)

print(f"The sum is {sum}")


#power algorithm
def raise_to_power(base_num,pow_num):

    result = 1
    for index in range(pow_num):
        result *= base_num

    return result

print(raise_to_power(3,2))