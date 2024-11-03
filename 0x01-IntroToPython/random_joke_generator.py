#!/usr/bin/python3
import random

joke_list = [
    'Python is the opposite of Java: Java takes 10 lines of code to print "Hello, World!" while Python does it in one.',
    'A Python developer doesn’t pass by reference; they pass with style.',
    'Python programmers don’t need glasses; they see with self.',
    'A data-driven snake is called a Pythonista.',
    'It takes zero programmers to change a light bulb—because that\'s a hardware problem.',
    'Python broke up with C++ because it found someone more dynamic.',
    'The programmer quit because he didn’t get arrays.',
    'Python and Java can’t be friends because they keep throwing type errors at each other.',
    'The object-oriented way to become wealthy is through inheritance.',
    'The if statement and else statement broke up because they couldn’t agree on their true feelings.',
    'The JavaScript developer was sad because he didn’t know how to null his feelings.',
    'Python developers make great dancers because they can follow for loops.',
    'A programmer’s Starbucks order: one Java, hold the script.',
    'Python developers prefer dark mode because light attracts bugs.',
    'The Python developer was feeling down, stuck in a loop of self-doubt.',
    'Programmers give too many excuses and not enough commits.',
    'Python lives in the mountains to avoid syntax errors.',
    'Python’s breakup line to Java: "You\'re not my type."',
    'Python developers write in lowercase because they don’t want to get CAPS-locked.',
    'Python developers avoid arguments and settle things with try-except.'
]

selected_joke = random.choice(joke_list)

print("----------------------------")
joke_title = "| radom joke generator app |".title()
print(joke_title)
print("----------------------------")

print("\n")

print("Type 'run' to generate one")
run = input("").strip().lower()

print("\n")

if run == 'run':
    print(selected_joke)
    print("\n")
else:
    print("--------------")
    print("| Try again! |")
    print("--------------")