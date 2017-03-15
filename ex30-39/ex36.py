from sys import exit


def start():
    print "Do you want to play a game?"

    choice = raw_input('> ')

    if 'yes' in choice:
        print "Wow, I expected you to say no... Okay let's play."
        intro()
    elif 'no' in choice:
        print "I can respect that."
        exit(0)
    else:
        print "A simple 'yes' or 'no' will do."
        start()


def intro():
    print "We're going to make up a game on the fly. Bear with me."
    print "Speaking of bears, do you like bears?"

    choice = raw_input('> ')

    if 'yes' in choice:
        print "Did you know that bears can climb a tree faster than humans?"
        know = raw_input('> ')

        if 'yes' in know:
            print "Smart ass."
            exit(0)
        else:
            print "Damn, dude. Read a book."

    elif 'no' in choice:
        print "Yeah, fuck bears."
        continue_game()
    else:
        print "No one needs any of you attitude. Bye!"
        exit()


def continue_game():
    print "Did you know that bears eat beets?"

    answer = raw_input('> ')

    if 'yes' in answer:
        print "Beets, bears, Battlestar Galactica."
    elif 'no' in answer:
        print "Of course you didn't dumbass."
        exit()
    else:
        print "You have a lot to learn, like typing for one."
        print "One more soft one!"
        final()


def final():
    print "Thanks for playing the game with me!"
    print "Do you want to keep playing?"

    answer = raw_input('> ')

    if 'yes' in answer:
        intro()
    else:
        'Bye dummie!'
        exit()


start()

