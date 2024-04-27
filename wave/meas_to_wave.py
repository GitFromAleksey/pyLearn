import json
from gen_wave import cWaveSaver




def main():

    with open('MEAS_71_S_5.txt.json', 'r') as jf:
        content = jf.read()
        j = json.loads(content)
        jf.close()

    data = j[9]['A(A)']

    ws = cWaveSaver()
    # data = np.random.uniform(-1, 1, rate)
    ws.SetRawDataList(data)
    ws.SaveWave('A(A).wav')

if __name__ == '__main__':
    main()