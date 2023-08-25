# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define janeway = Character('Captain Janeway', color="#cc0c00")
define seven = Character('Seven of Nine', color="#5c88da")
define ensign = Character('Ensign', color="#cc0c00")
define engineer = Character('Ingenieur', color="#ffcd00")

define borg = Character('Borg', color="#143421")
define queen = Character('Borg Königin', color="#143421")

define ferengi = Character('Ferengi', color="#ffa54d")

default hasFrequence = False
default hasCorrectFrequence = False


# Hier beginnt das Spiel.
label start:

    play music "audio/background.mp3"

    scene bg space
    with fade

    "Der Weltraum, unendliche Weiten."
    "Das Raumschiff USS Voyager der Intrepid-Klasse ist im Delta-Quadranten gestrandet und befindet sich auf dem Weg zum Alpha-Quadranten."
    "Die Gefahr durch die Borg ist allgegenwärtig."
    "Während ihrer Reise durch den Delta-Quadranten konnte die Crew der Voyager Seven of Nine von den Borg befreien und rehabilitieren."

    jump logo

label logo:
    scene bg space
    show intro
    with moveinbottom
    #with Dissolve(10.0)
    jump intro

label intro:

    scene bg voyager bridge
    with fade

    show seven at right
    with dissolve

    seven "Captain, ein Raumschiff nähert sich unseren Koordinaten."

    show janeway smile at left
    with dissolve

    menu:
        "Identifizieren":
            janeway "Identifizieren Sie das Raumschiff, Seven."
            jump identify

        "Kaffee trinken und identifizieren":
            hide janeway smile
            with moveoutleft
            "Captain Janeway holt sich genüsslich einen Kaffee aus dem Replikator."
            show janeway smile at left
            with easeinleft
            janeway "Seven, das Raumschiff identifizieren."
            jump identify

label identify:
    seven "Es handelt sich um einen Borg-Kubus."
    
    menu:
        "Fliehen":
            janeway "Wie stehen unsere Chancen zu fliehen, Seven?"
            seven "Das feindliche Schiff ist auf Abfang-Kurs. Aufeinandertreffen in fünf Minuten."
            jump first_confrontation

        "Auf Konfrontation vorbereiten":
            janeway "Energie auf die Schilde und Waffensysteme."
            jump first_confrontation
