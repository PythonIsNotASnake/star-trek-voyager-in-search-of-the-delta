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
