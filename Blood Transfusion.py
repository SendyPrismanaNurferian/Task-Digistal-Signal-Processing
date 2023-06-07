import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = pd.read_csv('transfusion.csv')

# Mengambil sinyal EMG untuk transfusi darah normal
normal_data = data["Monetary (c.c. blood)"]

# Fungsi untuk melakukan pemulusan (smoothing) pada sinyal
def smooth_signal(signal, window_size):
    smoothed_signal = np.convolve(signal, np.ones(window_size)/window_size, mode='same')
    return smoothed_signal

# Menentukan ukuran jendela (window size) untuk pemulusan
window_size = 10

# Menstabilkan sinyal EMG untuk tekanan darah normal
smoothed_signal = smooth_signal(normal_data, window_size)

# Menampilkan sinyal asli dan sinyal yang sudah distabilkan
plt.figure(figsize=(12, 6))
plt.plot(normal_data, label='Original Signal')
plt.plot(smoothed_signal, label='Smoothed Signal')
plt.xlabel('Sample (Time)')
plt.ylabel('EMG Signal')
plt.title('Stabilizing EMG Signal for Normal Blood Transfusion using Adaptive Filter')
plt.legend()
plt.show()