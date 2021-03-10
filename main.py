def on_gesture_shake():
    pins.servo_write_pin(AnalogPin.P12, 100)
    basic.pause(1000)
    pins.servo_write_pin(AnalogPin.P12, 85)
    basic.show_icon(IconNames.HEART)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pins.servo_write_pin(AnalogPin.P12, 85)
    while input.button_is_pressed(Button.A):
        pins.servo_write_pin(AnalogPin.P12, 100)
    pins.servo_write_pin(AnalogPin.P12, 85)
    while input.button_is_pressed(Button.B):
        pins.servo_write_pin(AnalogPin.P12, 70)
    pins.servo_write_pin(AnalogPin.P12, 85)
basic.forever(on_forever)
