# Private does not exist
def choice3():
	print("\n\nClass Abstraction hurts me. In my native language, C#, I can simply have a member as 'private' or "
		  "'protected'. [rtrn]")
	input()
	print("This is easy, and most importantly, IT WORKS!!!! I cannot access a private member unless I am inside a "
		  "method of the class. [rtrn]")
	input()
	print("But in Python, this doesn't really exist. The convention is that protected members start with _ and private "
		  "members start with __, but this isn't true abstraction. [rtrn]")
	input()
	print("The interpreter will prepend private members with underscore and the name of the parent, so a class called "
		  "'Parent' with a member '__hello()' will become _Parent__hello() when out of scope. [rtrn]")
	input()
	print("\n\n")