import PySimpleGUI as sg
import os
import time
import threading

sg.theme("DarkAmber")


def run(window, delay): 
    with open("./words_list.txt", "r") as file:
        for line in file.readlines():
            try:
                with open("./words_list-used.txt", "r") as output_file:
                    if line in output_file.readlines():
                        continue
            except:
                pass
            with open("./words_list-used.txt", "a") as output_file:
                line_n = line.replace('\n', '')
                t = threading.currentThread()
                if not getattr(t, "do_run", True):
                    break
                window.write_event_value('-THREAD UPDATE-', line_n)

                import pyaudio
                import wave

                filename = line_n + '.wav'
                chunk = 1024
                FORMAT = pyaudio.paInt16
                channels = 1
                sample_rate = 44100
                record_seconds = delay+1
                p = pyaudio.PyAudio()
                stream = p.open(format=FORMAT,
                                channels=channels,
                                rate=sample_rate,
                                input=True,
                                output=True,
                                frames_per_buffer=chunk)
                frames = []
                window.write_event_value('-STATUS UPDATE-', 'RECORDING')
                for i in range(int(44100 / chunk * record_seconds)):
                    data = stream.read(chunk)
                    frames.append(data)
                window.write_event_value('-STATUS UPDATE-', 'FINISHED RECORDING')
                stream.stop_stream()
                stream.close()
                p.terminate()
                wf = wave.open(filename, "wb")
                wf.setnchannels(channels)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(sample_rate)
                wf.writeframes(b"".join(frames))
                wf.close()
                output_file.write(line)
    window.write_event_value('-THREAD UPDATE-', 'KONIEC')

def start_flashing(delay):
    t = threading.Thread(target = run, args =(window,delay, ), daemon=True) 
    t.start() 
    return t

def stop_flashing(t):
    # Signal termination 
    t.do_run = False


layout = [
        [sg.Text("Words to Flash here", key="-WORD-", size=(30,5)), sg.VSep(), sg.Text("...", key="-STATUS-", size=(30,5))],
        [sg.Button('Go'),sg.Button('Stop'), sg.Button('Nothing'), sg.Button('Exit')],
        [ sg.Text("Seconds"), sg.Slider(range=(1,5), orientation="horizontal", key="-DELAY-") ],
]

window = sg.Window('Window Title', layout)


while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        t = start_flashing(values["-DELAY-"])
    elif event == 'Stop':
        stop_flashing(t)
    elif event == 'Nothing':
        print('nic')
    elif event == '-STATUS UPDATE-':
        try:
            print(values['-STATUS UPDATE-'])
            window["-STATUS-"].update(values['-STATUS UPDATE-'])
        except:
            print("wtf")
    elif event == '-THREAD UPDATE-':
        try:
            print(values['-THREAD UPDATE-'])
            window["-WORD-"].update(values['-THREAD UPDATE-'])
        except:
            print("wtf")
    else:
        #  print(event, values)
        pass
window.close()
