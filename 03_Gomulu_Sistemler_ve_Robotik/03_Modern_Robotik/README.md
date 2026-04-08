# 🤖 Modern Robotik: ROS2 (Robot Operating System)

Robotik artık sadece bir kolun hareket etmesi değil, devasa bir veri iletişim ağıdır. **ROS2**, bu ağın sinir sistemidir.

---

## 1. ROS2 Mimarisi: Node Tabanlı İletişim

ROS2 bir işletim sistemi değil; bir **Middleware** (Ara Yazılım) katmanıdır. Robotun her parçası bir **Node** (Düğüm) dır.

*   **Pub/Sub (Topics):** Bir düğüm veri yayınlar (örn: Lidar), diğeri dinler (örn: Navigasyon).
*   **Services:** İstek-Cevap mantığı (örn: "Işıkları yak").
*   **Actions:** Uzun süreli görevler (örn: "Mutfağa git").

---

## 2. Otonom Navigasyon (Nav2)

Bir robotun otonom hareket etmesi için 3 soruya cevap vermesi gerekir:
1.  **Neredeyim? (Localization):** Odometre ve IMU verilerinin EKF (Extended Kalman Filter) ile birleştirilmesi.
2.  **Etrafımda ne var? (Mapping):** Lidar verisiyle harita (SLAM) oluşturma.
3.  **Nasıl giderim? (Path Planning):** A* veya DWA gibi algoritmalarla en kısa ve güvenli yolu bulma.

---

## 3. İletişim Protokolü: DDS (Data Distribution Service)

ROS2'yi ROS1'den ayıran en büyük fark endüstriyel standart olan **DDS** kullanımıdır. Bu sayede robotlar arası iletişim çok daha güvenli ve gerçek zamanlıdır.

> [!TIP]
> **Expert Note:** Bir robot tasarlarken sensör verilerini ROS2 ile işliyorsanız, **Micro-ROS** kullanarak doğrudan STM32 seviyesindeki verileri ROS ağının bir parçası yapabilirsiniz.
