import sys
from psychopy import sound, core, event, gui
from psychopy import visual
#from pydub import AudioSegment
#from pydub.playback import play
import random

print('Using %s (with %s) for sounds' % (sound.audioLib, sound.audioDriver))

expInfo = {'Observer':'Your Name', 'Volunteer Name':'Burdell', 'Pure Tone Duration (s)' : 6, 'Dual Tone Duration (s)':10,'Volume (0-100)':25}

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
    message = visual.TextStim(win, pos=[0,+3],text='This is the sound you need to focus on.')
    message.draw()
    circle = visual.Circle(win=win, radius=1, pos=[0,0], fillColor=[1.0,1.0,1.0], colorSpace='rgb')
    circle.draw()
    win.flip()

    hello = sound.Sound('b5-35.wav', secs=expInfo['Pure Tone Duration (s)']) if(i%2) else sound.Sound('cs6-75.wav')
    hello.play()
    core.wait(expInfo['Pure Tone Duration (s)'])

    message = visual.TextStim(win, pos=[0,+3],text='Press any key to continue')
    message.draw()
    win.flip()
    event.waitKeys()
    circle = visual.Circle(win=win, radius=1, pos=[0,0], fillColor=[1.0,1.0,1.0], colorSpace='rgb')
    circle.draw()
    win.flip()
    
    hello = sound.Sound('mix12.wav') if(i%2) else sound.Sound('mix13.wav')
    hello.setVolume(2)
    hello.play()
    core.wait(expInfo['Dual Tone Duration (s)'])

    message = visual.TextStim(win, pos=[0,+3],text='''Could you focus on it? Press '\Y\' or \'N\' ''')
    message.draw()
    win.flip()
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
