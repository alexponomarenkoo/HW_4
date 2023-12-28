####Task 1
# Користувач вводить рядок з клавіатури.
# Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)
# string = input("Enter a sentence with numbers: ")
# letter_count = 0
# digit_count = 0
# for char in string:
#    if char.isalpha():
#        letter_count += 1
#    elif char.isdigit():
#        digit_count += 1
# print('Number of letters:', letter_count)
# print('Number of digits:', digit_count)

####Task 2
# Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ.
# Отримане число виведіть на екран.
# a = list(map(int,input("Enter a series of numbers separated by spaces: ").split()))
# b = int(input("Enter a number to search: "))
# k = 0
# for i in a:
#    if i==b:
#        k+=1
# print(f"The number {b} occurs {k} times")

####Task 3
# Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше.
# Отриманий рядок на екрані.
# string = input("Enter a string: ")
# search_word = input("Enter the word to search for: ")
# replace_word = input("Enter the word to replace it with: ")
# words = string.split()
# modified_words = []
# for word in words:
#    if word == search_word:
#        modified_words.append(replace_word)
#    else:
#        modified_words.append(word)
# modified_string = " ".join(modified_words)
# print(modified_string)

####Task 4
# Дано рядок. (зробити зрізи)
# - Спершу виведіть третій символ цього рядка.
# - У другому рядку виведіть передостанній символ цього рядка.
# - У третьому рядку виведіть перші п'ять символів цього рядка.
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# - У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0,
# тому символи виводяться з першого).
# - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# - У сьомому рядку виведіть усі символи у зворотному порядку.
# - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# - У дев'ятому рядку виведіть довжину цього рядка.
# string = input("Enter a word: ")
# rev=string[::-1]
# print(string[2], string[-2],string[0:5],string[0:-2],string[::2],string[1::2],rev,rev[::2],len(string),sep='\n\n',end='')

