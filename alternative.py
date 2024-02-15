# asks user for a sentence
string = input("Please enter a sentence: ")

string_letters = "" # the new sentence will be created in here


for i in range(len(string)): 
    if i % 2 == 0:
        string_letters += string[i].upper() # the even numbers are going to be upper case
    else:
        string_letters += string[i].lower() # the odd numbers are going to be lower case 

print(string_letters) # prints out the upper and lower cased new sentence 

string_words_list = string.split(" ") # splitting the sentence into a list of it's words 
string_words = "" # where the new sentence will be stored

for i in range(len(string_words_list)):
    if i % 2 == 0:
        string_words += string_words_list[i].upper() + " " # the count of word which is even will be upper case
    else:
        string_words += string_words_list[i].lower() + " " # the count of word which is odd will be lower case

# prints out the final sentence 
print(string_words)
