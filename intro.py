print("""
A GAME THAT DOESN'T HAVE A NAME YET
Interactive fiction - a science fiction story
Copyright(c) 2018 by ME (...even though I haven't copyrighted it yet...)
Something, lalaallalalala,
Just play the damn game! """)

print()

intro = "You wake up. The cell is cold. You have no blanket as the natives on this planet are immune to cold. However, you are not. You wished you were, but you're not. Your body is heavy from the sedative they use to keep prisoners manageable and your head feels foggy."
print('You are an intergalactic ambassador from a confederation of planets.')
print(intro)
print()


def begin():
    verbs = ['get up', 'rise']

    if any(word in action for word in verbs):
        print('It is very hard, but you somehow manage to move your limbs to stand up. You notice the edges of your vision vingette slightly.')

    if action == 'wake up':
        print("You're groggy but awake.")

    if action == 'get out':
        print('(Out of cot)')
        print('It is very hard, but you somehow manage to move your limbs to stand up. You notice the edges of your vision vingette slightly.')

    # else:
    #     print('You want to do WHAT?!')


def discover():
    print('You see your cell is bare except for the cott you were lying on and a backless stool tucked underneath a plain wooden table. Atop the table is a poorly-made hollow tube with a bottom precariously welded on--it seems to leak whenever you try to carry any liquid with it.')
    print('There is nothing else in your cell.')


def pain():
    print("It's difficult for you to move around your cell, however small it is. You're not yet in control of all your numb limbs. You can barely stand.")
    print()
    discover()


while True:
    action = input('>')
    begin()

    # search = ['look around', 'walk around', 'search']
    if 'look around' in action:
        discover()
    if 'walk around' in action:
        pain()