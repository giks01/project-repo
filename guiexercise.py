import FreeSimpleGUI as sg
from FreeSimpleGUI import theme
from feet_meters import get_meters

sg.theme("Black")

feet_label = sg.Text("Enter Feet")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter Inches")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output1 = sg.Text(key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                    layout=[[feet_label, feet_input],
                            [inches_label, inches_input],
                            [button, exit_button, output1]])

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == "Exit":
        break

    try:
        feet = float(values["feet"])
        inches = float(values["inches"])

        result =get_meters(feet, inches)
        window["output"].update(value=f"{result}m", text_color = 'white')
    except ValueError:
        sg.popup("Please provide input", font=('Helvetica', 10))

window.close()
