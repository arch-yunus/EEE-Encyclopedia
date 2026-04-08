# 📐 Donanım Tasarımı (Hardware Design)

Donanım tasarımı, teorik bir devrenin fiziksel, üretilebilir ve güvenilir bir ürüne dönüştürülme sürecidir. Bir "System Architect" için bu, sadece yolları çizmek değil, elektronların yüksek hızdaki davranışlarını (Signal Integrity) yönetmektir.

---

## 1. Şematik Tasarım (The Foundation)
Her şey iyi bir şematik ile başlar.
*   **Bileşen Seçimi:** Güç tüketimi, paket boyutu (footprint), bulunabilirlik (BOM management).
*   **Hiyerarşik Çizim:** Karmaşık sistemlerin (MCU, Power, Sensors) bloklar halinde ayrılması.
*   **Decoupling:** Güç girişlerine doğru kapasitör (100nF, 1uF vb.) yerleşimi şematik seviyesinde planlanmalıdır.

---

## 2. PCB Layout Stratejileri
Fiziksel tasarımda kurallar değişir.
*   **Katman Yönetimi (Stackup):** 2, 4 veya 8 katmanlı kartlarda sinyal ve ground plane yerleşimi. 
*   **Sinyal Bütünlüğü (Signal Integrity):** Empedans kontrollü yollar (örn: USB için 90 ohm diferansiyel çift).
*   **Termal Yönetim:** Yüksek akım geçen yolların genişletilmesi ve "Thermal Via" kullanımı.

---

## 3. EMI / EMC (Elektromanyetik Uyumluluk)
Tasarladığınız kartın hem dışarıya gürültü yaymaması hem de dışarıdaki gürültüden etkilenmemesi gerekir.
*   **Ground Plane:** Mümkünse kesintisiz bir toprak katmanı.
*   **Dönüş Yolları (Return Paths):** Akımın kaynağına dönerken izlediği yolun alanı ne kadar küçükse, radyasyon o kadar azdır.

---

## 4. Kullanılan Araçlar
*   **Altium Designer:** Endüstrideki lider, profesyonel çözüm.
*   **KiCad:** Güçlü, açık kaynaklı ve her geçen gün büyüyen alternatif.

> [!CAUTION]
> **Pro Tip:** PCB tasarımında "Vialar" (katmanlar arası geçiş delikleri) parazitik endüktans yaratır. Yüksek hızlı sinyallerde (örn: DDR bellek) via sayısını minimize etmezseniz, sinyal yansıma yapar ve sistem açılmaz.
