#Conditional Dictionary Comprehension
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# Dict Comprehension:
# new_dict = {new_key:new_value for item in list}
string = "Welcome to the begginning of your endeavors"
# result = {word:len(word) for }

result = {word:len(word) for word in string.split()}
print(result)