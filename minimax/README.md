# Minimax Text-to-Speech Client

Minimax API kullanarak Türkçe metinleri seslendirme aracı.

## Özellikler

- ✅ Türkçe seslendirme desteği
- 🎚️ Hız ve ses seviyesi ayarları
- 🎤 Özel voice clone desteği
- 📦 Basit kurulum ve kullanım

## Kurulum

### 1. Gereksinimler

```bash
pip install -r requirements.txt
```

### 2. API Anahtarlarını Ayarlayın

`.env.example` dosyasını `.env` olarak kopyalayın:

```bash
cp .env.example .env
```

`.env` dosyasını düzenleyin ve kendi bilgilerinizi girin:

```env
MINIMAX_API_KEY=your-api-key-here
MINIMAX_GROUP_ID=your-group-id-here
MINIMAX_VOICE_ID=your-voice-id-here
```

**API anahtarlarını nereden alabilirsiniz?**
- https://platform.minimax.io/ adresine gidin
- Account Management > API Keys bölümünden API Key alın
- Group ID'nizi Settings bölümünden bulun
- Voice ID için sistem seslerinden birini kullanın veya kendi voice clone'unuzu oluşturun

## Kullanım

### Komut satırından:

```bash
python minimax_tts.py "Merhaba, bu bir test mesajıdır."
```

### İnteraktif mod:

```bash
python minimax_tts.py
```

Program sizden metin girmenizi isteyecektir.

### Örnek:

```bash
python minimax_tts.py "Dünya nüfusunun yüzde 80'i bunu bilmiyor! Bakın olay şu, yapay zeka teknolojisi artık Türkçe'yi de destekliyor."
```

## Sistem Sesleri

Varsayılan Türkçe sesler:
- `Turkish_CalmWoman` - Sakin Kadın Sesi
- `Turkish_Trustworthyman` - Güvenilir Erkek Sesi

Kendi voice clone'unuzu da kullanabilirsiniz.

## Çıktı

Seslendirilen metin `ses.mp3` dosyası olarak kaydedilir ve otomatik olarak oynatılır (Windows).

## Ayarlar

Varsayılan ayarlar:
- **Hız:** 1.2
- **Ses Seviyesi:** 1.2
- **Ton:** 0
- **Model:** speech-2.8-hd

## Lisans

MIT

## Katkıda Bulunma

Pull request'ler memnuniyetle karşılanır!

## Sorun Giderme

**"invalid api key" hatası:**
- API Key'inizin doğru olduğundan emin olun
- `.env` dosyasında boşluk olmadığından emin olun
- Doğru API host kullandığınızdan emin olun (`api.minimax.io`)

**"insufficient balance" hatası:**
- Minimax hesabınızda yeterli kredi olduğundan emin olun
- API erişimi olan bir plan kullandığınızdan emin olun

**"voice id not exist" hatası:**
- Voice ID'nizin doğru olduğundan emin olun
- Sistem seslerinden birini kullanmayı deneyin: `Turkish_CalmWoman` veya `Turkish_Trustworthyman`
