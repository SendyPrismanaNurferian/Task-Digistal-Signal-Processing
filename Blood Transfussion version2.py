#Perlu diperbaiki untuk mencari cutt off maka untuk mencari signal yang cut off seperti ini:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as signal

# Membaca data dari file CSV
data = pd.read_csv('transfusion.csv')

# Mengambil sinyal EMG untuk tekanan darah normal
normal_data = data["Monetary (c.c. blood)"]

# Fungsi untuk melakukan pemulusan (smoothing) pada sinyal
def smooth_signal(signal, window_size):
    smoothed_signal = np.convolve(signal, np.ones(window_size)/window_size, mode='same')
    return smoothed_signal

# Menentukan ukuran jendela (window size) untuk pemulusan
window_size = 10

# Menstabilkan sinyal EMG untuk tekanan darah normal
smoothed_signal = smooth_signal(normal_data, window_size)

# Menghitung cut-off frequency menggunakan metode Nyquist
sampling_rate = 1000  # Frekuensi sampling dalam Hz
nyquist_frequency = sampling_rate / 2
cut_off_frequency = 100  # Frekuensi cut-off dalam Hz
normalized_cut_off = cut_off_frequency / nyquist_frequency

# Menghitung panjang estimasi FIR filter menggunakan metode Kaiser
attenuation = 60  # Reduksi amplitudo (dB) pada daerah stopband
transition_width = 10  # Lebar transisi antara daerah passband dan stopband (Hz)

# Menggunakan formula Kaiser untuk mengestimasi panjang filter
filter_length = signal.kaiserord(attenuation, transition_width / nyquist_frequency)

print("Cut-off frequency:", cut_off_frequency, "Hz")
print("Estimation FIR filter length:", filter_length)

# Menampilkan sinyal asli dan sinyal yang sudah distabilkan
plt.figure(figsize=(12, 6))
plt.plot(normal_data, label='Original Signal')
plt.plot(smoothed_signal, label='Smoothed Signal')
plt.xlabel('Sample (Time)')
plt.ylabel('EMG Signal')
plt.title('Stabilizing EMG Signal for Normal Blood Transfusion using Adaptive Filter')
plt.legend()
plt.show()
