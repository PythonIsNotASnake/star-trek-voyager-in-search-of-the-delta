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
    ""

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
                "":

                "":
            jump spy
        "Keine Fragen":
            seven "Nein. Ich weiß alles, was ich wissen muss."
            queen "Sehr schön. Dann können wir alles für die Prozedur vorbereiten. Bald bist du wieder ein Teil von uns."

return
