# 📡 Sinyaller ve Sistemler: Frekansların Mimari Dansı

Donanımda var olan fiziksel dünya (sensör akımları, gürültülü voltaj dalgalanmaları), kontrol algoritmalarımız (örneğin otonom bir sistemdeki PID) tarafından değerlendirilmeden önce soyutlanmak zorundadır. Sinyaller Zaman (Time-Domain) uzayını, Sistemler ise bu sinyalleri deforme eden mimari filtreleri (Frequency-Domain) temsil eder.

---

## 1. Lineer Zamanla Değişmeyen (LTI) Sistemler

Sistem mimarları, çevre sistemlerini (motorlar, filtreler) matematiksel öngörülebilirliği olduğu için LTI (Linear Time-Invariant) olarak zorlar veya o bölgeye linearize ederler.
*   **Duyarsızlık (Time Invariant):** $y(t) = S[x(t)]$ ise, $y(t-t_0) = S[x(t-t_0)]$.
*   **Doğrusallık (Linearity):** Süperpozisyon geçerlidir. $S[ax_1(t) + bx_2(t)] = a S[x_1(t)] + b S[x_2(t)]$.

### Konvolüsyon (Convolution)
Sinyaller Zaman düzleminde sadece birbirleriyle girişim yaparak (katlanıp kaydırılarak) LTI sistemden çıkarlar: 
$$ y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau $$
*   $x(t)$ : Giriş sinyali (örn. Lidar'dan gelen raw veri)
*   $h(t)$ : Sistemin İmpuls Cevabı (Sisteme Dirac Delta impulsı vurulduğundaki çınlama karakteristiği)
*   $y(t)$ : Çıkış sensör verisi.

---

## 2. Fourier Dönüşümleri (CTFT / DTFT)

*"Herhangi bir kompleks sinyal, sonsuz sayıdaki temel sinüs ve kosinüs dalgalarının matematiksel birleşimidir."*

Zaman uzayında okyanus dalgaları gibi bozuk duran bir radar sinyalini (veya EKG sinyalini), Frekans uzayına geçirip içindeki spesifik 50Hz şebeke gürültüsünü (Noise) cımbızla çekerek koparmak için Fourier tek yöntemdir.

$$ X(j\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} dt $$

**Endüstriyel Pratik:** Gömülü sistemlerde (Örn. STM32 ile spektrum analizi yaparken) sürekli zamanı analitik olarak integrale dökmek CPU'yu dondurur. Bu yüzden **Fast Fourier Transform (FFT)** kullanırız! Cortex-M4/M7 işlemciler, donanımsal FPU (Kayan Nokta Ünitesi) ile sadece ayrık zamanlı sinyallerin ($x[n]$) matris işlemlerini saniyede milyonlarca kez yaparak gerçek zamanlı Spektrum analizi sunar.

---

## 3. Laplace Dönüşümü (S-Domain) ve Kontrol Kararlılığı

Fourier'in aksine Laplace, sistemlerin "Kararlılığını" (Stability) inceler. Bir sisteme üstel çarpan ($e^{-\sigma t}$) katarak sonsuza ıraksamasını matematikte engelleriz. Kompleks düzlem $s = \sigma + j\omega$ olarak formüle edilir.

$$ X(s) = \int_{0}^{\infty} x(t) e^{-st} dt $$

### S-Plane, Kutuplar (Poles) ve Sıfırlar (Zeros)
Transfer fonksiyonundaki paydanın kökleri **Kutuplardır**. Denklemin sıfıra gittiği yerler **Sıfırlardır**.

*   Kutuplar S-Düzleminde **SAĞ TARAFA** devrilirse, sistem enerjisini atamaz kararsız (Unstable) hale gelir (Otonom drone havada takla atarak düşer).
*   Kutuplar İmajiner ($j\omega$) eksene tam oturursa, sistem saf osilasyon yapar.
*   Kutuplar S-Düzleminin **SOLUNDA** ($-\sigma$) ise, sistem dengeli bir şekilde başlangıç noktasına geri döner - Kontrol teorisinde Mükemmel PID mimarisinin nihai tasarımı sol yarı düzleme yerleşimdir!
