# Az Dictionary

<h2>Bu sene boyunca yapıcağım python dili ile sözlük uygulamasının genel repodur</h2>

<h3>İlk önce vers. 0.0.1 sadece kelime_girme, kelime_ekle, kelime_sil ve kelime içinde harf arama yapma fonksiyonlarını eklicez.</h3>

Öncelikle dosya yollarını belirleyelim:
![image](https://github.com/user-attachments/assets/af63f594-62be-47ce-962c-d84e5f65d09b)


# Kelime_yonetimi
ilk önce Kelime_yonetimi.py dosyası ile başlayalım.
bu dosyaya kelime_ekle,kelimeleri_yükle ,kelimeleri_kaydet ve kelime_sil fonksiyonlarını tanımlayalım:

![image](https://github.com/user-attachments/assets/4037f556-5ee4-4eb3-a380-f939c5a63174)

burada ki "KELIME_DOSYASI" kelimelerin kayıt edildiği dosyaya yönlendirilmiştir.

# arama.py 
bu dosyada ise girilen harfi içeren kelimeler gösterecek fonskiyon vardır.

![image](https://github.com/user-attachments/assets/33a3eba3-7480-4a7a-aceb-60bd2d5de64b)

# ui.py
Şimdide basit bir ui yapalım.
Öncelikle gerekli olan importları yazalım.
![image](https://github.com/user-attachments/assets/98002dc6-41a2-47b1-8c88-304b1edbb6f7)

önce ![image](https://github.com/user-attachments/assets/86d45d85-adb4-4be5-a967-b25873ae9fc0) oluşturduktan sonra her kodu bu classın altına yazıcaz.

bunları yazdıktan sonra ise pencere ayarları ile Wıdget ve button ekleyelim.

![image](https://github.com/user-attachments/assets/66de16e6-0159-46a4-a2e2-69b0800306dd)

daha sonradan ise bu butonların işlevini ekleyelim.

![image](https://github.com/user-attachments/assets/370cfb69-d56b-454c-a989-2fe837986bd2)

# main.py
Hepsini tek bir kod altında toplayabiliriz artık.

![image](https://github.com/user-attachments/assets/474606e1-6973-4c9a-8e69-0ff52c26a3d1)


Ve kodu çalıştırdığımızda ise çıktı görseldeki gibi olucaktır.

![image](https://github.com/user-attachments/assets/74e742a2-1c60-4fd1-b1c4-af4140671c67)

şuan istediğimiz fonksiyonlar düzgünce çalışmaktadır.

"""Bu sürüme V 0.0.1 diyebiliriz."""


<h1>Vers. 0.0.2 </h1>
Bu sürümde ise artık kelimelerin anlamlarını girip kelimeyi ve anlamını tek bir sayfada görebileceğiz artık bi adım daha sözlük(dictionary) benzemeye başladı.

<h2>def kelimleri_yükle()</h2>
İlk adım olarak kelimelerin kaydedildiği dosya eğer silinirse diye bir önlem alarak boş bir sözlük döndürmesini isteyebilriz. 

![image](https://github.com/user-attachments/assets/45992226-8528-4e31-a757-b452356e9f32)

Ve artık "def kelimeleri_kaydet() kaldırıp onuda def kelimeleri_yukle() içine ele alabiliriz ve artık def kelimeler_yukle() yeni hali görseldeki gibi olmuş olur.

![image](https://github.com/user-attachments/assets/b5f29c46-b7b1-48c3-b495-3bf996cfc671)


<h2>def kelime_ekle()</h2>

Artık kelimeler_ekle() anlam olayını da eklicez ve kelimelerle beraber anlamlarınıda eklicez 
İlk olarak aynı kelimeler eklenmemesi adına kullandığımız if komuyunu daha etkili hale getirebilmek için 

![image](https://github.com/user-attachments/assets/d351d4d3-6b05-4e51-8c91-976774e679f5)
başına ekliyerek kelime tekrarlanmasını önlemiş oluruz.

Devamında ise kelimeye anlam eklemek için 

![image](https://github.com/user-attachments/assets/7744d29a-9381-4153-bc30-aa5168f19575)
komutunu uygulayarak kelimenin anlamını sozlukğe eklemiş oluruz. Ve kodun son hali:


![image](https://github.com/user-attachments/assets/6bedc0cb-8f4b-46f3-82ab-4bcdf4d505f1)

# def kelime_sil()
Aynı şekilde buradada kelime_ekle() de kullandığımız sozluk komutunu kullanıcaz. 
Eğer ki sözlüğün içinde kelime bulunmassa diye return komutları eklemeliyiz.
Sonunda ise elde ettiğimiz yeni kelime_sil() komutu ektedir. 

![image](https://github.com/user-attachments/assets/2926992d-f460-4b31-82ec-586a7b640b09)

# def anlam_getir()
Bu fonskiyonda ise verilen kelimenin anlamını döndürür, yoksa 'Anlam bulunamadı' yazar. 

![image](https://github.com/user-attachments/assets/992011f4-0c6e-4591-b8d5-a0bcb6796f9f)

# ui.py güncelenmiş hali

İlk önce yeni importlar ekleyerek başlayalım

![image](https://github.com/user-attachments/assets/bf8fa03a-0eef-4333-8d32-220aca6dfa90)
<h3>Burada QIcon kütüphanesi ıcon eklememize işe yarıyorken os kütüphanesi bilgisyardaki logoyu bulmaya işe yarıyor. </h3>

Eğer icon_name in yeri değiştirilir ise;

![image](https://github.com/user-attachments/assets/66d3e4f5-9a73-4f6c-bca4-47a2d40d3eaa)
<h3>Kullanılarak dosyayı otomatik olarak bulmaya işe yarar.</h3>

## Kodun son hali 

![image](https://github.com/user-attachments/assets/f39041c5-fd66-4d57-80c3-b8e4b58ff017)

![image](https://github.com/user-attachments/assets/41debd6c-8f9d-49e4-ade7-977c8c66da78)

![image](https://github.com/user-attachments/assets/261293bd-9ebd-499b-86f2-30c1d4afe596)

![image](https://github.com/user-attachments/assets/c1bc7d24-20ef-41a6-ae6a-623a0387cda9)

# main.py güncellenmiş hali

Son olarak tüm kodları tek dosyada toparlamak adına.

![image](https://github.com/user-attachments/assets/f45ccd06-78d1-40d3-989b-a7637d45f0f5)
Artık son eklediğimiz fonksiyonlarıda yazdığımıza artık run yaparak programımızın son halini alabiliriz.
Artık kelimelerin anlamlarını girerek ve kelime anlamını tek bir sayfadan görebilriz.

![image](https://github.com/user-attachments/assets/66e7b80f-349a-4212-94b0-77fd1e74dc71)


# Vers. 0.0.3 
coming soon
