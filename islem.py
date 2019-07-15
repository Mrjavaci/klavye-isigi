import pyaudio
import numpy as np
import os

CHUNK = 2**11

# Hertz muhabbeti
RATE = 44100

#PyAudio sinifini calistiriyorum
p=pyaudio.PyAudio()

# Varsayilan giris cihazini kullanmak icin
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)


while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    #donen veriyi bolme islemi
    v = int(50*peak/2**16)

    # aldigim veriyi print ediyorum.
    print(v)
    #### EN AZ 0 EN FAZLA 30 GORDUM. GELISTIRILICEKSE BU SEKILDE GELISTIRILEBILIR
    if v == 0:
        os.system("./kbrightness 0")
    
    elif v < 8 and v > 0:
        os.system("./kbrightness 0.5")

    else:
        os.system("./kbrightness 1")

stream.stop_stream()
stream.close()
p.terminate()
#hadi-eyw
