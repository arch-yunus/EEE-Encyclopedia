# 🧲 Elektromanyetik Teori: Uzayın Dijital Kodu

Mühendislik, atomik seviyede elektromanyetik alanlara hükmetme sanatıdır. Çizdiğiniz bir PCB hattı eğer yeterince hızlı (High-Speed Signals) sinyal iletiyorsa artık bir tel değil, bir *Dalga Kılavuzu* (Waveguide) gibi davranmaya başlar.

**Maxwell Denklemleri**, evrenin donanımsal kod bloklarıdır.

---

## 1. Maxwell'in Dört Denklemi (The Core Engine)

Sistem mimarları (System Architects) için Maxwell, ezberlenecek denklemlerden ibaret değil, RF ve EMI/EMC (Elektromanyetik Girişim) sorunlarını çözen nihai referanstır.

### I. Gauss'un Elektrik Yasası
Yükler, elektrik alan çeşmeleridir (source) veya girdaplarıdır (sink).
*   **İntegral Form:** $\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{enc}}{\epsilon_0}$
*   **Diferansiyel Form:** $\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$
**Endüstriyel Pratik:** Bir çipin bacakları arasında biriken parazitik kapasitansı hesaplarken yüzey alanındaki yük dağılımına Gauss yasasıyla bakarız.

### II. Gauss'un Manyetik Yasası
Manyetik monopoller yoktur; manyetik alan çizgileri daima kapalı bir döngü olmak zorundadır.
*   **İntegral Form:** $\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$
*   **Diferansiyel Form:** $\nabla \cdot \mathbf{B} = 0$
**Endüstriyel Pratik:** Bir SMPS güç kaynağı transformatörü sararken, manyetik akının devreyi nüve (ferrite core) üzerinden kapatmak zorunda olması bu yasaya dayanır.

### III. Faraday'ın İndüksiyon Yasası
Zamanla değişen bir manyetik alan, elektrik alan yaratır (voltaj indükler).
*   **İntegral Form:** $\oint_C \mathbf{E} \cdot d\mathbf{l} = - \frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$
*   **Diferansiyel Form:** $\nabla \times \mathbf{E} = - \frac{\partial \mathbf{B}}{\partial t}$
**Endüstriyel Pratik:** "Cross-Talk" problemi. Devrenizdeki bir yoldan vuran (switching) yüksek akım ($di/dt$), yanından geçen hassas analog ADC yoluna Manyetik B alanı batırarak voltaj (gürültü) yükler! Bunu engellemek için parazitik döngü alanını ($d\mathbf{A}$) küçültürüz.

### IV. Ampère-Maxwell Yasası
Zamanla değişen elektrik alanı manyetik alan yaratır (Deplasman Akımı).
*   **İntegral Form:** $\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{enc} + \mu_0 \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A}$
*   **Diferansiyel Form:** $\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$
**Endüstriyel Pratik:** İki kapalı kapasitör plakası arasında bir tel bile yoktur ama AC sinyal plakalardan akar. Havadan iletilen radyo sinyallerinin ($\frac{\partial \mathbf{E}}{\partial t}$) varlığı bu kısmi türev omurgasıyla kanıtlanır.

---

## 2. Poynting Vektörü: Gücün Akışı

Enerji telin içinde değil, elektromanyetik alanlarla telin *dışında* uçar!
Poynting vektörü ($\mathbf{S}$), metrekare başına uzaydan ilerleyen elektromanyetik gücü simgeler:
$$ \mathbf{S} = \mathbf{E} \times \mathbf{H} $$

> [!WARNING] 
> **System Architect Visyonu:** Pili bir motora bağladığınızda enerji, elektronların kabloda sekmesiyle aktarılmaz. Pil ile motor arasında kurulan E (Elektrik Alan) ve H (Manyetik Alan) sayesinde havadan uzamsal bir tüp halinde (Poynting field) aktarılır. Bu yüzden Microstrip (PCB Hattı) dizayn ederken hattın altındaki *Return Path (Ground Plane)* kopuksa, güç alanı yüzeye sızar ve devasa bir EMI (Radyasyon) problemi cihazınızın FCC/CE testlerinden kalmasına sebep olur!
