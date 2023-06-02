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
    engineer "Wie lauten Ihre Befehle?"

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
            jump end_fight_destroyed
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
    with fade
    show voyager warp at center
    with moveinleft

    "Die Voyager fliegt mit Warp Sieben..."

    hide voyager warp
    with moveoutright

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

    "Die Voyager fliegt mit Warp Neun..."

    hide voyager warp
    with moveoutright

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
            "WIP"
            return


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

    janeway "Ich bin Kapitän Janeway vom Föderations Raumschiff Voyager."
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
    return

label ferengi_ignore:
    janeway "Ignorieren. Ich traue einem Ferengi Schiff soweit draußen nicht."
    janeway "Fähnrich, wir fliegen weiter."

    hide voyager
    with moveoutright
    
    return

# end ferengi -------------------------------------------------------









# End scenarios -----------------------------------------------------
label end_fight_destroyed:
    show voyager damaged
    with hpunch

    hide voyager
    with vpunch

    "Die Schilde haben nicht standgehalten."
    "Die Borg konnten die Voyager zerstören."
    "Nun wird die Besatzung der Voyager niemals in den Alpha Quadranten zurückkehren."

    return

label end_wormhole_destroyed:
    scene bg space
    with fade

    show core at center
    with moveinleft

    "Das Wurmloch war instabil und ist kolabiert."
    "Die Außenhülle der Voyager ist gerissen und die Besatzung konnte nicht rechtzeitig gerettet werden."

    hide core
    with moveoutright

    return

label end_assimilate:
    "Assimilated End WIP"
    return

label end_success:
    scene bg space
    with fade

    show voyager at center
    with moveinleft

    "Die Voyager konnte erfolgreich entkommen."
    "Keine Borg in der Umgebung."
    "Die Voyager setzt ihre Reise durch den Delta Quadranten fort..."

    return

label end_warp_core:
    janeway "Maschinendeck, werfen Sie den Warp-Kern ab!"
    show core at center
    with moveinbottom

    pause 0.5

    hide voyager
    hide cube
    with vpunch

    "Beide Schiffe wurden zerstört."
    "Sie haben die Borg daran gehindert die Besatzung der Voyager zu assimilieren."
    "Bedauerlicherweise haben Sie dafür die gesamte Besatzung geopfert."
    "Das war es bestimmt wert."

    return
