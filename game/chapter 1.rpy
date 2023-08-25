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
