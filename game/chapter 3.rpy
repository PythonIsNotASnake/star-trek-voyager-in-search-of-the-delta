# start second contact ------------------------------------------------------

label second_contact:
    scene bg space
    with fade
    show chapter3
    with Dissolve(2.0)
    hide chapter3
    with Dissolve(2.0)

    scene bg voyager bridge
    with fade

    show janeway smile at left
    with easeinleft

    janeway "Lagebericht Fähnrich."
    
    show ensign at right
    with easeinright

    ensign "Wir konnten den Borg entkommen."
    janeway "Wenigstens etwas Erfreuliches."
    janeway "Janeway an Maschinendeck. Wie ist die Lage bei Ihnen."

    scene bg warp core
    with fade
    show engineer at center
    with easeinbottom

    engineer "Die Außenhülle ist leicht angeschlagen."
    janeway "Wie lange brauchen Sie für die Reparaturen?"
    engineer "In einer Stunde sollten die Schäden behoben sein."
    janeway "Das freut mich zu hören. Janeway Ende."

    scene bg space
    with fade
    "Die Reparaturen gehen gut voran."
    "Eine Stunde vergeht..."

    scene bg voyager bridge
    show janeway smile at left
    with fade

    janeway "Scannen Sie den Sektor. Ich willen wissen, was da draußen ist."

    show seven at right
    with easeinright
    seven "Eine Verzerrung ganz in der Nähe. Den Sensoren zufolge taucht gleich ein Schiff auf."
    jump queen_contact

label queen_contact:
    scene bg space
    show voyager at left
    with fade

    seven "Jetzt sollte es erscheinen."

    show cube at right
    with dissolve

    seven "Es handelt sich um einen Borg Kubus."
    janeway "Scannen Sie, ob es der selbe wie vorhin ist."
    seven "Wir werden gerufen."
    janeway "Auf den Schirm."

    scene bg voyager bridge
    show janeway smile at left
    with fade

    show queen at right
    with easeinright

    janeway "Ich bin Kathryn Janeway. Captain des Föderationsraumschiffs USS Voyager. Mit wem habe ich das Vergnügen?"
    queen "Ich bin der Anfang, das Ende, die Eine, die Viele ist. Ich bin die Borg."
    
    menu:
        "Was ist Ihr Anliegen?":
            janeway "Was können wir für Sie tun?"

        "Was haben Sie vor?":
            janeway "Sie führen doch irgendwas im Schilde. Was plant das Borg Kollektiv?"
    
    queen "Kommen Sie nicht von selbst darauf?"
    queen "Wir möchten nur das, was uns genommen wurde zurück holen."
    janeway "Wovon reden Sie? Warten Sie. Sie meinen doch nicht Seven of Nine?"
    show queen laughing
    queen "Natürlich. Und wir werden sie uns holen. Händigen Sie sie freiwillig aus?"

    menu:
        "Seven of Nine aushändigen":
            janeway "Lassen Sie die Besatzung der Voyager in Frieden weiterziehen, wenn wir Ihnen Seven of Nine aushändigen?"
            queen "Wir geben Ihnen unser Wort."
            $ tradeSevenWithoutResistance = True

        "Der Forderung widersetzen":
            janeway "Wir werden Ihnen Seven of Nine niemals überlassen."
            queen "Dann werden wir sie uns eben nehmen müssen."
            $ tradeSevenWithoutResistance = False
    
    scene bg warp core
    show seven at left
    with fade

    show borg at right
    with Dissolve(2.0)
    borg "Seven of Nine wird dem Kollektiv hinzugefügt."
    borg "Widerstand ist zwecklos!"
    hide seven
    hide borg
    with Dissolve(2.0)

    jump kidnapping

label kidnapping:
    scene bg cube
    show queen at right
    with fade

    show seven at left
    show borg at center
    with Dissolve(2.0)
    show seven angry at left

    seven "Was hat das zu bedeuten?"
    queen "Das werde ich dir sofort erklären."
    queen "Entferne dich Drohne."

    hide borg
    with moveoutbottom

    queen "Es ist deine Bestimmung Teil des Kollektivs zu sein und das Kollektiv an meiner Seite zu führen."

    menu:
        "Ich bin zu Hause":
            $ isSevenEvil = True
            seven "Du hast recht. Ich beuge mich dir. Nimm mich wieder im Kollektiv auf."
            show queen laughing
            queen "Ich wusste, dass du zur Besinnung kommst."
        "Ich bin ein Individuum":
            $ isSevenEvil = False
            seven "Das denke ich nicht. Ich bin nun ein Individuum. Einem Schwarmbewusstsein möchte ich nicht mehr angehören."
            show queen angry
            queen "Mit der Zeit wirst du noch gefügig werden."
    
    scene bg space
    show voyager at left
    show cube at right
    with fade

    ensign "Captain, der Borg Kubus verschwindet."
    janeway "Nein! Seven, nicht!"

    hide cube
    with moveoutright

    jump thinking_after_kidnapping

label thinking_after_kidnapping:
    scene bg voyager bridge
    with fade

    show ensign at right
    with easeinright

    if tradeSevenWithoutResistance == True:
        ensign "Wieso haben Sie Seven of Nine freiwillig den Borg übergeben?"
        show janeway smile at left
        with easeinleft
        janeway "Dies tat ich nur um die Borg Königin in Sicherheit zu wiegen."
        ensign "In Sicherheit zu wiegen? Aber wozu?"
        janeway "Weil Sie jetzt die Gejagte ist und nicht mehr wir. Die Situation hat sich um 180 Grad gedreht. Das bringt uns möglicherweise einen taktischen Vorteil."
        ensign "Wie lauten Ihre Befehle?"
    if tradeSevenWithoutResistance == False:
        ensign "Wie lauten Ihre Befehle?"
        show janeway smile at left
        with easeinleft

    menu:
        "Verfolgen":
            janeway "Nehmen Sie die Verfolgung auf."
            janeway "Finden Sie diesen Borg Kubus."
            janeway "Finden Sie Seven of Nine."
            ensign "Wir scannen den Sektor nach Anzeichen ab."

            jump rescue_mission

        "Entkommen lassen":
            janeway "Sind wir in der Lage dem Borg Kubus zu folgen?"
            ensign "Wir haben keine Indizien wohin sie unterwegs sind. Sie könnten überall sein."
            janeway "Brechen Sie die Suche ab. Ich werde nicht das Leben der gesamten Crew riskieren, um Seven möglicherweise zu retten."

            jump end_flight_without_seven
