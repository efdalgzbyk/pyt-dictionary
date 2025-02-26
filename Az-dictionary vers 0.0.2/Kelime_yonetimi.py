import json
import os

DOSYA_ADI = "sozluk.json"

def kelimeleri_yukle():
    """Sözlük dosyasını yükleyip Python sözlüğü olarak döndürür."""
    if not os.path.exists(DOSYA_ADI):
        return {}  # Eğer dosya yoksa boş bir sözlük döndür
    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        try:
            return json.load(dosya)  # JSON'u yükle
        except json.JSONDecodeError:
            return {}  # Eğer JSON bozuksa, boş bir sözlük döndür

def kelime_ekle(kelime, anlam):
    sozluk = kelimeleri_yukle()
    
    if kelime in sozluk:  # Aynı kelimeyi tekrar eklemeyi engelle
        return False  # Eklenmedi
    
    sozluk[kelime] = anlam  # Kelimeye anlam ekle
    
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(sozluk, dosya, ensure_ascii=False, indent=4)
    
    return True  # Başarıyla eklendi


def kelime_sil(kelime):
    """Verilen kelimeyi sözlükten siler."""
    sozluk = kelimeleri_yukle()
    
    if isinstance(sozluk, dict) and kelime in sozluk:  # Kelimenin olup olmadığını kontrol et
        del sozluk[kelime]  # Kelimeyi sil
    
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            json.dump(sozluk, dosya, ensure_ascii=False, indent=4)
        
        return True  # Başarıyla silindi
    
    return False  # Kelime bulunamadı

def anlam_getir(kelime):
    sozluk = kelimeleri_yukle()
    return sozluk.get(kelime, "Anlam bulunamadi.")
