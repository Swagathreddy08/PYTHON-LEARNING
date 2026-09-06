def clean_username(messy_name):
    username = messy_name.strip()
    username = username.lower()
    username = username.replace(" ", "_")
    if "@" in username:
        username = username.replace("@", "_")
    while "__" in username:
        username = username.replace("__", "_")
    return username

messy_name = input("Enter your name: ")
cleaned_username = clean_username(messy_name)
if cleaned_username:
    print(f"Clean username: {cleaned_username}")
else:
    print("Invalid input: username cannot be empty.")