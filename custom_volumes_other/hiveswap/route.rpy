
label {{package_entrypoint}}_route:
    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True
    scene bg alternia4

    call ending pass ("gui/game_menu.png", True, True)
    return
