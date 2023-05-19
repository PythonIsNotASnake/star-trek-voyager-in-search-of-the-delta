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

default book = False


# Hier beginnt das Spiel.
label start:

    play music "audio/background.mp3"

    scene bg space
    with fade

    "Der Weltraum, unendliche Weiten."
    "Das Raumschiff USS Voyager der Intrepid-Klasse ist im Delta-Quadranten gestrandet und befindet sich auf dem Weg zum Alpha-Quadranten."
    "Die Gefahr durch die Borg ist allgegenwärtig."
    "Während ihrer Reise durch den Delta-Quadranten konnte die Crew der Voyager Seven of Nine von den Borg befreien und rehabilitieren."

    jump intro

label intro:

    scene bg voyager bridge
    with fade

    show ensign at right
    with dissolve

    ensign "Captain, ein Raumschiff nähert sich unseren Koordinaten."

    show janeway smile at left
    with dissolve

    menu:
        "Identifizieren":
            janeway "Identifizieren Sie das Raumschiff, Fähnrich."
            jump identify

        "Kaffee trinken und identifizieren":
            hide janeway smile
            with moveoutleft
            "Captain Janeway holt sich genüsslich einen Kaffee aus dem Replikator."
            show janeway smile at left
            with easeinleft
            janeway "Fähnrich, das Raumschiff sofort identifizieren."
            jump identify

label identify:
    ensign "Es handelt sich um einen Borg-Kubus."
    
    menu:
        "Fliehen":
            janeway "Wie stehen unsere Chancen zu fliehen, Fähnrich?"
            ensign "Das feindliche Schiff ist auf Abfang-Kurs. Aufeinandertreffen in fünf Minuten."
            jump first_confrontation

        "Auf Konfrontation vorbereiten":
            janeway "Energie auf die Schilde und Waffensysteme."
            jump first_confrontation


# start first borg meeting ------------------------------------------

label first_confrontation:
    scene bg space
    show voyager at left
    with fade

    show cube at right
    with easeinright
    seven "Das feindliche Schiff möchte Kontakt aufnehmen."
    menu:
        "Auf den Schirm":
            jump first_talk_with_borg
        "Energie auf die Waffensysteme":
            jump first_attack

label first_talk_with_borg:
    scene bg voyager bridge
    show janeway smile at left
    with fade

    janeway "Auf den Schirm."
    "Seven of Nine stellt die Verbindung her..."

    show borg at right
    with moveinright

    borg "Wir sind die Borg. Deaktivieren Sie Ihre Schutzschilde und ergeben Sie sich. Wir werden Ihre biologischen und technologischen Charakteristika den unseren hinzufügen. Ihre Kultur wird sich anpassen und uns dienen. Widerstand ist zwecklos!"
    menu:
        "Angreifen":
            jump first_fight_begin
        "Kapitulieren":
            jump end_assimilate
        "Fliehen":
            jump first_escape

label first_attack:
    scene bg voyager bridge
    show janeway angry at left
    with fade

    janeway "Energie auf die Waffensysteme."

    show seven at right
    with easeinright

    seven "Waffensysteme bereit."
    seven "Das Borg Schiff versucht weiterhin Kontakt aufzubauen."

    menu:
        "Auf den Schirm":
            jump first_talk_with_borg
        "Feuer!":
            jump first_fight_begin

label first_fight_begin:
    scene bg space
    show voyager at left
    show cube at right
    with fade

    janeway "Feuer auf die feindlichen Schilde."

    show voyager attack
    show cube shield

    seven "Feindliche Schilde halten."

    show voyager
    show cube shield

    borg "Widerstand ist zwecklos!"

    show voyager damaged
    show cube attack
    with vpunch
    with hpunch

    ensign "Wir wurden getroffen. Schilde bei Null."

    menu:
        "Flucht":
            jump first_escape
        "Kampf fortsetzen":
            jump first_fight_continue

label first_fight_continue:
    janeway "Nehmen Sie das Borg Schiff weiter unter Beschuss."

    show voyager attack
    show cube shield

    pause 1.0

    show voyager damaged
    show cube attack
    with vpunch
    with hpunch

    pause 1.0

    show cube

    scene bg warp core
    with fade
    show engineer at center
    with moveinbottom

    engineer "Captain, wir haben einen Hüllenbruch erlitten."
    ensign "Wie lauten Ihre Befehle?"

    scene bg space
    show voyager damaged at left
    show cube at right
    with fade

    menu:
        "Kampf fortsetzen":
            show voyager damaged
            show cube attack
            with vpunch
            with hpunch
            "Die USS Voyager hat einen schweren Treffer erlitten."
            jump end_destroyed
        "Fliehen":
            jump first_escape
        "Warp-Kern abwerfen":
            jump end_warp_core

# end first borg meeting --------------------------------------------


# start escape ------------------------------------------------------

label first_escape:
    scene bg voyager bridge
    with fade

    show janeway angry at left
    with moveinleft

    menu:
        "Fliehen mit Warp Sieben":
            jump escape_warp_seven
        "Fliehen mit Warp Neun":
            jump escape_warp_nine

label escape_warp_seven:
    janeway "Gehen Sie auf Warp Sieben."

    show ensign at right
    with moveinright

    ensign "Wie Sie wünschen Captain."

    scene bg space warp
    with blinds

    pause 1.5
    jump worm_hole_danger

label escape_warp_nine:
    janeway "Gehen Sie auf Warp Neun."

    show ensign at right
    with moveinright

    ensign "Wie Sie wünschen Captain."

    scene bg space warp
    with blinds
    show voyager warp at center
    with moveinleft

    pause 1.5

    hide voyager warp
    with moveoutright

    jump ferengi

# end escape --------------------------------------------------------


# start worm hole ---------------------------------------------------

label worm_hole_danger:
    scene bg wormhole
    with blinds

    show voyager warp at left
    with moveinleft
    show voyager at left

    ensign "Captain, ein Wurmloch voraus."
    ensign "Sollen wir hindurch fliegen?"

    menu:
        "Wurmloch betreten":
            hide voyager
            with moveoutright
            jump end_destroyed
        "Weiterfliegen":
            "WIP"

label worm_hole_save:
    scene bg wormhole
    with blinds

    show voyager warp at left
    with moveinleft
    show voyager at left

    ensign "Captain, ein Wurmloch voraus."
    ensign "Sollen wir hindurch fliegen?"

    menu:
        "Wurmloch betreten":
            hide voyager
            with moveoutright
            jump end_success
        "Weiterfliegen":
            "WIP"


# end worm hole -----------------------------------------------------


# start ferengi -----------------------------------------------------

label ferengi:
    scene bg space
    show dkora at right
    with blinds

    show voyager warp at left
    with moveinleft
    show voyager at left

    "First Escape WIP"
    return

# end ferengi -------------------------------------------------------









# End scenarios -----------------------------------------------------
label end_destroyed:
    "Destroyed End WIP"
    return

label end_assimilate:
    "Assimilated End WIP"
    return

label end_success:
    "Successful End WIP"
    return

label end_warp_core:
    janeway "Maschienendeck, werfen Sie den Warp-Kern ab!"
    # Beide Schiffe werden zerstört
    "Warp Core End WIP"
    return
