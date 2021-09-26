# ASSRStimulus

Steps to run the stimulus and integrate with LSL stream:

Ensure you have the following installed on your machine:

1. Python3
2. Pip
3. PsychoPy
4. OpenBCI GUI
5. OpenBCI_LSL-master
6. pydub

If not previously installed, from a clean Ubuntu 20.04 setup, these are the commands to execute in order:

```
sudo apt-get install python3-pip
pip install psychopy
export PATH=/home/ubuntu/.local/bin:$PATH
```

Download the given wheel from [here](https://extras.wxpython.org/wxPython4/extras/linux/gtk3/)
```
pip install Downloads/wxPython-4.1.1-cp38-cp38-linux_x86_64.whl 
sudo apt-get install libusb-1.0-0-dev portaudio19-dev libasound2-dev
pip install psychtoolbox
```

Download Conda from official [website](https://docs.anaconda.com/anaconda/install/index.html) and:
```
sha256sum Anaconda3-2021.05-Linux-x86_64.sh 
bash Anaconda3-2021.05-Linux-x86_64.sh 
export PATH=/home/ubuntu/anaconda3/bin:$PATH

cd ASSRExp/
conda env create -n psychopy -f psychopy-env.yml
conda activate psychopy

conda init bash
conda activate psychopy
sudo apt-get install libwebkitgtk-1.0.0
```
(Might need to exachange the order of above two commands if it does not work on your machine)

```
pip install pydub
psychopy
(After your work, close PsychoPy and deactivate)
conda deactivate
```

More details on installing PsychoPy on Ubuntu and other platforms can be found [here](https://www.psychopy.org/download.html).

Clone OpenBCI_LSL-master form [Github](https://github.com/openbci-archive/OpenBCI_LSL)
```
cd OpenBCI_LSL-master/
pip install -r requirements.txt 

(If you get an error, run the command below. After that remove numpy and scipy from requirements.txt manually and rerun the command above)
python -m pip install --user numpy scipy matplotlib ipython jupyter

```
If not previously done, ensure your path is correct:
```export PATH=/home/ubuntu/.local/bin:$PATH```

Now, download and install OpenBCI_GUI standalone [app](https://openbci.com/downloads) and in its directory, run
```./OpenBCI_GUI ```

Go to OpenBCI_LSL-master/ and run
```python openbci_lsl.py --stream```

If you get any port related errors, specify it manually using:

```
python openbci_lsl.py [PORT] --stream
```


Now, clone this repository and open it on PsychoPy coder's file navigation pane.

Open ```FinalStimulus.py``` on PsychoPy coder by double clicking it and run it.

## Updates incoming:

Full LSL stream integration and saving skipped trials and their timestamps in a CSV.
