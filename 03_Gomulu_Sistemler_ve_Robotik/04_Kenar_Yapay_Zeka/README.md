# 🧠 Kenar Yapay Zeka (Edge AI)

Yapay zekayı bulutta (Cloud) değil, doğrudan sensörün olduğu yerde, veri kaynağında (Edge) çalıştırma devrimidir.

---

## 1. Neden Edge AI?

*   **Düşük Gecikme (Latency):** Verinin buluta gidip gelmesini beklemez (Otonom sürüş için kritik).
*   **Gizlilik:** Kişisel veriler cihazdan ayrılmaz.
*   **Bandwidth:** Terabaytlarca ham görüntü yerinde işlenir, sadece sonuç gönderilir.

---

## 2. Donanım Hızlandırıcılar

Standart CPU'lar AI modellerini çalıştırmak için yavaştır. Özel donanımlar gerekir:
*   **NVIDIA Jetson (GPU):** CUDA çekirdekleri ile ağır görüntü işleme modellerini (YOLO vb.) saniyede yüksek kare hızlarında (FPS) çalıştırır.
*   **TPU/NPU:** Google'ın Coral serisi veya özel AI çiplerindeki sinir ağı hızlandırıcıları.

---

## 3. Model Optimizasyonu: TensorRT

Geliştirdiğiniz bir modu doğrudan cihazda çalıştıramazsınız. Cihazın mimarisine göre optimize edilmelidir.
*   **Quantization:** Değişkenlerin boyutunu küçültmek (örn: FP32 -> INT8).
*   **Pruning:** Gereksiz nöron bağlantılarını budamak.

---

## 4. Kullanım Alanları
*   Gerçek zamanlı nesne tespiti.
*   Sesli asistanlar.
*   Endüstriyel hata (anomali) tespiti.

> [!IMPORTANT]
> **Architect View:** Bir Edge AI sistemi tasarlarken kısıtlı bir enerji bütçeniz (Watt) vardır. Modelin doğruluğu (Accuracy) kadar, Watt başına işlem gücü (Efficiency) bir tasarım kriteridir.
