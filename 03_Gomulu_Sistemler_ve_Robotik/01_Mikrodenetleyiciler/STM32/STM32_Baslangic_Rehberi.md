# 🚀 STM32 Mikrodenetleyici Mimarisi ve Programlama

STM32 serisi, STMicroelectronics tarafından geliştirilen, endüstriyel ve tüketici elektroniğinde en çok tercih edilen **ARM Cortex-M** tabanlı bir ekosistemdir.

---

## 1. Mimariye Giriş: Neden STM32?

Geleneksel 8-bit mikrodenetleyicilerin aksine STM32, 32-bit veriyolu ve karmaşık çevre birimleri (peripherals) sunar.

*   **Pipelining:** Komutlar birden fazla aşamada (fetch, decode, execute) işlenir, bu da birim zamanda daha fazla işlem (MIPS) sağlar.
*   **Interrupt Handling (NVIC):** Önceliklendirilebilir kesmeler sayesinde gerçek zamanlı tepki verebilir.
*   **DMA (Direct Memory Access):** CPU'yu meşgul etmeden bellek ile çevre birimleri arasında veri taşımayı sağlar.

---

## 2. Yazılım Katmanları (HAL vs LL vs Bare-Metal)

STM32 programlarken üç ana yaklaşım vardır:
1.  **HAL (Hardware Abstraction Layer):** En kolayıdır, her şey hazır fonksiyonlarla yapılır (`HAL_GPIO_WritePin`). Taşınabilirdir ama hantaldır.
2.  **LL (Low-Layer):** Register seviyesine çok yakındır, daha hızlıdır ama her mikrodenetleyici için özeldir.
3.  **Bare-Metal (CMSIS):** Doğrudan register adreslerine (`*0x40021000 = 0x01;`) veri yazılarak yapılır. Maksimum performans için tercih edilir.

---

## 3. İlk Proje Akışı: "The Path to Bare-Metal"

Bir pinin durumunu değiştirmek (LED yakmak) için şu fiziksel adımları kod yönetmelidir:
1.  **Clock Management (RCC):** İlgili portun saat sinyalini aktif et (STM32'de her modül tasarruf için başlangıçta kapalıdır).
2.  **GPIO Configuration:** Pini "Output" veya "Input" olarak ayarla (`MODER` register).
3.  **Output Write:** Pini 1 veya 0 yap (`ODR` veya `BSRR` register).

---

## 4. Gelişmiş Özellikler
*   **PWM:** Motor kontrolü ve LED parlaklık ayarı.
*   **I2C/SPI:** Sensörler ve ekranlar ile yüksek hızlı haberleşme.
*   **ADC:** Analog dünyadan (sıcaklık, voltaj) veriyi dijitale çevirme.

> [!CAUTION]
> **Architect Insight:** Bir STM32 kartı tasarlarken besleme pinleri arasındaki **Decoupling Capacitors** (genelde 100nF) hayati önem taşır. Bu kapasitörler olmazsa CPU lojik işlemler sırasında voltajı dalgalandırır ve kodun ortasında "HardFault" hatası alarak çöker. Donanım ve yazılım ayrılmaz bir bütündür.
