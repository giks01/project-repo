import FreeSimpleGUI as sg
from feet_meters import get_meters

feet_label = sg.Text("Enter Feet")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter Inches")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output1 = sg.Text(key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output1]])
while True:
    events, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result =get_meters(feet, inches)
    window["output"].update(value=f"{result}m", text_color = 'blue')
    if events == sg.WIN_CLOSED:
        break


window.close()