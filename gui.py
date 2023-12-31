# PaperPixLive GUI Test
#
import PySimpleGUI as sg
from subprocess import Popen, DEVNULL

layout = [
    [sg.Text("action" , key="-ACTION-")],
    [sg.Button("StartBond", size=(15,4)),sg.Button("StopBond",size=(15,4))],
    [sg.Button("Reset 4G",size=(15,4)), sg.Button("Update",size=(15,4))],
    [sg.Button("QUIT")]
]

# Create the Window
window = sg.Window('PaperPixLive', layout, size=(320,240))
# Event Loop to process "events"
while True:
    event, values = window.read()
    window['action'].Update(event) 
    print(event,values)
    if event in ("-ACTION-"):
        Popen(["ls", "-la"], stdout=DEVNULL) #TODO: Use actual cmd
    if event in (None, 'QUIT'):
        break
window.close()
