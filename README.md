This is a simple program that flashes words and records with your default mic. 
You can run word_flasher.exe. You need file named words_list.txt in the same folder as word_flasher.exe is launched it has to contain words that you want the program to flash (separate words with new lines like in the example given).

If you want to run this as a script:

You need Python 3, PySimpleGUI and PyAudio to run this. Use following to install these libraries after you have installed Python 3.

```bash
pip install pysimplegui pyaudio
or
python -m pip install pysimplegui pyaudio
```

If you have troube installing pyaudio try it with pipwin

```bash
pip install pipwin
# Add pipwin to PATH as prompted during install
pipwin install pyaudio
```

Screenshot of Qt version (contact me for this version):

* Linux:

![ Linux ]( https://raw.githubusercontent.com/gnapiorkowski/word_flasher/master/screen.png )

* Widnows:

![ Windows ]( https://raw.githubusercontent.com/gnapiorkowski/word_flasher/master/screen2.png )
