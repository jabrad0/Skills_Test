# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for num in number_list:
        if num % 2 != 0:
            new_list.append(num)
    return new_list
#print all_odd(number_list)    

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []
    for num in number_list:
        if num  % 2 == 0:
            new_list.append(num)
    return new_list
#print all_even(number_list)

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for word in word_list:
        if len(word) >= 4:
            new_list.append(word)
    return new_list
#print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    min_ = number_list[0]
    for num in number_list:
        if num < min_:
            min_ = num
    return min_
#print smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    max_ = number_list[0]
    for num in number_list:
        if num > max_:
            max_ = num
    return max_
#print largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    new_list = []
    for num in number_list:
        half_num = num / 2.0
        new_list.append(half_num)
    return new_list
#print halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for word in word_list:
        wrdlength = len(word)
        new_list.append(wrdlength) 
    return new_list
#print word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    total = 0
    for num in number_list:
        total += num               
    return total
#print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    product = 1
    for num in number_list:
        product *= num
    return product
#print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    new_string = ''
    for word in word_list:
        new_string += word
    return new_string
#print join_strings(word_list)
# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    total = 0
    for num in number_list:
        total += num
    avg_ = total / float((len(number_list)))  
    return avg_
print average(number_list)

#This works as well:
#return sum_numbers(number_list) / float(len(number_list))









