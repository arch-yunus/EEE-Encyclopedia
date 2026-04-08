# 🎯 Kontrol Teorisi Masterclass: Kalman Filtresi ve Modern Gözlemciler

> *"Ölçemediğin şeyi kontrol edemezsin. Gözlemleyemediğin şeyi ölçemezsin."*

---

## 1. Durum Gözlemcisi (State Observer / Luenberger Observer)

State-Space bölümünde sistemin durum vektörünü ($\mathbf{x}$) teorik olarak ele aldık. Ancak pek çok gerçek sistemde durum değişkenlerinin tamamı doğrudan ölçülemez. Örneğin, bir DC motorun açısal hızını ($\dot{\theta}$) enkodersiz tahmin etmek zorunda kalabiliriz.

**Luenberger Gözlemcisi**, ölçülen çıkışı ($\mathbf{y}$) ve bilinen girişi ($\mathbf{u}$) kullanarak tahmin edilen durumu ($\hat{\mathbf{x}}$) sürekli düzelten paralel bir modeldir:

$$\dot{\hat{\mathbf{x}}} = \mathbf{A}\hat{\mathbf{x}} + \mathbf{B}\mathbf{u} + \mathbf{L}(\mathbf{y} - \mathbf{C}\hat{\mathbf{x}})$$

- **$\mathbf{L}$** : Gözlemci kazanç matrisi. Hata ($\mathbf{y} - \mathbf{C}\hat{\mathbf{x}}$) ile gerçeği ne kadar hızlı yakalayacağını belirler.
- Hata dinamiği: $\dot{\mathbf{e}} = (\mathbf{A} - \mathbf{LC})\mathbf{e}$
- **Tasarım Kriteri:** $(\mathbf{A} - \mathbf{LC})$ matrisi her zaman kararlı sol yarı S-düzleminde konumlandırılmalıdır.

---

## 2. Kalman Filtresi: Optimum Durum Tahmini

Luenberger gözlemcisi deterministik sistemler için idealdir. Gerçek dünya ise gürültü içerir. **Kalman Filtresi**, Gaussian gürültü altında en düşük ortalama karesel hata (MMSE - Minimum Mean Square Error) ile tahmin yapan optimal bir gözlemcidir.

### Süreç ve Ölçüm Modeli

$$\mathbf{x}_k = \mathbf{A}\mathbf{x}_{k-1} + \mathbf{B}\mathbf{u}_k + \mathbf{w}_k \quad [\text{Süreç Gürültüsü: } \mathbf{w}_k \sim \mathcal{N}(0, \mathbf{Q})]$$

$$\mathbf{z}_k = \mathbf{H}\mathbf{x}_k + \mathbf{v}_k \quad [\text{Ölçüm Gürültüsü: } \mathbf{v}_k \sim \mathcal{N}(0, \mathbf{R})]$$

### Kalman Filterinin İki Aşaması

**Tahmin (Predict):**
$$\hat{\mathbf{x}}_{k|k-1} = \mathbf{A}\hat{\mathbf{x}}_{k-1|k-1} + \mathbf{B}\mathbf{u}_k$$
$$\mathbf{P}_{k|k-1} = \mathbf{A}\mathbf{P}_{k-1|k-1}\mathbf{A}^T + \mathbf{Q}$$

**Güncelleme (Update):**
$$\mathbf{K}_k = \mathbf{P}_{k|k-1}\mathbf{H}^T(\mathbf{H}\mathbf{P}_{k|k-1}\mathbf{H}^T + \mathbf{R})^{-1} \quad [\textbf{Kalman Kazancı}]$$
$$\hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k(\mathbf{z}_k - \mathbf{H}\hat{\mathbf{x}}_{k|k-1})$$
$$\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k\mathbf{H})\mathbf{P}_{k|k-1}$$

> [!NOTE]
> **Q ve R Arasındaki Denge:** Bu iki matris, filtrenin kişiliğini belirler.
> - **$\mathbf{Q} \gg \mathbf{R}$:** "Modelime güvenmiyorum, ölçümlere uyanım." Filtre ölçüme abanır, hızlı tepkili ama gürültüye duyarlı.
> - **$\mathbf{R} \gg \mathbf{Q}$:** "Sensörüme güvenmiyorum, modele uyanım." Filtre yumuşak ama ataletli olur, ani değişimlere geç tepki verir.

---

## 3. Genişletilmiş Kalman Filtresi (EKF) — Lineer Olmayan Dünyaya Köprü

Standart Kalman Filtresi yalnızca lineer sistemlerde optimal çalışır. Gerçek robotik ve havacılık sistemleri (ataletsel navigasyon, SLAM) doğası gereği **non-lineerdir**. EKF, her kademede sistemi mevcut tahmin noktası etrafında Jacobian matris ile lineerize eder:

$$\mathbf{A}_{jakobyan} = \left. \frac{\partial f}{\partial \mathbf{x}} \right|_{\hat{\mathbf{x}}_{k-1}}$$

> [!WARNING]
> **EKF'nin Kırılma Noktası:** Eğer sistem karmaşık non-lineer bölgelerde çalışıyorsa (örneğin, bir hipersonik füzenin giriş açısı değişimleri), EKF'nin Jacobian linearizasyonu yetersiz kalır ve filtre ıraksayabilir. Bu durumlarda **UKF (Unscented Kalman Filter)** veya **Parçacık Filtreler (Particle Filters)** tercih edilir.

---

## 4. LQR (Linear Quadratic Regulator): Optimal Kontrol

Gözlemci ile durumu artık tahmin edebiliyoruz. Şimdi kontrolü optimize etmemiz gerekiyor. **LQR**, aşağıdaki maliyet fonksiyonunu minimum yapan kontrol girdisini ($\mathbf{u^*}$) hesaplar:

$$J = \int_0^{\infty} \left( \mathbf{x}^T \mathbf{Q} \mathbf{x} + \mathbf{u}^T \mathbf{R} \mathbf{u} \right) dt$$

- **$\mathbf{Q}$ matrisi:** Durum hatası (sapma) ağırlığı. Büyük Q → sistem hedefe hızla döner ama enerji harcar.
- **$\mathbf{R}$ matrisi:** Kontrol eforu ağırlığı. Büyük R → sistem enerji tasarrufu yapar ama yavaş tepki gösterir.

Çözüm, **Ricatti Denkleminin** ($\mathbf{P}$) sürekli hal çözümüdür:

$$\mathbf{A}^T\mathbf{P} + \mathbf{P}\mathbf{A} - \mathbf{P}\mathbf{B}\mathbf{R}^{-1}\mathbf{B}^T\mathbf{P} + \mathbf{Q} = 0$$

$$\mathbf{u}^* = -\underbrace{\mathbf{R}^{-1}\mathbf{B}^T\mathbf{P}}_{\mathbf{K}_{LQR}} \mathbf{x}$$

> [!IMPORTANT]
> **Endüstriyel Uygulama:** SpaceX Falcon 9'un iniş algoritması, son evrenin lineer bölgesine yaklaştığında EKF + LQR kombinasyonu kullanır. Motorun yalnızca yatay titreşimi (gimbal) lineer modele uyar, dolayısıyla bu kombinasyon hassas dikey inişi mathematiksel olarak garanti altına alır.
