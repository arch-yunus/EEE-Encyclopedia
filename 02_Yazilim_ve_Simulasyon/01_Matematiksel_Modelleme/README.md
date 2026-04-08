# 📐 Matematiksel Modelleme: Sistemlerin Ruhu

Karmaşık bir elektrik motorunu veya otonom bir aracın dinamiğini kodlamadan önce, onun matematiksel "soyutlamasını" yapmanız gerekir.

---

## 1. State-Space (Durum-Uzay) Temsili

Modern kontrol teorisinin temeli, iç değişkenlerin (akım, hız, sıcaklık vb.) bir matris sistemiyle ifade edilmesidir.

$$ \dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t) $$
$$ \mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) $$

*   **A Matrisi:** Sistem dinamiği (kararlılık burada gizlidir).
*   **B Matrisi:** Girişlerin sisteme etkisi.
*   **C & D Matrisleri:** Ölçülen çıkışlar.

---

## 2. MATLAB & Simulink: Endüstri Standardı

Mühendislik problemlerini nümerik olarak çözmek için MATLAB ana araçtır.

### Kritik Fonksiyonlar
*   `ss()`: State-space modeli kurma.
*   `tf()`: Transfer fonksiyonu oluşturma.
*   `step()`: Sistemin basamak tepkisini (settling time, overshoot) analiz etme.
*   `bode()`: Frekans cevabını ve kararlılık payını (Gain/Phase Margin) görme.

---

## 3. Sistem Tanımlama (System Identification)

Bazen sistemin iç denklemlerini bilemeyiz. Bu durumda girişe bilinen bir sinyal (beyaz gürültü veya impuls) verip çıkışı analiz ederek sistemi modelleriz.

> [!TIP]
> **System Architect View:** Bir drone üzerindeki motor sürücü (ESC) algoritmasını yazarken motorun endüktansını ve atalet momentini bu matematiksel modellerle simüle etmezseniz, yazdığınız PID katsayıları gerçek dünyada sistemi osilasyona sokup parçalayacaktır.
