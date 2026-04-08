# ⏱️ Real-Time Critical Systems Masterclass: RTOS Jitter, Interrupt Latency ve ARM Cortex-M Mimarisi

> *"Bir saniye geç gelen veri, karar verme mekanizmasını değil, güvenlik sistemini bozar."*

---

## 1. ARM Cortex-M İşlemci Hattı (Pipeline) Anatomisi

STM32'nin omurgası olan **ARM Cortex-M4** çekirdeği, 3 aşamalı (Fetch → Decode → Execute) bir pipeline mimarisine sahiptir. Asıl farklılığı ise:

- **Thumb-2 ISA:** 16-bit ve 32-bit karışık komut seti ile hem kod yoğunluğu hem performans optimize edilir.
- **FPU (Donanımsal Kayan Nokta Ünitesi):** IEEE 754 tek hassasiyetli işlemleri tek siklüste executes.
- **MPU (Bellek Koruma Birimi):** RTOS katmanında farklı task'ların birbirinin bellek alanına yazmasını engeller. Fonksiyonel güvenlik (IEC 61508) için zorunludur.
- **NVIC (Nested Vectored Interrupt Controller):** 240 adet önceliklendirilmiş kesme vektörü.

---

## 2. Interrupt Latency: Matematiği

Bir sensör kesmesi (IRQ) tetiklendiğinde, işlemcinin mevcut görevi durdurup ISR'a (Interrupt Service Routine) atlama süresi **Interrupt Latency** olarak adlandırılır.

ARM Cortex-M için minimum interrupt latency hesabı:

| Aşama | Siklüs Sayısı |
|---|---|
| Mevcut komutun tamamlanması | 0–3 |
| Stack'e register kaydetme (Push) | 12 (FPU'lu durumda 26+) |
| Pipeline temizleme (Flush) | 3 |
| Vektör tablosundan adres okuma | 3+ |
| **Toplam Minimum** | **~12–16 siklüs** |

200 MHz çalışan bir Cortex-M7 için: $16 / 200\text{MHz} = 80\text{ ns}$

> [!CAUTION]
> **Tail-Chaining Optimizasyonu:** Eğer bir ISR bittiğinde hemen ardından başka bir bekleyen IRQ varsa, ARM önbelleğe alınan register durumunu boşaltmadan yeni ISR'a geçer (Tail-Chaining). Bu mekanizma, ardışık kesmelerde stack operasyonlarını sıfıra indirir ve %33 latensi azaltır.

---

## 3. Deterministic Timing: WCET ve Jitter Analizi

Gerçek zamanlı sistemlerde sadece "ortalama" hız değil, **En Kötü Durum Yürütme Süresi (WCET - Worst Case Execution Time)** zamansal olarak garanti edilmek zorundadır.

### Jitter Kaynakları
1. **Cache Miss Jitter:** İşlemcinin instruction cache (I-Cache) doluysa belleğe gitmesi gerekir. STM32H7 gibi yüksek hızlı çekirdeklerde, ART (Adaptive Real-Time) Accelerator ile Flash bellek gecikmeleri maskelenir.
2. **Interrupt Preemption:** Daha yüksek öncelikli bir IRQ mevcut görevin yürütme süresine rastlantısal olarak eklenir.
3. **Pipeline Flush:** Koşul dallanmalarında (branch misprediction) pipeline temizlenir.

### Schedulability Testi: Rate Monotonic Analysis (RMA)
$n$ adet periyodik görev varsa, tüm görevlerin zamanında tamamlandığının matematiksel garantisi:

$$\sum_{i=1}^{n} \frac{C_i}{T_i} \leq n(2^{1/n} - 1)$$

*Burada $C_i$ görünün en kötü yürütme süresi, $T_i$ görünün periyodudur.*

$n \rightarrow \infty$ için bu üst sınır $\ln(2) \approx 0.693$'e yaklaşır, yani CPU kullanımı %69.3'ü geçmediği sürece hiçbir görev deadline'ını kaçırmaz.

---

## 4. Lock-Free Programlama: Mutex Olmadan Veri Paylaşımı

Gerçek zamanlı sistemlerde iki görev aynı veri yapısına erişiyorsa Mutex veya Semaphore kullanırız. Ancak Mutex almak deterministik değildir (Priority Inversion). Çözüm: **Lock-Free veri yapıları.**

### Priority Inversion Senaryosu (Mars Pathfinder Vakası)
1997'de Mars Pathfinder görevinde düşük öncelikli bir görev bir Mutex tutuyordu.
Yüksek öncelikli görev bu Mutex için bekledi → beklerken orta öncelikli görev CPU'yu aldı → yüksek öncelikli görev asıldı.
Gerçek zamanlı İzleme yazılımı "watchdog timeout" vererek sistemi resetledi.

**Çözüm:** FreeRTOS'ta `configUSE_MUTEXES` yerine `configUSE_RECURSIVE_MUTEXES` + Priority Inheritance protokolü kullanılır:
```c
xSemaphoreCreateMutex(); // Priority Inheritance aktif
```

---

## 5. DMA: CPU'suz Veri Transferi Mimarisi

DMA (Direct Memory Access) denetleyicisi, CPU hiç müdahil olmadan çevre biriminden (ADC, SPI, UART) RAM'e veri taşır.

### Circular DMA ile ADC Örnekleme

```
ADC → DMA → RAM[0] → RAM[1] → ... → RAM[N-1] → RAM[0] → (tekrar)
```

DMA yarısı dolduğunda CPU'ya **Half-Transfer Interrupt**, tamamen dolduğunda **Transfer-Complete Interrupt** gönderir. Bu sayede ADC, CPU'yu tamamen meşgul etmeden sürekli örnekleme yapar ve CPU yalnızca işlenmiş bufferı çalışır.

> [!IMPORTANT]
> **Cache Coherency Tuzağı (STM32H7):** Cortex-M7'de L1 Data Cache aktiftir. DMA doğrudan RAM'e yazar ama CPU önbelleğe alanı hâlâ eski veriyi gösterir. Bu durumda **SCB_InvalidateDCache_by_Addr()** çağrılmadan DMA verisi işlenemez. Bu hata, gece yarısı hata ayıklamalarının birinci sebebidir.
