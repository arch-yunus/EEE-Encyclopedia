import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

"""
EE-Encyclopedia: Mühendislik Simülasyonu Örneği
Sinyal İşleme ve RLC Filtre Tepkisi Analizi
"""

def generate_noisy_signal(t, freq=50):
    """50Hz bir sinyal ve rastgele gürültü üretir."""
    clean = np.sin(2 * np.pi * freq * t)
    noise = 0.5 * np.random.normal(size=t.shape)
    return clean + noise

def apply_lowpass_filter(data, cutoff, fs, order=4):
    """Butterworth Alçak Geçiren Filtre uygular."""
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return signal.filtfilt(b, a, data)

if __name__ == "__main__":
    # Parametreler
    fs = 1000  # Örnekleme frekansı (1kHz)
    T = 0.2    # Süre (200ms)
    t = np.linspace(0, T, int(T*fs), endpoint=False)
    
    # 1. Ham Sinyal Üretimi
    signal_raw = generate_noisy_signal(t)
    
    # 2. Filtreleme (Cutoff = 80Hz)
    signal_filtered = apply_lowpass_filter(signal_raw, cutoff=80, fs=fs)
    
    print("Simülasyon Tamamlandı: Gürültülü sinyal filtreleme algoritması çalıştırıldı.")
    
    # Görselleştirme (Eğer grafik destekli bir ortamdaysanız)
    # plt.plot(t, signal_raw, label='Noisy Signal')
    # plt.plot(t, signal_filtered, label='Filtered (80Hz LP)', linewidth=2)
    # plt.legend()
    # plt.show()
