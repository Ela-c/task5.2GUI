import tkinter as tk
import tkinter.font as tkfont
import RPi.GPIO as GPIO


def setup():
    # declare pin standard
    # GPIO.setmode(GPIO.BCM)
    # Set pin mode for GPIO pins to OUTPUT
    for values in availableColors.values():
        pin = values['pin']
        print("pin: " + str(pin))
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


## GUI DEFINITIONS ##
mainWindow = tk.Tk()
mainWindow.title("LED Toggler")
myFont = tkfont.Font(family="Helvetica", size=12, weight="bold")

## EVENT FUNCTIONS ##


def dimLed(pin: int, duty: int):
    print(f"button pressed")
    print(f'pin: {pin}')
    GPIO.PWM(pin, 1000).ChangeDutyCycle(duty)


def close():
    # turn led off
    # GPIO.cleanup()
    print("closing program")
    # exit program
    mainWindow.destroy()


availableColors = {
    'red': {
        'label': 'Red',
        'hexCode': "#ff0000",
        'value': 'red',
        'pin': 11,
    }, 'blue': {
        'label': 'Blue',
        'hexCode': '#3944bc',
        'value': 'blue',
        'pin': 10,
    },
    'green': {
        'label': 'Green',
        'hexCode': '#3cb043',
        'value': 'green',
        'pin': 9,
    },

}

### WIDGETS ###

redSlider = tk.Scale(mainWindow, from_=0, to=255, orient='horizontal', activebackground='#ffaaaa', bg=availableColors['red']['hexCode'],
                     bd=0, command=lambda duty: dimLed(availableColors['red']['pin'], duty), font=myFont, label=availableColors['red']['label']).grid()

greenSlider = tk.Scale(mainWindow, from_=0, to=255, orient='horizontal', activebackground='#ffaaaa', bg=availableColors['green']['hexCode'],
                       bd=0, command=lambda duty: dimLed(availableColors['green']['pin'], duty), font=myFont, label=availableColors['red']['label']).grid()
blueSlider = tk.Scale(mainWindow, from_=0, to=255, orient='horizontal', activebackground='#ffaaaa', bg=availableColors['blue']['hexCode'],
                      bd=0, command=lambda duty: dimLed(availableColors['blue']['pin'], duty), font=myFont, label=availableColors['red']['label']).grid()


# for value in availableColors.values():
#     tk.Radiobutton(mainWindow, indicatoron=0, value=value['value'], text=value['label'], font=myFont,
#                    command=lambda: ledToggle(btn=value['value'], pin=2, currValue=sharedVariable.get()), bg=value['hexCode'], width=24).grid()


exitBtn = tk.Button(mainWindow, text="Exit", font=myFont,
                    command=close, bg="gray", width=24).grid()

mainWindow.protocol("WM_DELETE_WINDOW", close)

setup()
mainWindow.mainloop()
