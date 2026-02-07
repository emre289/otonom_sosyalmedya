# Viral İçerik Seslendirme Prompt

Viral sosyal medya içeriği için Türkçe seslendirme metni üretmek için optimize edilmiş yapay zeka promptu.

## 📋 Dosyalar

- **talimatlar.md** - Markdown formatında prompt (AI asistanlar için)
- **talimatlar.json** - JSON formatında prompt (programatik kullanım için)

## 🎯 Ne İşe Yarar?

Bu prompt, verdiğiniz bir konu, link, görsel, metin veya videodan:
- ✅ Yapay zeka seslendirme (TTS) için optimize edilmiş
- ✅ Viral içerik formatında (Problem-Interrupt Hybrid)
- ✅ Türkçe konuşma metni üretir

## 🚀 Kullanım

### ChatGPT / Claude / Gemini ile:

1. `talimatlar.md` dosyasını açın
2. İçeriği kopyalayın
3. AI asistanınıza yapıştırın
4. Konu verin ve seslendirme metnini alın

### Programatik Kullanım:

```python
import json

# JSON promptu yükle
with open('talimatlar.json', 'r', encoding='utf-8') as f:
    prompt = json.load(f)

# API'nize gönderin
# ...
```

## 📝 Özellikler

### ✅ Dil Kuralları
- Çıktı **her zaman Türkçe**
- Yabancı terimler **Türkçe okunuşuyla** yazılır
  - ChatGPT → "Çet Ci Pi Ti"
  - Elon Musk → "İlon Mask"

### ✅ Metin Yapısı
1. **Şok Açılış** - Dikkat çekici başlangıç
2. **Merak Yaratma** - İzleyiciyi içeri çek
3. **Bilgi Bombardımanı** - Hızlı, dinamik bilgi akışı
4. **Kapanış Kancası** - Etkileşim teşvik et

### ✅ Format
- Düz, akıcı konuşma metni
- Liste veya madde işareti yok
- Maksimum 2 dakika

## 📌 Örnek Çıktı

```
Dünya nüfusunun yüzde 80'i bunu bilmiyor! Bakın olay şu,
geçtiğimiz hafta yayınlanan bir araştırmaya göre bu teknoloji
sessiz sedasız hayatımıza girdi. Rakamlar ortada. 2024'te bu
oran yüzde 45'e ulaştı ve her geçen gün artıyor. Ve en kötüsü,
kimse bunu konuşmuyor! Peki şimdi asıl soru şu, bu bizim
hayatımızı nasıl etkileyecek? Ama iyi haber şu ki, çözüm
aslında düşündüğünüzden çok daha basit.
```

## ⚠️ Önemli Notlar

- **Sadece seslendirme metni** üretilir
- Giriş/kapanış cümleleri **yok**
- Açıklama, yorum **yok**
- Direkt TTS aracına yapıştırılabilir

## 🔄 Versiyon Geçmişi

### v3.0 (2026-02-07)
- ❌ Duygu etiketleme kaldırıldı (API uyumluluğu için)
- ✅ JSON format eklendi
- ✅ Daha basit ve temiz yapı

### v2.0
- Duygu etiketleme sistemi
- Detaylı kurallar

### v1.0
- İlk versiyon

## 📜 Lisans

MIT

## 🤝 Katkıda Bulunma

Pull request'ler memnuniyetle karşılanır!
