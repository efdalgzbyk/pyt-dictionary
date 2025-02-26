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
<h3>Bu sürümde ise artık kelimelerin anlamlarını girip kelimeyi ve anlamını tek bir sayfada görebileceğiz artık bi adım daha sözlük(dictionary) benzemeye başladı.</h3>

<h2>def kelimleri_yükle()</h2>
<h3>İlk adım olarak kelimelerin kaydedildiği dosya eğer silinirse diye bir önlem alarak boş bir sözlük döndürmesini isteyebilriz.</h3> 

![image](https://github.com/user-attachments/assets/45992226-8528-4e31-a757-b452356e9f32)

<h3>Ve artık "def kelimeleri_kaydet() kaldırıp onuda def kelimeleri_yukle() içine ele alabiliriz ve artık def kelimeler_yukle() yeni hali görseldeki gibi olmuş olur.</h3>

![image](https://github.com/user-attachments/assets/b5f29c46-b7b1-48c3-b495-3bf996cfc671)


<h2>def kelime_ekle()</h2>

<h3>Artık kelimeler_ekle() anlam olayını da eklicez ve kelimelerle beraber anlamlarınıda eklicez  </h3>
<h3>İlk olarak aynı kelimeler eklenmemesi adına kullandığımız if komuyunu daha etkili hale getirebilmek için </h3>

![image](https://github.com/user-attachments/assets/d351d4d3-6b05-4e51-8c91-976774e679f5)
<h3>başına ekliyerek kelime tekrarlanmasını önlemiş oluruz.
</h3>
<h3>Devamında ise kelimeye anlam eklemek için </h3>

![image](https://github.com/user-attachments/assets/7744d29a-9381-4153-bc30-aa5168f19575)
<h3>komutunu uygulayarak kelimenin anlamını sozlukğe eklemiş oluruz. Ve kodun son hali:
</h3>

![image](https://github.com/user-attachments/assets/6bedc0cb-8f4b-46f3-82ab-4bcdf4d505f1)

# def kelime_sil()
<h3>Aynı şekilde buradada kelime_ekle() de kullandığımız sozluk komutunu kullanıcaz. </h3>
<h3>Eğer ki sözlüğün içinde kelime bulunmassa diye return komutları eklemeliyiz.</h3>
<h3>Sonunda ise elde ettiğimiz yeni kelime_sil() komutu ektedir. </h3>

![image](https://github.com/user-attachments/assets/2926992d-f460-4b31-82ec-586a7b640b09)

# def anlam_getir()
<h3>Bu fonskiyonda ise verilen kelimenin anlamını döndürür, yoksa 'Anlam bulunamadı' yazar. </h3>

![image](https://github.com/user-attachments/assets/992011f4-0c6e-4591-b8d5-a0bcb6796f9f)

