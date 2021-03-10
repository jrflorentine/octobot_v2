basic.forever(function () {
    while (input.buttonIsPressed(Button.A)) {
        pins.servoWritePin(AnalogPin.P12, 100)
    }
    while (input.buttonIsPressed(Button.B)) {
        pins.servoWritePin(AnalogPin.P12, 75)
    }
    pins.servoWritePin(AnalogPin.P12, 85)
})
