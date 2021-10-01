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



def christmas_tree(n):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):
            print('',end='')
        for i in range(0,x):
            print('+',end='')
        for i in range(0,z):
            print('',end='')
        x=x*2
        x=x-1
        z=z-1
        print()
christmas_tree(5)
