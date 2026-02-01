print('Welcome to the online Hospital System!')

username = str(input('Enter your username: '))

password = str(input('Enter your password:'))

occupation = str("Please enter your occupation: ")

pin = (int(input("Please enter the hospital pin")))


while pin != 123456:
    pin = int(input('Incorrect hospital PIN. Please stry again'))

if pin == 123456:
    print("Hospital PIN accepted. Welcome!")

