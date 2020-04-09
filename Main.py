from time import sleep

from choice1 import choice1
from choice2 import choice2
from choice3 import choice3
from choice4 import choice4
from choice5 import choice5

print("The Pain of Python by Cain Atkinson. (https://cainy-a.github.io)\nA program about why I hate Python, "
	  "written in Python.")
sleep(0.5)
print("\nOK. First lets get some general stuff out the way you should know.\nFirst: I code in C#. I know C#, "
	  "and I like using it. I can code in Python, but it's not my primary language, and as you can probably tell, "
	  "not my favourite by a long shot.\nSecond: whenever you see this: [rtrn] it signifies that you should press "
	  "return / enter, and [1 | 2 | 3 | etc] works like in bash scripts, it signifies that you should choose an "
	  "option from the box and press enter. [rtrn]")
input()
while True:
	print('''What would you like to know about?
1: Dynamically Typed == Weakly Typed.
2: 'Hey! What version of python do I need for this script?'
3: The Non-Existence of 'private' keywords.
4: IDEs
5: Defining variables
[1 | 2 | 3 | 4 | 5]''')
	choice = input()
	if choice == '1':
		choice1()
	elif choice == '2':
		choice2()
	elif choice == '3':
		choice3()
	elif choice == '4':
		choice4()
	elif choice == "5":
		choice5()
