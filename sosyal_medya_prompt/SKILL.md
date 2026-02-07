# Sosyal Medya Prompt Skill

Bu modül, verilen konuya göre sosyal medya seslendirme metni üretir. Kurallar `talimatlar.md` ve `talimatlar.json` dosyalarında tanımlıdır.

## Girdi
- `konu` (zorunlu): Kısa açıklama veya tek cümle
- `platform` (opsiyonel): Instagram, TikTok, X, LinkedIn
- `ton` (opsiyonel): resmi, samimi, eğlenceli
- `hedef_kitle` (opsiyonel)

## Çıktı Sözleşmesi
- Çıktı Türkçe konuşma metnidir
- Liste/madde yok, düz metin
- Maksimum 2 dakika seslendirme
- Problem-Interrupt Hybrid akışı korunur

## Dosyalar
- `talimatlar.md`: AI asistanlar için prompt
- `talimatlar.json`: Programatik kullanım için prompt

## Kullanım
1. `talimatlar.md` içeriğini kopyalayın
2. AI asistana yapıştırın
3. Konuyu verin ve seslendirme metnini alın

Programatik kullanım örneği (Python):
```python
import json

with open("talimatlar.json", "r", encoding="utf-8") as f:
    prompt = json.load(f)

# prompt['prompt'] -> model çağrısına gönderilir
```

## Entegrasyon
- Üretilen metin doğrudan `minimax/minimax_tts.py` ile seslendirilir.
