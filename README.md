# ASSRStimulus

Steps to run the stimulus and integrate with LSL stream:

Ensure you have the following installed on your machine:

1. Python3
2. Pip
3. PsychoPy
4. OpenBCI GUI
5. OpenBCI_LSL-master
6. pydub

Starting from a clean Ubuntu 20.04 setup, these are the commands to execute in order:

```
sudo apt-get install python3-pip
pip install psychopy
export PATH=/home/ubuntu/.local/bin:$PATH
pip install <path>/wxPython
```



Clone this repository and open navigate to it on PsychoPy.

```Setup an LSL stream using python openbci_lsl.py --stream```

If you get any port related errors, specify it manually using:

```python openbci_lsl.py [PORT] --stream```

Open FinalStimulus.py on PsychoPy coder and run it.


