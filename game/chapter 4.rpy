# start rescue mission ------------------------------------------------------

label rescue_mission:
    scene bg space
    with fade
    show chapter4
    with Dissolve(2.0)
    hide chapter4
    with Dissolve(2.0)

    scene bg space
    show cube at center
    with fade

    "Inzwischen an einem anderen Teil im Delta Quadranten."

    scene bg cube
    with fade

    if isSevenEvil == True:
        jump bad_seven
    if isSevenEvil == False:
        jump good_seven
    
label good_seven:
    show queen at right
    show seven angry at left
    with moveinright

    queen "Kommst du nun endlich zur Besinnung und schließt dich uns an oder muss ich dich dazu zwingen?"

    menu:
        "Dem Schwarmbewusstsein nachgeben":
            seven "Ich werde mich dem Kollektiv hingeben."
            queen "Sehr schön. Dann werde ich alle Vorkehrungen für deine Rückkehr ins Kollektiv treffen."
            queen "Wenn du in der Zwischenzeit irgendwelche Fragen hast nur zu."
            jump spy
        "Dem Schwarmbewusstsein widersetzen":
            seven "Als Individuum werde ich mich nie wieder dem Kollektiv beugen."
            jump prisoner

label bad_seven:
    show queen laughing at right
    show seven at left
    with moveinright

    queen "Endlich hast du dich zurück besonnen. Hier gehörst du hin."
    queen "Wir sind deine wahre Familie. Betrachte mich einfach als deine Mutter."

    menu:
        "Natürlich":
            seven "Ja Mutter."
            queen "Sehr schön. Dann werde ich alle Vorkehrungen für deine Rückkehr ins Kollektiv treffen."
            queen "Wenn du in der Zwischenzeit irgendwelche Fragen hast nur zu."
            jump spy
        "Niemals":
            seven "Ich werde dich niemals als meine Mutter ansehen. Meine Eltern wurden vom Kollektiv getötet."
            jump prisoner

label prisoner:
    queen "Dann sehe ich keinen anderen Weg, als dich mit Gewalt ins Kollektiv aufzunehmen."
    queen "Drohnen, führt sie ab."
    show borg at center
    with moveinbottom
    borg "Fügen Sie sich Seven of Nine und folgen Sie uns."
    seven "Argh..."
    hide seven
    hide borg
    with moveoutbottom
    queen "Bald wird Seven of Nine wieder dem Kollektiv angehören. (Hämisches Gelächter)"
    jump voyager_preparation

label spy:
    menu:
        "Verbindung mit Kollektiv":
            seven "Wann werde ich wieder mit dem Schwarmbewusstsein verbunden sein."
            queen "Da hat es aber jemand eilig."
            queen "Die Prozedur kann etwas Zeit in Anspruch nehmen."
            queen "Hast du sonst noch Fragen?"
            jump spy
        "Pläne mit der Voyager":
            seven "Was hat das Kollektiv mit der Voyager vor?"
            queen "Diese Information ist nur innerhalb des Schwarmbewusstseins verfügbar."
            queen "Ich kann dir soviel sagen, dass der Voyager keine Gefahr droht, sofern sie uns nicht in die Quere kommt."
            queen "Hast du sonst noch Fragen?" 
            jump spy
        "Zugang zu Systemen":
            seven "Könnte ich wohl Zugang zu den Systemen erhalten?"
            queen "Wozu brauchst du denn Zugang zu den Systemen der Borg?"
            menu:
                "Erfahren was nach Austritt geschah":
                    seven "Ich möchte gerne erfahren, was es für Neuerungen der Borg gibt. Seit meinem Austritt aus dem Kollektiv wurden doch bestimmt neue Spezien hinzugefügt."
                    queen "Das klingt plausibel. Du sollst deinen Zugang erhalten."
                    "Seven of Nine verbindet sich mit den Systemen."
                    "Sie findet eine Frequenz, um die Schilde des Borg Kubus zu durchdringen."
                    $ hasFrequence = True
                    $ hasCorrectFrequence = True
                    $ hasSevenFrequence = True
                    jump spy
                "Informationen über Schiffssysteme":
                    seven "Ich würde gerne mehr über die Schiffssysteme in Erfahrung bringen."
                    queen "Das ist momentan nicht nötig. Oder möchtest du das Kollektiv etwa ausspähen um Informationen an die Voyager zu senden?"
                    queen "Das werde ich unterbinden. Es ist Zeit, dich ins Kollektiv einzubinden."
        "Keine Fragen":
            seven "Nein. Ich weiß alles, was ich wissen muss."
            queen "Sehr schön. Dann können wir alles für die Prozedur vorbereiten. Bald bist du wieder ein Teil von uns."
    hide seven
    hide queen
    with moveoutright

    jump voyager_preparation

label voyager_preparation:
    scene bg voyager bridge
    with fade
    show janeway smile at left
    with moveinleft
    janeway "Gibt es bereits eine Spur vom Borg Kubus?"
    show ensign at right
    with moveinright
    ensign "Wir konnten den Kubus lokalisieren."
    janeway "Sehr gut."
    jump rescue_journey_talk

label rescue_journey_talk:
    menu:
        "Wie lange bis wir dort sind?":
            janeway "Fähnrich, wann werden wir den Standort des Borg Kubus erreichen?"
            ensign "In ungefähr zwei Stunden."
            menu:
                "Akzeptabel":
                    janeway "Sehr schön. Bis dahin können wir uns auf den Ernstfall vorbereiten."
                    ensign "Sehr wohl Captain."
                    jump rescue_journey_talk
                "Zu langsam":
                    janeway "Geht das nicht schneller?"
                    janeway "Janeway an Maschinendeck. Können wir mit einer höheren Geschwindigkeit fliegen?"
                    engineer "Wir fliegen aktuell mit Warp Vier. Maximal Warp Fünf wäre möglich. Andernfalls können die Systeme irreparabel beschädigt werden."
                    janeway "Danke für die Auskunft."
                    janeway "Fähnrich, sie haben es gehört. Gehen Sie auf Warp Fünf."
                    ensign "Wie Sie wünschen Captain."
                    jump rescue_journey_talk

        "Wie steht es um die Schiffssysteme?":
            janeway "Maschinendeck bitte kommen."
            jump machine_talk
        "Weiterfliegen":
            jump rescue_location

label machine_talk:
    scene bg warp core
    with fade
    show engineer at center
    with moveinbottom
    engineer "Hier Maschinendeck. Was kann ich für Sie tun?"
    jump machine_talk_decisions

label machine_talk_decisions:
    menu:
        "Schilde":
            janeway "Ist mit den Schilden alles in Ordnung? Dies soll eine Rettungsmission werden und kein Himmelfahrtskommando."
            engineer "Die Schilde sind voll funktionstüchtig. Es sollten keine Komplikationen auftreten."
            janeway "Wunderbar."
            jump machine_talk_decisions
        "Waffensysteme":
            janeway "Wie steht es um unsere Waffenphalanx?"
            engineer "Der letzte Scan hat keine Fehler oder andere Beeinträchtigungen gefunden."
            janeway "Ausgezeichnet."
            jump machine_talk_decisions
        "Keine weiteren Fragen":
            janeway "Danke. Keine weiteren Fragen."
            scene bg voyager bridge
            show janeway smile at left
            show ensign at right
            with fade
            jump rescue_journey_talk

label rescue_location:
    scene bg space warp
    show voyager warp at center
    with fade
    "Die Voyager erreicht ihr Ziel in Kürze."
    hide voyager warp
    with moveoutright

    scene bg space
    show cube at right
    with fade
    show voyager warp at left
    with moveinleft
    show voyager

    "Die USS Voyager hat endlich den Borg Kubus erreicht, auf welchem sich Seven of Nine aufhält."

    scene bg voyager bridge
    show janeway smile at left
    with fade

    jump rescue_decisions

label rescue_decisions:
    menu:
        "Borg Kubus rufen":
            jump negotiation
        "Rettungstrupp beamen":
            jump beam
        "Borg Kubus unter Beschuss nehmen":
            jump attack_queen

label negotiation:
    janeway "Rufen Sie den Borg Kubus."
    show queen at right
    with moveinright
    queen "Captain Janeway. Welch unerwartete Überraschung Sie wiederzusehen."
    janeway "Schluss mit den Höflichkeitsfloskeln. Was haben Sie mit Seven angestellt."
    show queen laughing
    queen "Oh. Sie meinen Seven of Nine. Seven of Nine wird gerade dem Kollektiv hinzugefügt. Ich fürchte, Sie kommen zu spät."
    janeway "Fähnrich, Verbindung trennen."
    hide queen
    with moveoutright
    jump rescue_decisions

label beam:
    if hasSevenFrequence == True:
        ensign "Uns erreicht eine Nachricht vom Borg Kubus."
        janeway "Was steht drin?"
        ensign "Es scheint eine Art Frequenz zu sein."
        janeway "Die schickt uns bestimmt Seven."
    
    elif hasFrequence == False:
        scene bg space
        show voyager at left
        show cube shield at right
        with fade

        engineer "Aufgrund ihrer Schilde sind wir nicht in der Lage jemanden hinüber zu beamen."
        ensign "Der Borg Kubus legt Energie auf seine Waffensysteme und..."
        
        show voyager damaged
        show cube attack
        with vpunch
        with hpunch

        jump end_fight_destroyed

    elif hasCorrectFrequence == False:
        jump wrong_frequence
    
    janeway "Konfiguriert die Phaserbänke entsprechend der Frequenz, die wir erhalten haben und nehmt den Borg Kubus unter Beschuss."
    ensign "Wie Sie wünschen."
    scene bg space
    show voyager at left
    show cube shield at right
    with fade

    janeway "Feuer!"

    show voyager attack
    show cube shield
    with vpunch
    with hpunch
    show cube

    ensign "Schilde des Borg Kubus sind unten."

    scene bg warp core
    with fade
    show engineer at left
    with moveinbottom
    show janeway angry at right
    with moveinright

    janeway "Beamen Sie mich rüber."
    engineer "Jawohl Captain."

    hide janeway
    with Dissolve(2.0)

    jump beam_success

label attack_queen:
    janeway "Nehmen Sie den Borg Kubus unter Beschuss."

    scene bg space
    show voyager at left
    show cube shield at right
    with fade
    
    if hasSevenFrequence == False:
        jump borg_shields_up
    elif hasFrequence == False:
        jump borg_shields_up
    
    if hasSevenFrequence == True:
        ensign "Uns erreicht eine Nachricht vom Borg Kubus."
        janeway "Was steht drin?"
        ensign "Es scheint eine Art Frequenz zu sein."
        janeway "Die schickt uns bestimmt Seven."
    elif hasCorrectFrequence == False:
        jump wrong_frequence
    
    janeway "Konfiguriert die Phaserbänke entsprechend der Frequenz, die wir erhalten haben und nehmt den Borg Kubus unter Beschuss."
    ensign "Wie Sie wünschen."
    scene bg space
    show voyager at left
    show cube shield at right
    with fade

    janeway "Feuer!"

    show voyager attack
    show cube shield
    with vpunch
    with hpunch
    show voyager
    show cube

    ensign "Schilde des Borg Kubus sind unten."

    menu:
        "Angreifen und Borg Kubus vernichten":
            janeway "Es spielt keine Rolle, ob wir damit Seven of Nine verlieren. Wir müssen die Borg Königin aufhalten."
            janeway "Nehmt den Borg Kubus weiter unter Beschuss."

            show voyager attack
            show cube damaged
            with vpunch
            with hpunch

            jump end_fight_win
        "Auf den Borg Kubus beamen":
            scene bg warp core
            with fade
            show engineer at left
            with moveinbottom
            show janeway angry at right
            with moveinright

            janeway "Beamen Sie mich rüber."
            engineer "Jawohl Captain."

            hide janeway
            with Dissolve(2.0)

            jump beam_success

label borg_shields_up:
    ensign "Sie haben ihre Schilde noch oben. Wir werden Sie nicht durchdringen können."
    menu:
        "Borg Kubus unter Beschuss nehmen":
            janeway "Nehmen Sie den Kubus unter Beschuss."
            ensign "Aye Captain."
            show voyager attack
            show cube shield
            ensign "Feindliche Schilde halten."
            show voyager
            show cube shield
            queen "Feuer erwidern!"
            show voyager damaged
            show cube attack
            with vpunch
            with hpunch
            jump end_fight_destroyed
        "Warp Kern abwerfen":
            jump end_warp_core
        "Fliehen":
            janeway "Ein weiser Captain muss einsehen, wann er verloren hat. Wir treten den Rückzug an."
            jump end_flight_without_seven

label wrong_frequence:
    janeway "Benutzt die Frequenz vom Ferengi Händler, um die Phaserbänke anzupassen."
    ensign "Wird sofort erledigt."
    "..."
    ensign "Phaserbänke wurden umgestellt."
    janeway "Deaktiviert die feindlichen Schilde."

    scene bg space
    show voyager at left
    show cube shield at right
    with fade

    janeway "Feuer!"

    show voyager attack
    show cube shield

    janeway "Fähnrich, Bericht."
    ensign "Die feindlichen Schilde halten."
    janeway "Der Ferengi hat uns eine falsche Frequenz verkauft." 

    show voyager damaged
    show cube attack
    with vpunch
    with hpunch

    jump end_fight_destroyed

label beam_success:
    scene bg cube
    with fade
    show janeway smile at left
    with Dissolve(2.0)

    janeway "Janeway an Voyager. Ich bin auf dem Kubus. Nun muss ich Seven finden."
    ensign "Haben verstanden. Lebenszeichen bewegen sich auf Ihre Koordinaten zu."

    hide janeway
    with moveoutbottom

    borg "..."

    show borg at center
    with moveinright
    borg "..."
    hide borg
    with moveoutleft

    seven "Nein nicht! Aufhören!"
    show janeway angry at left
    with moveinbottom
    janeway "Das klang nach Seven. Der Schrei kam von da drüben."
    hide janeway
    with moveoutright

    scene bg cube
    with fade
    show janeway angry at center
    with moveinleft
    janeway "Irgendwie sehen alle Gänge gleich aus."
    hide janeway angry
    with moveoutright

    scene bg cube
    show seven angry at right
    show queen laughing at center
    with fade
    seven "Hör auf damit! Diese Stimmen in meinem Kopf! Aufhören!"
    queen "Ha ha ha!"
    queen "Du wirst wieder zu einem Teil von uns."
    show janeway angry at left
    with moveinleft
    queen "Janeway. Wie kommst du hier her? Wieso wurde die Voyager noch nicht zerstört?"
    janeway "Nenne es Glück oder Einfallsreichtum. Fakt ist, dass ich vor dir stehe."
    janeway "Und jetzt lass Seven frei."
    queen "Nicht widerstandslos."

    jump melee_fight

label melee_fight:
    scene bg cube
    with pixellate
    "Battle"
    show janeway angry at left
    with easeinleft
    show queen angry at right
    with easeinright
    "Fight!"

label fight_action:
    if queenHp <= 0:
        jump queen_defeated
    if janewayHp <= 0:
        jump janeway_defeated

    menu:
        "Schlagen":
            show queen angry at right
            with vpunch
            with hpunch
            $ queenHp = queenHp - 20
            queen "Autsch! Nimm das!"

            show janeway angry at left
            with vpunch
            with hpunch
            $ janewayHp = janewayHp - 30
            janeway "Argh!"

            jump fight_action
        "Treten":
            show queen angry at right
            with vpunch
            with hpunch
            $ queenHp = queenHp - 40
            queen "Uff! Das bekommst du zurück."

            show janeway angry at left
            with vpunch
            with hpunch
            $ janewayHp = janewayHp - 30
            janeway "Argh!"

            jump fight_action

label janeway_defeated:
    scene bg cube
    show janeway angry at left
    show queen laughing at center
    show seven angry at right
    with pixellate

    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)

    janeway "Uff!"
    hide janeway angry
    with fade
    queen "Die Borg triumphieren! Mein Plan ist geglückt und Seven of Nine gehört endlich mir."
    seven "Nein! Janeway!"

    scene bg space
    show voyager at left
    show cube at right
    with fade

    queen "Janeway wurde besiegt. Vernichtet die Voyager!"
    show cube attack
    show voyager damaged
    with hpunch

    hide voyager
    with vpunch

    "Captain Janeway wurde im Kampf besiegt und die USS Voyager ist nur noch ein Haufen Trümmer, welche durch das All treiben."
    "Seven of Nine wird wieder Teil des Borg Kollektivs. Niemand weiß, wie viel Zeit der Menschheit noch bleibt."

    return

label queen_defeated:
    scene bg cube
    show janeway smile at left
    show queen angry at center
    show seven at right
    with pixellate

    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)

    queen "Uff!"
    hide queen
    with fade
    janeway "Die Borg Königin ist besiegt. Nun lass mich Sie befreien Seven of Nine und dann fliehen wir von hier."
    seven "Ich dachte schon sie würde gewinnen und ihren Plan umsetzen."
    janeway "Voyager, zwei Personen zum Beamen."

    hide janeway
    hide seven
    with Dissolve(2.0)

    scene bg voyager bridge
    with fade
    show janeway smile at left
    show seven at right
    with Dissolve(2.0)

    janeway "Fähnrich, machen Sie die Waffensysteme bereit. Zerstören wir diesen Kubus."
    ensign "Mit Vergnügen."

    scene bg space
    show voyager at left
    show cube at right
    with fade

    janeway "Feuer!"
    show voyager attack
    show cube damaged
    with hpunch

    hide cube
    with vpunch

    show voyager

    janeway "Fähnrich, bringen Sie uns von hier weg. Gehen Sie auf Warp Neun."

    show voyager warp
    hide voyager
    with moveoutright

    "Dieses Abenteuer endet hier."
    "Doch die Reise der USS Voyager und ihrer Besatzung geht weiter."

    scene bg space
    show intro
    with MoveTransition(delay=4.0, enter=_movebottom)
    hide intro
    with Dissolve(5.0)

    return


return
