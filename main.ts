let dice: string[] = []
input.onButtonPressed(Button.A, function () {
    dice = [
    "1",
    "2",
    "3",
    "dragon"
    ]
    basic.showString("" + (dice._pickRandom()))
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("" + (randint(2, 12)))
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (randint(1, 6)))
})
basic.forever(function () {
	
})
