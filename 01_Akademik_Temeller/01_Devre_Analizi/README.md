# ⚡ Devre Analizi: Lineer Sistemlerin Temelleri

Bu kütüphane sıradan bir "vizeye hazırlık" notu değildir. Elektronların hareketini yönlendirme ve devasa enerji akışlarını matematiksel bir zarafetle kontrol altına alma sanatıdır. Modern bir RF kartından (PCB), bir otonom robotun motor sürücüsüne kadar her sistemin kalbinde bu yasalar çalışır.

## 1. Düğüm ve Çevre (Nodal & Mesh) Analizi: Sistemik Matris Yaklaşımı

Devreyi ilkel (tek tek denklem çözme) yaklaşımlarla çözmek yerine, endüstriyel standartta **durum matrisleri (state matrices)** kurarak analiz etmeliyiz.

### Nodal (Düğüm) Analizi
Kirchhoff'un Akım Yasası (KCL) baz alınır. Herhangi bir düğüme giren akımların toplamı çıkanlara eşittir:
$$ \sum_{k=1}^{n} I_k = 0 $$

Bunu bir empedans/kondüktans matrisine dönüştürürüz:
$$ [G] \cdot [V] = [I] $$
*Burada $[G]$ kondüktans matrisi, $[V]$ düğüm gerilimleri sütun vektörü, $[I]$ bağımsız akım kaynakları vektörüdür. Bu formülasyon, SPICE gibi endüstriyel simülatörlerin ana çalışma prensibidir.*

### Mesh (Çevre) Analizi
Kirchhoff'un Gerilim Yasası (KVL) baz alınır. Kapalı bir döngüdeki voltaj düşümlerinin toplamı sıfırdır:
$$ \sum_{k=1}^{n} V_k = 0 $$

Direnç matrisi formatında:
$$ [R] \cdot [I_{mesh}] = [V_{source}] $$

---

## 2. Devre Teoremleri: Karmaşayı İndirgemek

Bir sistem mimarı formüllerde boğulmaz; karmaşık sistemleri modellenmesini kolaylaştıran minimal eşdeğer formlara indirger.

### Thevenin ve Norton Eşdeğerlikleri
Gözlemlediğiniz "Yük (Load)" uçlarından (A-B terminalleri) bakıldığında, devasa bir veri merkezinin güç yönetimi sistemi bile tek bir voltaj kaynağı ($V_{th}$) ve tek bir seri empedansa ($Z_{th}$) indirgenebilir.

$$ V_{th} = V_{open\_circuit} $$
$$ Z_{th} = \frac{V_{open\_circuit}}{I_{short\_circuit}} $$

**Endüstriyel Karşılık:** Bir MCU'nun (STM32) GPIO pini dışarıdan bir kapasitif yüke bağlandığında Thevenin eşdeğeri olarak modellenir. Pin'in verebileceği akım kapasitesi (source/sink) bu THEVENIN direncine ($R_{th}$) bağlı olarak sinyal yükselme süresini (Rise Time) belirler.

### Maksimum Güç Transferi (Maximum Power Transfer)
Bir antenden LNA'ya (Düşük Gürültülü Yükselteç) RF sinyali taşırken enerjinin tamamının aktarılması için *empedans uyumu* (Impedance Matching) gerekir. 
Eğer kaynak empedansı $Z_S = R_S + jX_S$ ise, maksimum güç ancak yük empedansı bunun karmaşık eşleniği (complex conjugate) olduğunda aktarılır:
$$ Z_L = Z_S^* = R_S - jX_S $$

---

## 3. Dinamik Sistemler: RL, RC, RLC Filtreleri ve Zaman Cevapları

Dirençli devreler "anlık" çalışır. Fakat bobin (Inductor) ve kondansatör (Capacitor) zamanın dokusunu büker, devreyi bir diferansiyel denklemler sistemine dönüştürür.

### Kapasitör (Elektrik Alanı) ve İndüktör (Manyetik Alan)
$$ I_C = C \frac{dV_C}{dt} \quad\quad V_L = L \frac{dI_L}{dt} $$
*Bobin akımdaki ani değişime direnirken, kapasitör gerilimdeki ani değişime direnir.*

### RLC Devresi: İkinci Dereceden Sistemler (Sönümlenme)
Bir Seri RLC devresi, mekanik bir kütle-yay-amortisör sisteminin tam elektriksel karşılığıdır:
$$ L \frac{d^2 i}{dt^2} + R \frac{di}{dt} + \frac{1}{C} i = 0 $$

Sistemin karakteristiği sönümleme sabitine ($\alpha$) ve rezonans frekansına ($\omega_0$) bağlıdır:
*   **$\alpha = R / (2L)$** ve **$\omega_0 = 1 / \sqrt{LC}$**

1.  $\alpha > \omega_0$ : *Overdamped* (Sürünerek hedefe varır)
2.  $\alpha = \omega_0$ : *Critically Damped* (Sistem hedef gerilime en hızlı ve osilasyon yapmadan ulaşır - İdeal hedef).
3.  $\alpha < \omega_0$ : *Underdamped* (Sistem titrer/osile eder - LC Tank osilatörlerinin temeli).

> [!CAUTION]
> **Donanım Pratiği (Hardware Architect View):** Bir işlemcinin Power hattına dizdiğiniz bypass kapasitörleri, PCB izlerinin parazitik endüktansları (L) ile bir RLC devresi yaratır. Eğer "Underdamped" bölgeye düşerseniz (PDN Impedance Peak), işlemciniz çok fazla gürültü (voltage ringing) algılayıp rastgele Reset atar! Bu yüzden PDN (Power Delivery Network) tasarımı saf bir RLC iyileştirme sanatıdır.
