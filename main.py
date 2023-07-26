def on_button_pressed_a():
    if_not_pick_13 = 0
    basic.show_string("" + str((randint(1, 3))))
    if if_not_pick_13:
        basic.show_icon(IconNames.GHOST)
        basic.show_string("dragon")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("" + str((randint(2, 12))))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("" + str((randint(1, 6))))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
