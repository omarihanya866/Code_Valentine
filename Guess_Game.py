secret_number = 6
guess_count = 0
guess_limit = 3
username = input('name: ')
Gender = input('(M)Male or (F)Female: ')
status = input('(S)single or (T)taken: ')
if Gender.upper() == 'F' and status.upper() == 'S':
    Ready = input(username + ' are you ready for the game? ')
    if Ready.upper() == 'YES':
        print('Welcome to the Valentines Game')
        print('''You only have three chances.
Lets see if you can guess right.
if you fail you will have to send me a Valentines massage.
if you pass you will make a wish,
who knows.. your wish might be true.''')
        while guess_count < guess_limit:
            guess = int(input('Guess: '))
            guess_count += 1
            if guess == secret_number:
                print('Congratulations ' + username + ' you won.')
                wish = input('Do you wish to become my PLP code friend: ')
                if wish == 'yes':
                  print(
                    "\U0001F600 " + username + " is my new PLP partner")
                break
        else:
            print('Ooops..! sorry ' + username + ' you failed')
    else:
        print('Thanks for your time ' + username + ' have a wonderful day.')

else:
    print('ooops..! sorry ' + username +
          ' this game is only for girls who are single.Thanks for your time.')
