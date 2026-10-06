# Write your code here.

#TASK 1
def hello():
    return "Hello!"

#TASK 2
def greet(name):
    return "Hello, " + name + "!"


#TASK 3
def calc(a, b, operation= "multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except TypeError:
        return "You can't multiply those values!"
    except ZeroDivisionError:
        return "You can't divide by 0!"


#TASK 4

def data_type_conversion(value_a, convert):
    try:
        match convert:
            case "int":
                return int(value_a)
            case "float":
                return float(value_a)
            case "str":
                return str(value_a)
    except Exception:
        return f"You can't convert {value_a} into a {convert}."



#TASK 5
def grade(*args):
    try:
        total = 0
        for arg in args:
            total = total + arg
        grade = total / len(args)
        
        if grade >= 90:
            return "A"
        elif (grade >= 80) and (grade < 90):
            return "B"
        elif (grade >= 70) and (grade < 80):
            return "C"
        elif (grade >= 60) and (grade < 70):
            return "D"
        else:
            return "F"
    except Exception:
        return "Invalid data was provided."

    
# pytest -v -x assignment1-test.py

#Task 6
def repeat(word, count):
    newS = ""
    for i in range(count):
        newS = newS + word

    return newS


#Taskk 7
def student_scores(option, **kwargs):
    if option == "mean":
        total = 0

        for score in kwargs.values():
            total = total + score

        return total / len(kwargs)

    elif option == "best":
        best_student = ""
        highest_score = 0

        for name, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = name

        return best_student

#TASK 8

def titleize(word):
    new = []
    little = ["a", "on", "an", "the", "of", "and", "is", "in"]

    split = word.split()

    for i, word in enumerate(split):
        if i == 0:
            new.append(word.capitalize())
        elif i == len(split) - 1:
            new.append(word.capitalize())
        elif word in little:
            new.append(word)
        else:
            new.append(word.capitalize())

    return " ".join(new)


#Task 9
def hangman(secret, guess):
    word = ""

    for char in secret:
        if char in guess:
            word = word + char
        else:
            word = word + "_"

    return word


#TASK 10
def pig_latin(sentence):
    vowel = ["a", "e", "i", "o", "u"]
    new = []

    split = sentence.split()

    for word in split:

        if word[0] in vowel:
            new.append(word + "ay")

        else:
            consonants = ""

            for i, char in enumerate(word):

                if char == "q" and word[i + 1] == "u":
                    consonants = consonants + "qu"
                    break

                elif char not in vowel:
                    consonants = consonants + char

                else:
                    break

            new.append(word[len(consonants):] + consonants + "ay")

    return " ".join(new)

