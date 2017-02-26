from sys import exit


def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input(">")
    if next.isdigit():   #  .isdigit  is use for check the string is number or not
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice,you are not greedy,you win!"
        exit(0)
    else:
        dead("You're greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_move = False

    while True:
        next = raw_input(">")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_move:
            print "The bear has moved form the door .You can go through it now."
            bear_move = True
        elif next == "taunt bear" and  bear_move:
            dead("The bear gets pissed off and chews you leg off.")
        elif next =="open door" and bear_move:
            gold_room()
        else:
            print "I got no idea what that means."



def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He,it,whatever statres at you go insane."
    print "Do you flee for your life or eat you head?"

    next = raw_input(">")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input(">")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stunmble around the room until you starve.")

start()

