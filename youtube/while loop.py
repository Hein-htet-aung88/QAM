#x = 1
#while x <= 8:
#    print(x)
#    x += 1
#print("Done")
Secret_num = "8"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != Secret_num and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter number")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("you lose")
else:
    print("you are correct")