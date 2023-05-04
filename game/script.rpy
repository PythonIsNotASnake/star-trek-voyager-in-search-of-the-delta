# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define j = Character('Janeway', color="#cc0c00")
define b = Character('Borg', color="#143421")

define ferengi = Character('Ferengi', color="#cc0c00")

default book = False


# Hier beginnt das Spiel.
label start:

    scene bg warp core
    with fade

    ferengi "Ferengi spricht"

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    b "Hey... Umm..."

    pause

    show janeway smile at left
    with dissolve
    with vpunch
    with blinds

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    show borg at right
    with fade

    b "Ummm... Will you..."

    b "Will you be my artist for a visual novel?"

    show janeway angry at left
    show ferengi at center

    "Silence."

    scene bg space

    show cube at right
    show dkora at left

    j "Sure, but what's a \"visual novel?\""

menu:
    "What should I do?"

    "Drink coffee.":
        "I drink the coffee, and it's good to the last drop."

    "It's a videogame.":
        jump game

    "It's an interactive book.":
        jump book

label game:

    b "It's a kind of videogame you can play on your computer or a console."

    jump marry

label book:

    $ book = True

    b "It's like an interactive book that you can read on a computer or a console."

    jump marry

label marry:

    "And so, we become a visual novel creating duo."

if book:

    "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

else:

    "Sylvie helped with the script on our first video game."

    return
