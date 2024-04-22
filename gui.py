import tkinter as tk
import tkinter.font as tkfont
import RPi.GPIO as GPIO


def setup():
    # declare pin standard
    GPIO.setmode(GPIO.BCM)
    # Set pin mode for GPIO pins to OUTPUT
    for values in availableColors.values():
        pin = values['pin']
        print("pin: " + str(pin))
        GPIO.setup(pin, GPIO.OUT)


## GUI DEFINITIONS ##
mainWindow = tk.Tk()
mainWindow.title("LED Toggler")
myFont = tkfont.Font(family="Helvetica", size=12, weight="bold")

## EVENT FUNCTIONS ##


def dimLed(pin, duty, color):
    print(f"button pressed")
    print(f'pin: {pin}')
    print(f'duty: {duty}')
    if availableColors[color]['led'] == None:
        availableColors[color]['led'] = GPIO.PWM(pin, 100)
        availableColors[color]['led'].start(0)

    availableColors[color]['led'].ChangeDutyCycle(int(duty))


def close():
    # turn led off
    GPIO.cleanup()
    print("closing program")
    # exit program
    mainWindow.destroy()


availableColors = {
    'red': {
        'label': 'Red',
        'hexCode': "#ff0000",
        'value': 'red',
        'pin': 19,
        'led': None,

    }, 'blue': {
        'label': 'Blue',
        'hexCode': '#3944bc',
        'value': 'blue',
        'pin': 9,
        'led': None,
    },
    'green': {
        'label': 'Green',
        'hexCode': '#3cb043',
        'value': 'green',
        'pin': 10,
        'led': None,
    },

}

### WIDGETS ###

redSlider = tk.Scale(mainWindow, from_=0, to=100, orient='horizontal', activebackground='#ffaaaa', bg=availableColors['red']['hexCode'],
                     bd=0, command=lambda duty: dimLed(availableColors['red']['pin'], duty, 'red'), font=myFont, label=availableColors['red']['label']).grid()

greenSlider = tk.Scale(mainWindow, from_=0, to=100, orient='horizontal', activebackground='#ffaaaa', bg=availableColors['green']['hexCode'],
                       bd=0, command=lambda duty: dimLed(availableColors['green']['pin'], duty, 'green'), font=myFont, label=availableColors['red']['label']).grid()
blueSlider = tk.Scale(mainWindow, from_=0, to=100, orient='horizontal', activebackground='#ffaaaa', bg=availableColors['blue']['hexCode'],
                      bd=0, command=lambda duty: dimLed(availableColors['blue']['pin'], duty, 'blue'), font=myFont, label=availableColors['red']['label']).grid()


# for value in availableColors.values():
#     tk.Radiobutton(mainWindow, indicatoron=0, value=value['value'], text=value['label'], font=myFont,
#                    command=lambda: ledToggle(btn=value['value'], pin=2, currValue=sharedVariable.get()), bg=value['hexCode'], width=24).grid()


exitBtn = tk.Button(mainWindow, text="Exit", font=myFont,
                    command=close, bg="gray", width=24).grid()

mainWindow.protocol("WM_DELETE_WINDOW", close)

setup()
mainWindow.mainloop()
