from map import lower_level
from sys import exit

print("""
A GAME THAT DOESN'T HAVE A NAME YET
Interactive fiction - a science fiction story
Copyright(c) 2018 by ME (...even though I haven't copyrighted it yet...)
Something, lalaallalalala,
Just play the damn game!""")

print()

intro = "You wake up. The cell is cold. You have no blanket as the natives on this planet are immune to cold. However, you are not. You wished you were, but you're not. Your body is heavy from the sedative they use to keep prisoners manageable and your head feels foggy."
print('You are an intergalactic ambassador from a confederation of planets.')
print(intro)
print()


class Item(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def print_items(self):
        print('\t'.join(['Name', 'Desc']))
        for item in self.items.values():
            print('\t'.join([str(words) for words in [item.name, item.desc]]))


inventory = Inventory()
print('\t Your Items:')
print('\t You have nothing.')


def begin():
    verbs = ['get up', 'rise']

    if any(word in action.lower() for word in verbs):
        print('It is very hard, but you somehow manage to move your limbs to stand up. You notice the edges of your vision vingette slightly.')

    if action.lower() == 'wake up':
        print("You're groggy but awake.")

    if action.lower() == 'get out':
        print('(Out of cot)')
        print('It is very hard, but you somehow manage to move your limbs to stand up. You notice the edges of your vision vingette slightly.')


def discover():
    print('You see your cell is bare except for the cott you were lying on and a backless stool tucked underneath a plain wooden table. Atop the table is a poorly-made hollow tube with a bottom precariously welded on--it seems to leak whenever you try to carry any liquid with it.')
    print('There is nothing else in your cell.')


def pain():
    print("It's difficult for you to move around your cell, however small it is. You're not yet in control of all your numb limbs. You can barely stand.")


def key_riddle():
    print("You find a message carved into the table that wasn't there before:")
    print()
    print('"Look no further')
    print('under your very eyes')
    print('the stars will tell you')
    print('table all your fears')
    print()
    print("It's the fear in your soul")
    print('there no life, no destiny; only death!"')
    print()


def escape_cell():
    search_word = ['go', 'move', 'look']
    if any(word in move for word in search_word):
        if 'table' in move:
            key_riddle()

    search = input('>')
    search = search.lower()
    if any(word in search for word in search_word):
        if 'under' in search:
            if 'table' in search:
                print(
                    'Under the table, you find a skeleton key wedged into a crack between two boards. It mocks you.')

    get = input('>')
    get = get.lower()

    if 'get' in get:
        if 'key' in get:
            print(
                'You wrap your hands around the body of the key. The cold metal feels good on your skin, loosening you from the grasp of the drug\'s effects.')
            print()
            print()
            inventory.add_item(
                Item('Key', 'If you don\'t know what this does...'))
            print('\t Your Inventory')
            inventory.print_items()

            escape = input('>')
            escape = escape.lower()

            if any(word in escape for word in leave):
                if 'cell' in escape:
                    print(
                        'You wobble a little as you make your way to a steel door by the foot of your cot. It\'s set into the cement wall haphazardously.')
                    print(
                        'You jam the key at where you think the keyhole is, missing a few times. Finally you hear a click, and the door swings open into the hall.')
                    print()


def hall_dungeon():
    Current = 'Hall'
    print('You step into a brightly lit hallway. It feels clinical, immaculate, so unlike the grungy windowless cement box you just stepped out of. Your eyes need a moment to adjust to the brighter-than the sun lights above.')
    print('To the South is the Sentries Quarters.')
    print('To your West is another Prisoner\'s Cell.')
    print('To your East is a bare wall with single, giant gash.')

    direction = input('>')
    move_through_hall = ['go', 'move']
    if any(word in direction.lower() for word in move_through_hall):
        if 'south' in direction:
            print('You move into the', lower_level[Current]['south'])
            print('There are stairs leading up towards the East.')
            print(
                'To the West, there is a door. It must be some sort of Equipment Closet.')

        if 'west' in direction:
            print('You look into your neighbor\'s cell. He sees you looking in and screams. Sentries storm the hall and fire a tranquilizer shot into your arm. The dosage is too much for your physiology and you fall into an unwakeable coma.')

            input('>')
            print(
                'Sweet dreams. You\'ll be here forever because you were curious about who was in the box closest to your\'s. Good job.')
            print('What will you do now?')
            quit = input(
                'RESTART it all over or EXIT like a BOSS? ')
            if 'exit' in quit.lower():
                print(
                    'Yep, I thought so! Let\'s all call it quits. You\'re already napping anyway.')
                exit(0)


def cannot():
    print('You want to WHAT?!?!')


movement = ['look around', 'walk around', 'move around']
search_word = ['go', 'move', 'look', 'walk']
leave = ['get out', 'leave', 'open']

while True:
    action = input('>')
    begin()

    look = input('>')
    if any(word in look.lower() for word in movement):
        discover()

        move = input('>')
        move = move.lower()
        if 'table' in move:
            escape_cell()

            hallway = input('>')
            hallway.lower()
            if any(word in hallway for word in search_word):
                if 'hall' in hallway:
                    hall_dungeon()

                    decision = input('>')
                    decision = decision.lower()
                    if 'go' in decision:
                        if 'east' in decision:
                            print(
                                'You climb the stairs to your sweet, sweet ESCAPE!')
                            print(
                                'You\'re not sure whether the former Prime Minister has arrived at your rendevous point, but...it should all work out...right?')
                            print('What will you do now?')
                            quit = input(
                                'RESTART it all over or EXIT like a BOSS? ')
                            if 'exit' in quit.lower():
                                exit(0)
