#Write your code below this line 👇
def prime_checker(number):
    number_list = []
    for i in range (1, 101):
        if number % i == 0 :
            number_list.append(i)
    if len(number_list) == 2:
        if number in number_list:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
