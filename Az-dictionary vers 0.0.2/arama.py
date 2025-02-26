def kelime_ara(sozluk, harf):
    """Girilen harfi içeren kelimeleri döndürür."""
    return [kelime for kelime in sozluk if harf.lower() in kelime.lower()]
