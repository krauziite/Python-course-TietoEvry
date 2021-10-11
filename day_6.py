#1.
input_string = input("Enter a list element separated by space ")
My_list  = input_string.split()
sum = 0
avg=0
for num in My_list:
    sum += int (num)
    avg=sum/len(My_list)
print("Sum = ",sum)
print("Average = ", avg)

list_numbers = []

while True:
    user_input = input("Input a number or 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Thank you! Exiting")
        break
    else:
        list_numbers.append(float(user_input))
        print(f"All numbers: {list_numbers}\nAverage is {sum(list_numbers) / len(list_numbers):.2f}")
        print(f"BOTTOM 3 {sorted(list_numbers)[:3]}")
        print(f"TOP 3 {sorted(list_numbers)[-3:]}")

# 1.b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exiting the program is by entering "q"

input_string = input("Enter a list element separated by space ")
My_list  = input_string.split()
sum = 0
avg=0
for num in My_list:
    sum += int (num)
    avg=sum/len(My_list)
print("Sum = ",sum)
print("Average = ", avg)
print(f"You entered these numbers: {input_string}")
exit_code=input("Enter q to exit")
if exit_code == "q":
    exit()

#1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.

input_string = input("Enter a list element separated by space ")
My_list  = input_string.split()
sum = 0
avg=0
for num in My_list:
    sum += int (num)
    avg=sum/len(My_list)
print(My_list)
print("Sum = ",sum)
print("Average = ", avg)
print(f"You entered these numbers: {My_list}")
print(f"Top 3 numbers are {My_list[:3]}")
print(f"Bottom 3 numbers are {My_list[-3:]}")
exit_code=input("Enter q to exit")
if exit_code == "q":
    exit()

#2. Cubes
#
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
#
# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125
# All cubes: [8,27,64,125]
# PS could theoretically do without a list, but with a list it will be more convenient

first_no=int(input("Enter the first number: "))
second_no=int(input("Enter the second number: "))
no_list=[]
no_list.append(first_no)
no_list.append(second_no)
print(f"You have entered: {no_list}")
cubes=[n**3 for n in no_list]
print(f"All cubes: {cubes}")
for el,i in no_list,cubes:
     print(f"{el} cubed is {i}")
        
first = int(input("first number: "))
last = int(input("last number: "))
if first < last:
    # list comprehension
    cubed = [n**3 for n in range(first, last+1)]
    # list comprehensions are great but it is a bit tricky to print while creating a list comprehension
    print(cubed)
else:
    print("not gonna happen")

optional_list = []
# regular loop is a bit easier to do extra work such as printing some output
for n in range(first, last+1):
    cube = n**3
    print(f"{n} cubed: {cube}")
    optional_list.append(cube)
print(optional_list)

# 3. Reversed words
# The user enters a sentence.
# We output all the words of the sentence in reverse form. - not the whole text reversed!!
# Example
# Alus kauss mans -> Sula ssuak snam
# PS Split and join operations could be useful here.

sentence=input("Your sentence: ")
sentence_list=sentence.split()
print(sentence_list)
reversed_list=[i[::-1] for i in sentence_list]
new_sentence=" ".join(reversed_list)
print(new_sentence)

sentence = input("Input the sentence: ")
words = sentence.split()
print(words)
# reversed_word_list = [word[::-1] for i, word in enumerate(words)]  # here we are not using i but it is nice to have if you want
reversed_word_list = [word[::-1] for word in words]  # here we are not using i but it is nice to have if you want
# reversed_word_list = [word[::-1] for word in words if len(word) > 2]  # with short word filter
print(reversed_word_list)
reversed_sentence = ' '.join(reversed_word_list).capitalize()
print(f"{sentence} -> {reversed_sentence}")


# 4. Prime numbers -
# this could be a weekend assignment, there is hardly enough time in class
# Find and output the first 20 (even better option to choose how many first primes we want) prime numbers in
# the form of a list i.e. [2,3,5,7,11, ...]

def generate_n_primes(N):
     primes  = []
     chkthis = 2
     while len(primes) < N:
         ptest    = [chkthis for i in primes if chkthis%i == 0]
         primes  += [] if ptest else [chkthis]
         chkthis += 1
     return primes
print(generate_n_primes(20))
