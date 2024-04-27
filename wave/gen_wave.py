import numpy as np
from scipy.io.wavfile import write

rate = 44100
data = np.random.uniform(-1, 1, rate) # 1 second worth of random samples between -1 and 1
scaled = np.int16(data / np.max(np.abs(data)) * 32767)
write('test.wav', rate, scaled)

class cWaveSaver:
    
    def __init__(self) -> None:
        self.raw_data = None
        self.scaled_data = None

    def SetRawDataList(self, data: list):
        self.raw_data = np.array(data)
        raw_data = self.raw_data
        self.scaled_data = np.int16(32767 * raw_data/np.max(np.abs(raw_data)) )

    def SaveWave(self, file_name:str='default.wav'):
        rate = 44100
        write(file_name, rate, self.scaled_data)

def main():





    ws = cWaveSaver()
    data = np.random.uniform(-1, 1, rate)
    ws.SetRawDataList(data)
    ws.SaveWave('file.wav')

if __name__ == '__main__':
    main()