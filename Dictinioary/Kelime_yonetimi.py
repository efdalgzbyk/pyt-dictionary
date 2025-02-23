import json

KELIME_DOSYASI = "kelimeler.json"

def kelimeleri_yukle():
    """JSON dosyasından kelimeleri yükler ve bir set olarak döndürür."""
    try:
        with open(KELIME_DOSYASI, "r", encoding="utf-8") as dosya:
            return set(json.load(dosya))  # Set olarak döndür
    except (FileNotFoundError, json.JSONDecodeError):
        return set()

def kelimeleri_kaydet(sozluk):
    """Güncellenmiş kelimeleri JSON dosyasına kaydeder."""
    with open(KELIME_DOSYASI, "w", encoding="utf-8") as dosya:
        json.dump(list(sozluk), dosya, ensure_ascii=False, indent=4)  # Liste olarak kaydet

def kelime_ekle(sozluk, kelime):
    """Yeni bir kelime ekler."""
    if kelime in sozluk:
        return False  # Kelime zaten var
    sozluk.add(kelime)  # `add` metodu set için geçerli
    kelimeleri_kaydet(sozluk)
    return True

def kelime_sil(sozluk, kelime):
    """Bir kelimeyi siler."""
    if kelime in sozluk:
        sozluk.remove(kelime)  # Set'ten kaldırma işlemi
        kelimeleri_kaydet(sozluk)
        return True
    return False
