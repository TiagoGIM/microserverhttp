from time import sleep


def keyboardTimeout(time):
    try:
        for i in range(0,int(time)):
            sleep(1) # could use a backward counter to be preeety :)
        print('No input is given.')
    except KeyboardInterrupt:
        raw_input('Input x:')
        print('You, you! You know something.')


