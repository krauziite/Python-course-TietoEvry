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



# # Generating Triangle Shape
# def triangleShape(n):
#     for i in range(n):
#         for j in range(n-i):
#             print(' ', end=' ')
#         for k in range(2*i+1):
#             print('*',end=' ')
#         print()
#
# # Generating Pole Shape
# def poleShape(n):
#     for i in range(n):
#         for j in range(n-1):
#             print(' ', end=' ')
#         print('* * *')
#
# # Input and Function Call
# row = int(input('Enter number of rows: '))
#
# triangleShape(row)
# triangleShape(row)
# poleShape(row)
