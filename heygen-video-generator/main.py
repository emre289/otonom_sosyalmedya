import requests
import time
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# --- AYARLAR (Gizli bilgiler .env dosyasından okunuyor) ---
PHOTO_AVATAR_ID = os.getenv("PHOTO_AVATAR_ID")
SES_DOSYASI = os.getenv("SES_DOSYASI")
API_KEY = os.getenv("HEYGEN_API_KEY")

# Değişkenlerin yüklenip yüklenmediğini kontrol et
if not all([PHOTO_AVATAR_ID, SES_DOSYASI, API_KEY]):
    print("❌ Hata: .env dosyasındaki değişkenler eksik!")
    print("Lütfen .env.example dosyasını kopyalayıp .env olarak kaydedin ve değerleri doldurun.")
    exit(1)


def ses_yukle(dosya_yolu):
    """Ses dosyasını RAW BINARY olarak HeyGen'e yükle"""
    
    if not os.path.exists(dosya_yolu):
        print("❌ Dosya bulunamadı!")
        return None
    
    print(f"🎵 Ses dosyası yükleniyor: {dosya_yolu} ({os.path.getsize(dosya_yolu)} bytes)")
    
    # ÖNEMLİ: upload.heygen.com kullanılıyor, api.heygen.com DEĞİL!
    url = "https://upload.heygen.com/v1/asset"
    
    headers = {
        "X-Api-Key": API_KEY,
        "Content-Type": "audio/mpeg"  # Raw binary için şart!
    }
    
    # Dosyayı binary olarak oku
    with open(dosya_yolu, "rb") as f:
        ses_verisi = f.read()
    
    # files= DEĞİL, data= kullanıyoruz!
    res = requests.post(url, headers=headers, data=ses_verisi)
    
    if res.status_code != 200:
        print(f"❌ Ses yükleme hatası: {res.text}")
        return None
    
    audio_id = res.json().get("data", {}).get("id")
    print(f"✅ Ses yüklendi! ID: {audio_id}")
    return audio_id


def video_olustur(audio_id):
    """Video oluştur"""
    print(f"\n🎬 Video oluşturuluyor...")
    
    url = "https://api.heygen.com/v2/video/generate"
    headers = {"X-Api-Key": API_KEY, "Content-Type": "application/json"}
    
    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "talking_photo",
                    "talking_photo_id": PHOTO_AVATAR_ID
                },
                "voice": {
                    "type": "audio",
                    "audio_asset_id": audio_id
                }
            }
        ],
        "dimension": {
            "width": 720,
            "height": 1080  # 1:1 kare format
        }
    }
    
    res = requests.post(url, headers=headers, json=payload)
    
    if res.status_code != 200:
        print(f"❌ Video oluşturma hatası: {res.text}")
        return None
    
    video_id = res.json().get("data", {}).get("video_id")
    print(f"✅ Video başlatıldı! ID: {video_id}")
    return video_id


def video_takip(video_id):
    """Video durumunu takip et"""
    print(f"\n⏳ Video işleniyor...")
    
    # V1 endpoint kullanılmalı!
    url = "https://api.heygen.com/v1/video_status.get"
    headers = {"X-Api-Key": API_KEY}
    
    while True:
        res = requests.get(url, headers=headers, params={"video_id": video_id})
        
        if res.status_code != 200:
            print(f"API Hatası: {res.status_code}")
            time.sleep(5)
            continue
        
        data = res.json().get("data", {})
        status = data.get("status")
        
        if status == "completed":
            print("\n" + "★" * 40)
            print("🎉 VİDEO HAZIR!")
            print(f"⬇️ İNDİR: {data.get('video_url')}")
            print("★" * 40)
            return data.get('video_url')
        
        elif status == "failed":
            print(f"\n❌ BAŞARISIZ: {data.get('error')}")
            return None
        
        else:
            print(f"⏳ Durum: {status}...", end="\r")
            time.sleep(5)


def main():
    # 1. Ses dosyasını yükle (RAW BINARY)
    audio_id = ses_yukle(SES_DOSYASI)
    if not audio_id:
        return
    
    # 2. Video oluştur
    video_id = video_olustur(audio_id)
    if not video_id:
        return
    
    # 3. Takip et
    video_takip(video_id)


if __name__ == "__main__":
    main()