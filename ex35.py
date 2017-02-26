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


def dead(why):
    print why, "Good job!"
    exit(0)


gold_room()
