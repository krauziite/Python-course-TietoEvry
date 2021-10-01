# for fizzbuzz in range(100):
#     if fizzbuzz % 5 == 0 and fizzbuzz % 7 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 7 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)


# num=input("Please write a number:")
# num=int(num)
# flag=False
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#
#     # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")


def tree(n):
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
        x+=2
        z-=1
tree(5)
