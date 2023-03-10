# Problem 1:ANAGRAM CHECKER

def is_anagram(str1, str2):
    # Convert strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Check if strings have the same length
    if len(str1) != len(str2):
        return False

    # Count the occurrences of each character in both strings
    count1 = {}
    count2 = {}
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    for char in str2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1

    # Compare the character counts
    return count1 == count2


str1 = "anagram"
str2 = "nag a ram"
print(is_anagram(str1, str2))  # Output: True

str1 = "hello"
str2 = "world"
print(is_anagram(str1, str2))  # Output: False


# Problem 2: FLIZZBUZZ

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


n = 15
fizz_buzz(n)


# PROBLEM 3- FIBONACCI SEQUENCE PROBLEM

def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    prev = 1
    curr = 1

    for i in range(3, n + 1):
        next_num = prev + curr
        prev = curr
        curr = next_num

    return curr


n = 10
print(fibonacci(n))  # Output: 55
