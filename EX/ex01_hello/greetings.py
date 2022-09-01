"""EX01 Greetings."""
"""
3. GreetingsGreetingsGreetings
Example output:

Enter a greeting: Hello
Enter a recipient: world
How many times to repeat: 3
Hello world! Hello world! Hello world!

"""
command1 = input("Enter a greeting: ")
command2 = input("Enter a recipient: ")
command3 = input("How many times to repeat: ")
calculation = (command1 + " " + command2 + " ") * int(command3)
print(calculation)
