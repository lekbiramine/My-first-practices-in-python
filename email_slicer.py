# Email Slicer 

email = input("Enter your email address:")
name = email[:email.index("@")]
domain = email[email.index("@")+1:]

print(f"Your username is {name} and domain is {domain}")