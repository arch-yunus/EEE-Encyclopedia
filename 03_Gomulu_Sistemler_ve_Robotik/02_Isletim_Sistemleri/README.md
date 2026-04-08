# 🕒 Gerçek Zamanlı İşletim Sistemleri (RTOS)

Karmaşık bir sistemde (örn: bir drone), aynı anda GPS verisi okumanız, PID kontrolü yapmanız ve telemetri göndermeniz gerekir. Bunları tek bir sonsuz döngü (`while(1)`) içinde yapmak imkansızdır. Çözüm: **RTOS**.

---

## 1. RTOS Nedir?

Genel işletim sistemlerinin (Windows/Linux) aksine RTOS, bir görevi (task) yapmak için **garanti süresi (Deterministic time)** sunar.

*   **Scheduler:** Hangi görevin ne zaman çalışacağına karar veren çekirdek mekanizma.
*   **Multitasking:** CPU'nun çok hızlı görev değiştirerek her şeyi aynı anda yapıyor gibi görünmesi.

---

## 2. Temel Kavramlar

*   **Tasks:** Programın bağımsız fonksiyonları.
*   **Priority:** Yüksek öncelikli görev (örn: emniyet durdurma) düşük öncelikli olanı (örn: ekran güncelleme) yarıda kesebilir.
*   **Semaphore & Mutex:** İki görevin aynı donanıma (örn: UART) aynı anda saldırmasını engelleyen trafik ışıkları.
*   **Queues:** Görevler arası veri taşıyan güvenli boru hatları.

---

## 3. FreeRTOS: Gömülü Dünyanın Standartı

FreeRTOS, en popüler açık kaynaklı RTOS'tur. STM32 ve ESP32 gibi işlemcilerde standart olarak kullanılır.

### Örnek Kod Yapısı (C):
```c
void Task1(void *pvParameters) {
    while(1) {
        // Sensör oku
        vTaskDelay(pdMS_TO_TICKS(10)); // 10ms bekle (CPU'yu diğerlerine bırak)
    }
}
```

> [!IMPORTANT]
> **Critical Error:** `vTaskDelay` yerine `HAL_Delay` kullanırsanız, tüm işletim sistemini dondurursunuz! Bu, RTOS mimarisindeki en yaygın ve ölümcül hatadır.
