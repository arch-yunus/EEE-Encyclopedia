"""
Python for EEE - Mühendislik Uygulamaları Başlangıç Kütüphanesi

Bu script, gömülü sistemler, sinyal işleme ve veri analizi süreçlerinde 
kullanılacak temel Python fonksiyonlarını barındıracaktır.
"""

def ohm_yasasi_akim_hesapla(gerilim_v, direnc_ohm):
    """
    Ohm yasasına göre akım değerini hesaplar. (I = V / R)
    """
    if direnc_ohm == 0:
        raise ValueError("Direnç 0 olamaz. Kısa devre hatası!")
    return gerilim_v / direnc_ohm

if __name__ == "__main__":
    v = 5.0
    r = 220.0
    i = ohm_yasasi_akim_hesapla(v, r)
    print(f"Gerilim: {v}V, Direnç: {r} ohm => Akım: {i*1000:.2f} mA")
