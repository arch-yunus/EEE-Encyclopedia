# 🏛️ Systems Engineering & Savunma Sanayii Masterclass: DO-254, MIL-STD ve Fonksiyonel Güvenlik

> *"Sivil elektronikte bir hata sizi sindirir. Kritik sistemlerde bir hata sizi öldürür."*

---

## 1. V-Modeli: Sistem Geliştirme Yaşam Döngüsü

Savunma ve havacılık sistemlerinde "önce yaz, sonra test et" yaklaşımı kabul edilemez. **V-Modeli** her geliştirme aşamasını bir doğrulama adımıyla eşleştirir.

```
Sistem Gereksinimleri ─────────────────── Sistem Doğrulama Testleri
        │                                           │
   Tasarım Mimarisi ─────────────── Entegrasyon Testleri
              │                           │
         Detaylı Tasarım ─────── Birim Testleri
                    │
               Implementasyon (Kod/Donanım)
```

### DO-178C (Uçuş Yazılımı) ve DO-254 (Havacılık Donanımı) Seviyeleri

Her ikisi de yazılım veya donanımın arızalanmasının ne denli kritik sonuçlara yol açacağına göre A'dan E'ye seviyelendirilir:

| Seviye | Arıza Etkisi | Örnek |
|---|---|---|
| **DAL-A** | Felaket (Uçak düşer, kayıp olur) | Fly-by-wire uçuş kontrol bilgisayarı |
| **DAL-B** | Tehlikeli (Ağır yaralanma) | Motor FADEC kontrol yazılımı |
| **DAL-C** | Major (Acil durum) | Trafik kaçınma sistemi (TCAS) |
| **DAL-D** | Minor (Ekstra iş yükü) | Kabini izleme sistemi |
| **DAL-E** | Etkisiz | Eğlence sistemi |

DAL-A donanım geliştirmesi, her mantık kapısı için izlenebilirlik (Traceability), her test senaryosu için kapsam kanıtı (Coverage) ve bağımsız doğrulama ekibi (IV&V) gerektirir.

---

## 2. Fonksiyonel Güvenlik: IEC 61508 ve ISO 26262

Havacılık dışındaki kritik sistemler (Endüstriyel otomasyon, Otomotiv) IEC 61508 ve türev standardı ISO 26262 (ASIL - Automotive Safety Integrity Level) kapsamında değerlendirilir.

### Güvenli Durum Tasarımı (Fail-Safe Architecture)

Sistem arıza durumunda güvenli bir duruma geçmelidir:
- **Fail-Passive:** Arızada sistem kapanır (Örn: motor durdurulur).
- **Fail-Operational:** Arızaya rağmen çalışmaya devam eder (Örn: uçak her zaman yedek FBW kanalı aktif tutar).
- **Fail-Safe:** Arızada bilinen güvenli bir konuma alınır.

### Hata Ağacı Analizi (FTA - Fault Tree Analysis)

Üst seviye tehlike olayından (Top Level Hazard) geriye doğru giderek nedensellik zinciri kurulur:
```
[UÇAK KATASTROFİK KAYIP]
         |
    [AND kapısı] 
    /           \
[FBW Arıza]  [Pilot Müdahale Yok]
     |
 [OR kapısı]
  /      \
[CPU Arıza] [Güç Kaybı]
```

IEC 61508 SIL-3 için üst seviye tehlike olasılığı $< 10^{-7}$ hata/saat sınırındadır.

---

## 3. MIL-STD-810: Çevre Dayanıklılık Test Standartları

Savunma elektroniğinin muharebeye hazır olması için aşağıdaki testleri geçmesi gerekir:

| Test | Metot | Koşul |
|---|---|---|
| **Sıcaklık** | MIL-STD-810 Method 501/502 | -51°C ile +85°C arası |
| **Nem** | Method 507 | %95 bağıl nem, 24 saat |
| **Vibrasyon** | Method 514 | Kara araçları için 7.7g RMS |
| **Şok** | Method 516 | 40g, 11ms saw-tooth pulse |
| **Tuz Sisi** | Method 509 | %5 NaCl çözeltisi, 48 saat |
| **EMI/EMC** | MIL-STD-461 | CE/CS/RE/RS limitleri |

> [!WARNING]
> **MIL-SPEC Malzeme Seçimi:** Ticari (COTS) bileşenler genellikle 0–70°C aralığında çalışıyorken askeri sınıf (-55°C – +125°C) bileşenler gereklidir. Bir geliştirme safhasında "bütçe kısıtı" nedeniyle ticari bileşen kullanılırsa, ilerleyen süreçteki TRL (Technology Readiness Level) yükseltmeleri imkânsız hale gelir.

---

## 4. TEKNOFEST ve KDR Yazımında Profesyonel Metodoloji

Türkiye'nin en büyük teknoloji yarışması olan TEKNOFEST'te skorlanmanın %40'ını teknik raporlar oluşturur.

### KDR (Kritik Tasarım Raporu) Anatomisi

```
1. Yönetici Özeti (Executive Summary)
   - Problemin tanımı, çözümün özeti ve beklenen performans metrikleri

2. Sistem Mimarisi
   - Fonksiyonel blok diagram
   - Veri akış diyagramı (DFD)
   - Güç bütçesi (Power Budget)

3. Alt Sistem Tasarımları (Her blok için ayrı bölüm)
   - Teorik arka plan (neden bu yaklaşım?)
   - Tasarım hesaplamaları
   - Simülasyon sonuçları
   - Devre/mekanik/yazılım detayı

4. Doğrulama ve Doğrulama Planı (V&V)
   - Test matrisi (Her gereksinim ← Test metodu)
   - Kabul kriterleri

5. Risk Analizi (FMEA - Failure Mode & Effects Analysis)
```

> [!TIP]
> **Puanı Belirleyen Küçük Detay:** KDR'de "Bu yaklaşımı seçtik çünkü X alternatifleri inceledik ve Y metriği açısından bizim çözümümüz üstün çıktı" cümlesi, hakeme tasarım kararlarınızın bilinçli verildiğini gösterir. Alternatif analizi olmayan raporlar yarışmada üst sıralara çıkamaz.
