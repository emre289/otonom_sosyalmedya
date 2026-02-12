# Heygen Video Generator Skill

Bu modül, Minimax sesini Heygen avatar videosuna uygular.

## Dosyalar
- `main.py`: API çağrıları ve video üretimi
- `requests.txt`: bağımlılıklar

## Kurulum
```bash
pip install -r requests.txt
```

## Yapılandırma
`.env` dosyası oluşturun ve aşağıdaki alanları girin:
```
HEYGEN_API_KEY=...
PHOTO_AVATAR_ID=...
SES_DOSYASI=.../ses.mp3
```

## Kullanım
```bash
python main.py
```

## Kadraj ve Yerleşim (9:16)
- Çıktı formatı: 1080x1920
- Karakter: ekranın ortasında, toplam yüksekliğin %50'si
- Çerçeve: hafif parlak mavi, yumuşak radius
- Arka plan: koyu mavi, yavaş hareketli gradient

Not: `main.py` içindeki `dimension` alanını 1080x1920 olarak ayarlayın.

## Entegrasyon
- Heygen çıktısı doğrudan nihai video çıktısı olarak kullanılır.
