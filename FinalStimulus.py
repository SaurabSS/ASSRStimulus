import sys
from psychopy import sound, core, event, gui
from psychopy import visual
#from pydub import AudioSegment
#from pydub.playback import play
import random
from pydub import AudioSegment

print('Using %s (with %s) for sounds' % (sound.audioLib, sound.audioDriver))

expInfo = {'Observer':'Your Name', 'Volunteer Name':'Burdell', 'Pure Tone Duration (s)' : 3, 'Dual Tone Duration (s)':6,'Volume (0-100)':25}

dlg = gui.DlgFromDict(expInfo, title='ASSR')
if dlg.OK:
    print("continuing to the Experiment")
else:
    core.quit()

win = visual.Window([1280,700],allowGUI=True,
                    monitor='testMonitor', units='deg')

circle = visual.Circle(win=win, radius=1, pos=[0,0], fillColor=[1.0,1.0,1.0], colorSpace='rgb')
circle.draw()
win.flip()

for i in range(0,5):
    sound1 = AudioSegment.from_file("a4-40.wav")
    sound2 = AudioSegment.from_file("b5-35.wav")
    sound3 = AudioSegment.from_file("cs6-75.wav")
    sound4 = AudioSegment.from_file("f5-17.wav")
    sound5 = AudioSegment.from_file("g6-23.wav")

    soundFile1 = "a4-40.wav"
    soundFile2 = "b5-35.wav"
    soundFile3 = "cs6-75.wav"
    soundFile4 = "f5-17.wav"
    soundFile5 = "g6-23.wav"

    
    listSoundWavs = [sound1, sound2, sound3, sound4, sound5]
    listSoundFiles= [soundFile1, soundFile2, soundFile3, soundFile4, soundFile5]
    listIndices = range(1,5)
    pick1 = random.choice(listIndices)
    pick2 = random.choice(listIndices)
    
    fSound1 = listSoundWavs[pick1]
    fSound2 = listSoundWavs[pick2]
    fSoundFile1 = listSoundFiles[pick1]
    fSoundFile1 = listSoundFiles[pick2]
    
    
    while(abs(pick2-pick1)<2):
        pick2 = random.choice(listIndices)
    
    if pick1<pick2:
        lowerInd = sound1 
    else:
        lowerInd = sound2
    
    combined = sound1.overlay(sound2)
    combined.export("combined.wav", format='wav')
        
    message = visual.TextStim(win, pos=[0,+3],text='This is the sound you need to focus on.')
    message.draw()
    circle = visual.Circle(win=win, radius=1, pos=[0,0], fillColor=[1.0,1.0,1.0], colorSpace='rgb')
    circle.draw()
    win.flip()

    hello = sound.Sound(fSoundFile1, stopTime=expInfo['Pure Tone Duration (s)']) 
    hello.play()
    core.wait(expInfo['Pure Tone Duration (s)'])

    message = visual.TextStim(win, pos=[0,+3],text='Press any key to continue')
    message.draw()
    win.flip()
    event.waitKeys()

    circle = visual.Circle(win=win, radius=1, pos=[0,0], fillColor=[1.0,1.0,1.0], colorSpace='rgb')
    circle.draw()
    win.flip()

    hello = sound.Sound('combined.wav', stopTime=expInfo['Dual Tone Duration (s)']) 
    hello.play()
    core.wait(expInfo['Dual Tone Duration (s)'])


    message = visual.TextStim(win, pos=[0,+3],text='''If you want to skip the last trial, press spacebar in 3 seconds''')
    message.draw()
    win.flip()
    while(core.wait(3)):
        event.waitKeys()


if sys.platform == 'win32':
    ding = sound.Sound('ding')
    ding.play()

    core.wait(1)

    tada = sound.Sound('tada.wav')
    tada.play()

    core.wait(2)
print('done')

core.quit()
