# End scenarios -----------------------------------------------------
label end_fight_destroyed:
    show voyager damaged
    with hpunch

    hide voyager
    with vpunch

    scene bg space
    with fade
    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)

    scene bg space

    "Die Schilde haben nicht standgehalten."
    "Die Borg konnten die Voyager zerstören."
    "Nun wird die Besatzung der USS Voyager niemals in den Alpha Quadranten zurückkehren."

    return

label end_fight_win:
    show cube damaged
    with hpunch

    hide cube
    with vpunch

    scene bg space
    with fade
    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)

    scene bg space

    "Der Borg Kubus wurde vernichtet."
    "Doch zu welchem Preis?"
    "Die Voyager kann ihre Reise durch den Delta Quadranten fortsetzen."
    "Die Borg Königin wird sie nicht länger verfolgen."

    return

label end_wormhole_destroyed:
    scene bg space
    with fade
    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)
    
    scene bg space

    show core at center
    with easeinleft

    "Das Wurmloch war instabil und ist kolabiert."
    "Die Außenhülle der Voyager ist gerissen und die Besatzung konnte nicht rechtzeitig gerettet werden."

    hide core
    with moveoutright

    return

label end_assimilate:
    scene bg space
    with fade
    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)

    scene bg voyager bridge
    show ensign at left
    show janeway angry at center
    with fade
    show borg at right
    with Dissolve(2.0)
    borg "Sie werden nun assimiliert."
    borg "Widerstand ist zwecklos!"
    hide ensign
    hide janeway
    hide borg
    with Dissolve(2.0)

    scene bg warp core
    show engineer at left
    show seven angry at center
    with fade
    show borg at right
    with Dissolve(2.0)
    borg "Sie werden nun assimiliert."
    borg "Widerstand ist zwecklos!"
    hide engineer
    hide seven
    hide borg
    with Dissolve(2.0)

    scene bg cube
    with fade
    show janeway angry at right
    show borg at left
    with Dissolve(2.0)
    janeway "Wo befindet sich meine Crew? Was haben Sie mit ihnen gemacht?"
    borg "Sie werden assimiliert. Dasselbe was wir mit Ihnen vorhaben."
    borg "Widerstand ist zwecklos!"

    hide janeway
    hide borg
    with moveoutright

    scene bg space
    show cube at center
    with fade

    "Die gesamte Besatzung der USS Voyager wurde assimiliert."
    "Nun wird die Besatzung der USS Voyager niemals in den Alpha Quadranten zurückkehren."
    
    return

label end_success:
    scene bg space
    with fade
    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)

    scene bg space

    show voyager at center
    with easeinleft

    "Die Voyager konnte erfolgreich entkommen."
    "Keine Borg in der Umgebung."
    "Die Voyager setzt ihre Reise durch den Delta Quadranten fort..."

    hide voyager
    with moveoutright

    return

label end_warp_core:
    janeway "Maschinendeck, werfen Sie den Warp-Kern ab!"
    show core at center
    with easeinbottom

    pause 0.5

    hide voyager
    hide cube
    with vpunch

    scene bg space
    with fade
    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)

    scene bg space

    "Beide Schiffe wurden zerstört."
    "Sie haben die Borg daran gehindert die Besatzung der Voyager zu assimilieren."
    "Bedauerlicherweise haben Sie dafür die gesamte Besatzung geopfert."
    "Das war es bestimmt wert."

    return

label end_flight_without_seven:
    scene bg space
    with fade
    show epilog
    with Dissolve(2.0)
    hide epilog
    with Dissolve(2.0)

    scene bg space

    show voyager at center
    with easeinleft

    "Die Voyager konnte erfolgreich entkommen."
    "Leider ohne Seven of Nine."
    "Immerhin wird die Voyager nun nicht mehr von den Borg gejagt."
    "Die Voyager setzt ihre Reise durch den Delta Quadranten fort..."

    hide voyager
    with moveoutright

    return

return
