email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]#array concept to slice the email and domain
#creating as an object
domain = email[email.index('@') + 1:]

print(f"Your username is {username} & domain is {domain}")