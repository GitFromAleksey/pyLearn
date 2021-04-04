# -*- coding: utf-8 -*-
import os
import sys
import time
import wave
import struct
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME_READ = 'Ring09.wav'
FILE_NAME_WRITE = '_' + FILE_NAME_READ

types = {
    1:np.int8,
    2:np.int16,
    4:np.int32
    }

## -----------------------------------------------------------------------------
def main(argv):
    print(argv)

    print(wave.__file__)

    wav = wave.open(FILE_NAME_READ, mode='rb')
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    print('nchannels:', nchannels)
    print('sampwidth:', sampwidth)
    print('framerate:', framerate)
    print('nframes:', nframes)
    print('comptype:', comptype)
    print('compname:', compname)

    content = wav.readframes(nframes)
    wav.close()
        
    samples = np.fromstring(content, dtype=types[sampwidth])

    channels = []
    for n in range(nchannels):
        channel = samples[n::nchannels]
        channels.append(channel)
        print(type(channel))
        fig, axes = plt.subplots()
        axes.plot(channel)
    fig, axes = plt.subplots()
    mono = channels[1]+channels[0]
    Amax = np.amax(np.absolute(mono))
    coef = 32767/Amax
    print('coef:',coef)
    mono = mono*coef
    print('Amax:',Amax)
    axes.plot(mono)

    wav_write = wave.open(FILE_NAME_WRITE, 'w')
    wav_write.setnchannels(1)
    wav_write.setsampwidth(sampwidth)
    wav_write.setframerate(framerate)
    for h in mono:
        wav_write.writeframesraw(struct.pack('<h', int(h)))
    wav_write.close()

    plt.show()
    
    return sys.exit(0)
## -----------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv)
