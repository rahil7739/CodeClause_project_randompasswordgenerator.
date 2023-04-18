import random
def main():
    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*-+"
    lenght_password = int(input("Enter the lenght of the password:"))
    a = "".join(random.sample(password,lenght_password))
    print(f"Your password is {a}")
    main()
main()