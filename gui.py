# PaperPixLive GUI Test
#
import PySimpleGUI as sg
#proc=Popen(["ls","-la"])

layout = [ [sg.Text("action" , key="action")],
           [sg.Button("StartBond", size (15,4)),sg.Button("StopBond",size=(15,4))],
           [sg.Button("USBRESET",size=(15,4)), sg.Button("NMAP",size=(15,4))],
           [sg.Button("QUIT")]          ]
# Create the Window
window = sg.Window('PaperPixLive', layout, size=(320,240))
# Event Loop to process "events"
while True:
    event, values = window.read()
    window['action'].Update(event) 
    print(event,values)
    if event in (None, 'QUIT'):
        break
window.close()
