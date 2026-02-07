# Minimax Skill

Bu modül, sosyal medya metnini Minimax API ile sese çevirir.

## Dosyalar
- `minimax_tts.py`: TTS istemcisi
- `.env.example`: API anahtarları şablonu

## Kurulum
```bash
pip install -r requirements.txt
```

PowerShell ile `.env` oluşturma:
```powershell
Copy-Item .env.example .env
```

`.env` değişkenleri:
```
MINIMAX_API_KEY=...
MINIMAX_GROUP_ID=...
MINIMAX_VOICE_ID=...
```

## Kullanım
```bash
python minimax_tts.py "Konuya gore uretilmis metin"
```

## Çıktı
- `ses.mp3` dosyası üretir
- Dosya Heygen modülüne giriş olarak verilir

## Video Senkron Rehberi
- 2-4 saniyede bir bilgi kartı
- 0.3-0.6s giriş, 0.2-0.4s çıkış animasyonu
- Kısa başlıklar (6-8 kelime)
- Vurgu anlarında grafik/ikon pulse
