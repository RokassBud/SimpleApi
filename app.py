import tkinter as tk
import sounddevice as sd
#from scipy.io.wavfile import write

def recording():
    if(button['text'] == 'Record'):
        button['text'] = 'Stop'
        # ac = True
    else:
        button['text'] = 'Record'
    #
    # while(ac == True):
    #     fs = 44100
    #     sd.rec(samplerate=fs,channels=2)




window = tk.Tk()
window.title('Recorder')
window.geometry('300x200')
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

button = tk.Button(window,
                   text='Record',
                   command=recording)
button.place(x=125,y=75)

window.mainloop()

