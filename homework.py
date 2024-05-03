
document_text = ""
with open("document.txt", "r") as file_object:
    for line in file_object:
        document_text += line
print(document_text)
# word counter
counter = 0

words_list = document_text.split()
word_count = len(words_list)
print(f"Word count: {word_count}")

for string in range(len(words_list)):
    if words_list[string] == "the":
        counter += 1
print(counter)


# mean

for i in range(len(words_list)):
    my_word = words_list[i]
    print(my_word)
    print(len(my_word))
word_lengths_sum = 0
for i in range(len(words_list)):
    my_word = words_list[i]
    word_lengths_sum += len(my_word)

print(word_lengths_sum / len(words_list))


# Standard Deviation
x = word_lengths_sum/ len(words_list)

for i in range(len(words_list)):
    my_word = words_list[i]
    my_word = len(my_word) - x
    my_word = my_word ** 2
    word_lengths_sum += my_word
print((word_lengths_sum/len(words_list)) ** 0.5)




# range

min_length = 100
max_length = 0

for i in range(len(words_list)):
    my_word = words_list[i]
    my_word_length = len(my_word)
    if my_word_length < min_length:
        min_length = my_word_length
    if my_word_length > max_length:
        max_length = my_word_length

print(max_length - min_length)

# Mode
word_lengths = []
for i in range(len(words_list)):
    my_word = words_list[i]
    word_lengths.append(len(my_word))

word_lengths.sort()
word_lengths = [1, 2, 3, 4, 5, 6]
print(word_lengths)
mid = len(word_lengths) // 2
if len(word_lengths) % 2 == 1:
    print(word_lengths[mid])
else:
    lower_mid = mid - 1
    print((word_lengths[mid] + word_lengths[lower_mid]) / 2)




# Q1
    quartile1 = word_lengths[:mid - 1]

    for i in range(len(word_lengths)):
        my_word = words_list[i]
        quartile1.append(len(my_word))

    quartile1.sort()
    print(quartile1)
    mid = len(quartile1) // 2

    if len(quartile1) % 2 == 1:
        print(quartile1[mid])
    else:
        lower_mid = mid - 1
        print((quartile1[mid] + quartile1[lower_mid]) / 2)

        quartile3 = word_lengths[mid + 1:]
# IQR
        for i in range(len(word_lengths)):
            my_word = words_list[i]
            quartile3.append(len(my_word))
# Q3
        quartile3.sort()
        print(quartile3)
        mid = len(quartile3) // 2

        if len(quartile3) % 2 == 1:
            print(quartile3[mid])
        else:
            lower_mid = mid - 1
            print((quartile3[mid] + quartile3[lower_mid]) / 2)

        print(quartile3[mid] - quartile1[mid])
