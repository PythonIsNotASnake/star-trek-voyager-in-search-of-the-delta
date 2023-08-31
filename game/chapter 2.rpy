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
    with fade
    show voyager warp at center
    with moveinleft

    "Die Voyager flieht mit Warp Sieben..."

    hide voyager warp
    with moveoutright

    scene bg space
    with fade
    show chapter2
    with Dissolve(2.0)
    hide chapter2
    with Dissolve(2.0)

    jump worm_hole_danger

label escape_warp_nine:
    janeway "Gehen Sie auf Warp Neun."

    show ensign at right
    with moveinright

    ensign "Wie Sie wünschen Captain."

    scene bg space warp
    with fade
    show voyager warp at center
    with moveinleft

    "Die Voyager flieht mit Warp Neun..."

    hide voyager warp
    with moveoutright

    scene bg space
    with fade
    show chapter2
    with Dissolve(2.0)
    hide chapter2
    with Dissolve(2.0)

    jump ferengi

# end escape --------------------------------------------------------


# start worm hole ---------------------------------------------------

label worm_hole_danger:
    scene bg wormhole
    with fade

    show voyager warp at left
    with moveinleft
    show voyager at left

    ensign "Captain, ein Wurmloch voraus."
    ensign "Sollen wir hindurch fliegen?"

    menu:
        "Wurmloch betreten":
            hide voyager
            with moveoutright
            jump end_wormhole_destroyed
        "Weiterfliegen":
            hide voyager
            with moveoutright
            jump worm_hole_journey

label worm_hole_journey:
    scene bg space
    with fade

    show voyager at center
    with moveinleft

    pause 2.0

    hide voyager
    with moveoutright

    jump worm_hole_save

label worm_hole_save:
    scene bg wormhole
    with fade

    show voyager warp at left
    with moveinleft
    show voyager at left

    ensign "Captain, schon wieder ein Wurmloch voraus."
    ensign "Sollen wir hindurch fliegen?"

    menu:
        "Wurmloch betreten":
            hide voyager
            with moveoutright
            jump end_success
        "Weiterfliegen":
            hide voyager
            with moveoutright
            jump second_contact

# end worm hole -----------------------------------------------------


# start ferengi -----------------------------------------------------

label ferengi:
    scene bg space
    show dkora at right
    with fade

    show voyager warp at left
    with moveinleft
    show voyager at left

    seven "Ein Ferengi Schiff genau vor uns."
    seven "Was sollen wir tun?"

    menu:
        "Kontakt aufnehmen":
            jump ferengi_contact
        "Ignorieren und weiterfliegen":
            jump ferengi_ignore

label ferengi_contact:
    scene bg voyager bridge
    with fade

    show janeway smile at left
    with moveinleft
    janeway "Öffnen Sie einen Kanal!"

    show seven at right
    with moveinright
    seven "Grußfrequenzen aktiviert."
    seven "Sie antworten."
    janeway "Auf den Schirm"

    hide seven
    with moveoutright
    "..."
    show ferengi at right
    with dissolve

    janeway "Ich bin Captain Janeway vom Föderations Raumschiff Voyager."
    ferengi "Mein Name ist Nanzo. Ich bin Händler und immer auf der Suche nach lukrativer Beute... äh ich meinte einem fairen Handel."
    ferengi "Wie ich sehe haben Sie Kampfspuren von einer Auseinandersetzung mit den Borg."
    ferengi "Zu Ihrem Glück besitze ich eine Phaser Frequenz, welche einem Borg Kubus gefährlich werden kann."
    ferengi "Wären Sie offen für einen Handel?"

    menu:
        "Mit Nanzo verhandeln":
            jump ferengi_start_deal
        "Nicht auf Handel einlassen":
            janeway "Tut mir Leid, aber ich verhandel nicht mit Ferengi."
            ferengi "Ihr Pech. Ich werde schon einen Abnehmer finden. (garstiges Gelächter)"
            jump ferengi_deal_ended

label ferengi_start_deal:
    janeway "Was erwarten Sie als Gegenleistung für diese Information?"
    ferengi "20 Barren feinstes Latinum."

    menu:
        "20 Barren Latinum zahlen":
            janeway "Wir sind bereit Ihnen die 20 Barren Latinum zu zahlen."
            ferengi "Ausgezeichnet! Teleportieren Sie das Latinum auf mein Schiff und ich übergebe Ihnen die Frequenz."
            "Latinum wird transportiert..."
            ferengi "Das Latinum ist bei mir angekommen. Hier die besagte Frequenz: *****"
            $ hasFrequence = True
            $ hasCorrectFrequence = True
            jump ferengi_deal_ended
        "Den Preis drücken":
            janeway "Wir sind nur in Besitz von 10 Barren Latinum. Diese könnten wir Ihnen überlassen."
            ferengi "Das ist aber viel weniger. Lassen Sie mich überlegen."
            ferengi "..."
            ferengi "Gut. Abgemacht. Schicken Sie das Latinum auf mein Schiff und ich übermittel Ihnen die besagte Frequenz."
            "Latinum wird transportiert..."
            ferengi "Das Latinum ist bei mir angekommen. Hier die besagte Frequenz: *****"
            $ hasFrequence = True
            $ hasCorrectFrequence = False
            jump ferengi_deal_ended
        "Handel ablehnen":
            janeway "Wir haben nicht so viel Latinum und das was wir haben benötigen wir für wichtigere Güter."
            ferengi "Ihr Pech. Ich werde schon einen Abnehmer finden. (garstiges Gelächter)"
            jump ferengi_deal_ended

label ferengi_deal_ended:
    scene bg space
    show voyager at left
    show dkora at right
    with fade

    pause 1.5

    hide dkora
    with moveoutright

    janeway "Fähnrich, wir fliegen weiter."
    hide voyager
    with moveoutright
    
    jump second_contact

label ferengi_ignore:
    janeway "Ignorieren. Ich traue einem Ferengi Schiff soweit draußen nicht."
    janeway "Fähnrich, wir fliegen weiter."

    hide voyager
    with moveoutright
    
    jump second_contact

# end ferengi -------------------------------------------------------
