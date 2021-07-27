# Installing this package (Mac/Linux)
To install this package and its dependencies in a new conda environment, simply run:
```shell
conda create -n week1 python=3.8
conda activate week1

(week1) pip install -e cogworks_week1
```
It is important that you use this `develop` install option, as the microphone configuration requires that
this package is installed in-place.

# Installing this package (PC)
To install this package and its dependencies in a new conda environment, simply run:
```shell
conda create -n week1 python=3.8 ipython jupyter notebook numpy scipy matplotlib pyaudio numba
conda install -n week1 -c conda-forge librosa ffmpeg
conda activate week1

(week 1) pip install -e cogworks_week1
```

# Configuring Your Microphone

Now we will configure `microphone` to use the appropriate microphone on your computer.
Open the iPython console by running 'python', then run:
```python
from microphone import configure_input
configure_input()
```
and follow the selection prompt. This will save your microphone preference for future use. The resulting configuration file will be saved to `Microphone/microphone/config.ini`.
The contents of the file will look something like this

```
[input device]
name = Desktop Microphone (RØDE NT-USB)
index = 1
```

You can edit [this file](https://github.com/CogWorksBWSI/Microphone/blob/master/microphone/config.py) to change the recording settings (e.g. the sampling rate) used to sampled audio from your microphone.

# Testing Your Microphone
Open the iPython console by running 'python', then run:
```python
from microphone import test_input
test_input()
```
This should record and play back a brief audio clip using the microphone selected during configuration.

# Recording Audio
```python
from microphone import record_audio

# Record 10 seconds of audio
byte_encoded_signal, sampling_rate = record_audio(10)
```

# Playing Audio
```python
from microphone import play_audio

# Play 10 seconds of audio
play_audio(byte_encoded_signal, 10)
```
