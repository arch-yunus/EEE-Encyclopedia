# 🔬 High-Speed PCB Design Masterclass: Sinyal ve Güç Bütünlüğü (SI & PI)

> *"Bir devreyi protoboard'da çalıştırmak kolaydır; GHz frekanslarında, EMC testleri geçerken çalıştırmak mühendisliktir."*

---

## 1. İletim Hattı Teorisi (Transmission Line Theory)

Sinyalin yayılma hızı kesinlikle sonsuzdur ve PCB hattının uzunluğu artık ihmal edilemez. **Bir PCB hattı, boyutunun sinyalin dalga boyunun ($\lambda$) $\approx 1/10$'una ulaştığında artık bir iletim hattıdır.**

$$\lambda = \frac{v_p}{f} = \frac{c / \sqrt{\epsilon_r}}{f}$$

FR4 dielektriği için ($\epsilon_r \approx 4.5$): 1 GHz'de $\lambda \approx 14\text{ cm}$. 1.4 cm uzunluğundaki herhangi bir hat iletim hattı davranışı sergiler.

### Karakteristik Empedans ($Z_0$)
Sonsuz uzunlukta bir iletim hattının göreceği empedans:

$$Z_0 = \sqrt{\frac{L'}{C'}}$$

*Burada $L'$ ve $C'$ birim uzunluk başına seri endüktans ve paralel kapasitanstır.*

**Microstrip İçin:**
$$Z_0 = \frac{87}{\sqrt{\epsilon_r + 1.41}} \ln\left(\frac{5.98h}{0.8w + t}\right)$$

*$h$ = dielektrik kalınlığı, $w$ = hat genişliği, $t$ = bakır kalınlığı*

Bu formülü çözerek: 50Ω hat için FR4 üzerinde standart bir stackup'ta $w \approx 2h$ çıkar.

---

## 2. Yansıma ve Sonlandırma (Reflection & Termination)

Bir iletim hattının sonunda yük empedansı ($Z_L$) hat empedansına ($Z_0$) eşit değilse, enerji kaynağa geri yansır. Yansıma katsayısı ($\Gamma$):

$$\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}$$

| Durum | $\Gamma_L$ | Etki |
|---|---|---|
| Açık devre ($Z_L = \infty$) | +1 | Sinyal 2 katına yükselerek yansır |
| Kısa devre ($Z_L = 0$) | -1 | Sinyal ters polaritede yansır |
| Uyumlu yük ($Z_L = Z_0$) | 0 | Yansıma yok, mükemmel transfer |

### Sonlandırma Stratejileri
- **Seri Sonlandırma:** Kaynak yanına $R_{series} = Z_0 - Z_{driver\_output}$ eklenir. Ucuz, tek yönlü hatlarda kullanılır.
- **Paralel (Shunt) Sonlandırma:** Alıcı yanına $R_{shunt} = Z_0$ eklenir. Güç harcar ama çift yönlü (point-to-point) DDR için standarttır.
- **Thevenin Terminasyon:** $R_1$ ile $V_{CC}$, $R_2$ ile GND arasında gerilim bölücü. DC bias ve empedans uyumu aynı anda sağlanır.

---

## 3. Diferansiyel Çiftler: LVDS ve USB 3.0

Yüksek hızlı veriler (USB, HDMI, SERDES, DDR) diferansiyel çiftlerle taşınır. İki hat arasındaki gerilim farkı ($V^+ - V^-$) sinyali taşır; bu sayede ortak mod gürültü (common-mode noise) etkisizleşir.

### Kritik Tasarım Kuralları
1. **Impedance Control:** LVDS için 100Ω diferansiyel (her hat 50Ω), USB 3.0 için 90Ω diferansiyel.
2. **Length Matching (Skew):** İki hat arasındaki uzunluk farkı toleransı frekansta $\Delta t$ zaman kaymasına yol açar. DDR4 veri hatlarında bu tolerans genellikle $<10 \text{ mil}$ ($<0.254\text{ mm}$) olarak sınırlandırılır.
3. **Serpentine Routing:** Uzun hattı kısaltmak yerine kısa hattı "yılan gibi" kıvrarak uzatmak. Ancak serpentin kıvrımlarının açıklığı kıvrım endüktansını etkiler.

---

## 4. Power Delivery Network (PDN) Tasarımı

İşlemcinin güç pini, bir iletim hattı değil, **rezonans yapabilen bir RLC ağıdır**.

PDN hedef empedansı şu formülle belirlenir:
$$Z_{target} = \frac{V_{dd} \cdot \text{ripple\%}}{I_{max}}$$

Örneğin 3.3V bir işlemci, %3 ripple toleransıyla 2A ani akım çekiyorsa:
$$Z_{target} = \frac{3.3 \times 0.03}{2} = 49.5\text{ m}\Omega$$

**Bypas Kapasitör Seçiminin Frekans Dağılımı:**

| Kapasitör Türü | Değer | Frekans Bölgesi |
|---|---|---|
| Bulk Alüminyum Elektrolitik | 220µF | < 1 MHz |
| Seramik MLCC (0805/0603) | 10µF | 1–50 MHz |
| Seramik MLCC (0402/0201) | 100nF | 50 MHz–500 MHz |
| IC Paketi Kapasitörü | 10–100nF | > 500 MHz |

> [!WARNING]
> **Rezonans Tuzağı:** Birden fazla kapasitör türü paralel bağlandığında, aralarında anti-rezonans (Anti-Resonance Peak) oluşabilir. Bu frekans noktasında PDN empedansı beklenmedik şekilde yükselir. VRM (Voltage Regulator Module) tasarımında MLCC kapasitörlerini seçerken ESL (Eşdeğer Seri Endüktans) değerleri dikkatlice analiz edilmelidir.

---

## 5. EMI / EMC Uyumluluk Mühendisliği

Tasarımınızın CE (Avrupa) veya FCC (ABD) sertifikası alabilmesi için belirlenen sınırların (CISPR 22, EN55032) altında elektromanyetik emisyon üretmesi gerekir.

### EMI'nın Kaynağı: Diferansiyel ve Ortak Mod Emisyonu
- **Diferansiyel Mod (DM):** Gidip gelen akımın oluşturduğu döngü alanı. PCB return path alanı azaltılarak baskılanır.
- **Ortak Mod (CM):** Şasi ve yeşil hat arasındaki kaçak akım. Ortak mod bobin (CMC) ile filtrelenir.

### EMI Mühendisinin Araç Kutusu
1. **Kesintisiz Ground Plane:** Sinyalin altında her zaman eksiksiz bir referans düzlemi olmalı.
2. **Kritik Döngü Alanını Daraltmak:** $A_{döngü} \downarrow \Rightarrow \text{Anten Kazancı} \downarrow \Rightarrow \text{Radyasyon} \downarrow$
3. **Guard Ring:** Yüksek empedanslı analog hatların etrafına yerleştirilen toprak çiti, yüksek hızlı dijital sinyallerin alan etkisini engeller.

> [!IMPORTANT]
> **Sertifikasyon Stratejisi:** Bir ürünü EMC testine göndermeden önce tasarım aşamasında "Pre-Compliance Test" yapmak zorundasınız. Bir LISN (Line Impedance Stabilization Network) ve geniş bant EMI alıcısı ile kendi laboratuvarınızda ölçüm yapabilirsiniz. Son anda tespit edilen EMI sorunu tüm PCB'nin yeniden tasarımına yol açabilir.
