# 🧪 Devre Simülasyonu: Digital Twin Yaklaşımı

Donanım üretimi pahalı ve zaman alan bir süreçtir. "First-Time-Right" (ilk seferde doğru) tasarımı için simülasyon bir zorunluluktur.

---

## 1. SPICE (Simulation Program with Integrated Circuit Emphasis)

SPICE, 1970'lerden beri tüm devre simülatörlerinin kalbidir. Devreyi düğüm matrisleri (Nodal Analysis) üzerinden çözer.

### Temel Analiz Türleri:
1.  **Transient (.TRAN):** Zaman düzleminde sinyal dalga formları (Osiloskop görünümü).
2.  **AC Analysis (.AC):** Frekans cevabı (Bode plot), kazanç ve faz.
3.  **DC Sweep (.DC):** Bir kaynağın değeri değiştikçe devrenin statik tepkisi.
4.  **Monte Carlo:** Komponent toleranslarının (örn: %5 direnç hatası) seri üretimde devreyi nasıl bozacağını simüle etmek.

---

## 2. Araçlar

*   **LTspice (Analog Devices):** Ücretsiz, hızlı ve endüstri standardı olan en popüler simülatör.
*   **PSpice (Cadence):** Daha profesyonel, kapsamlı kütüphaneler sunan ücretli çözüm.
*   **Proteus:** Mikrodenetleyici (MCU) kodlarını ve devreyi aynı anda simüle edebilen popüler eğitim aracı.

---

## 3. Modelleme Hataları ve Gerçeklik

Simülasyon mükemmel değildir. Genelde "ideal" komponentler kullanılır.

> [!WARNING]
> **Architect Insight:** Simülasyonda 1GHz'de çalışan bir devreniz gerçek hayatta çalışmayabilir. Çünkü simülasyona PCB yollarının parazitik kapasitansı ve endüktansını (Parasitic Extraction) eklemezseniz, "Digital Twin" kopyanız gerçeği yansıtmaz. Karmaşık tasarımlarda **Post-Layout Simulation** hayat kurtarır.
