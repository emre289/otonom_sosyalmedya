import os
import subprocess
import time

import requests
from dotenv import load_dotenv

# .env dosyasini yukle
load_dotenv()

# Gizli bilgiler .env dosyasindan okunuyor
PHOTO_AVATAR_ID = os.getenv("PHOTO_AVATAR_ID")
SES_DOSYASI = os.getenv("SES_DOSYASI")
API_KEY = os.getenv("HEYGEN_API_KEY")

# Gerekli degiskenleri dogrula
if not all([PHOTO_AVATAR_ID, SES_DOSYASI, API_KEY]):
    print("Hata: .env dosyasindaki degiskenler eksik!")
    print("Lutfen .env.example dosyasini kopyalayip .env olarak kaydedin ve degerleri doldurun.")
    raise SystemExit(1)


def mp3_to_wav(mp3_path):
    """MP3 dosyasini WAV formatina cevir"""
    wav_path = mp3_path.replace(".mp3", ".wav")
    print("MP3 -> WAV donusturuluyor...")
    subprocess.run(["ffmpeg", "-i", mp3_path, wav_path, "-y"], check=True)
    print(f"WAV dosyasi olusturuldu: {wav_path}")
    return wav_path


def ses_yukle(dosya_yolu):
    """Ses dosyasini RAW BINARY olarak HeyGen'e yukle"""
    if not os.path.exists(dosya_yolu):
        print("Dosya bulunamadi!")
        return None

    print(f"Ses dosyasi yukleniyor: {dosya_yolu} ({os.path.getsize(dosya_yolu)} bytes)")

    url = "https://upload.heygen.com/v1/asset"
    headers = {
        "X-Api-Key": API_KEY,
        "Content-Type": "audio/x-wav",
    }

    with open(dosya_yolu, "rb") as f:
        ses_verisi = f.read()

    res = requests.post(url, headers=headers, data=ses_verisi)

    if res.status_code != 200:
        print(f"Ses yukleme hatasi: {res.text}")
        return None

    audio_id = res.json().get("data", {}).get("id")
    print(f"Ses yuklendi! ID: {audio_id}")
    return audio_id


def video_olustur(audio_id):
    """Video olustur"""
    print("\nVideo olusturuluyor...")

    url = "https://api.heygen.com/v2/video/generate"
    headers = {"X-Api-Key": API_KEY, "Content-Type": "application/json"}

    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "talking_photo",
                    "talking_photo_id": PHOTO_AVATAR_ID,
                },
                "voice": {
                    "type": "audio",
                    "audio_asset_id": audio_id,
                },
            }
        ],
        "dimension": {
            "width": 720,
            "height": 1280,
        },
    }

    res = requests.post(url, headers=headers, json=payload)

    if res.status_code != 200:
        print(f"Video olusturma hatasi: {res.text}")
        return None

    video_id = res.json().get("data", {}).get("video_id")
    print(f"Video baslatildi! ID: {video_id}")
    return video_id


def video_takip(video_id):
    """Video durumunu takip et"""
    print("\nVideo isleniyor...")

    url = "https://api.heygen.com/v1/video_status.get"
    headers = {"X-Api-Key": API_KEY}

    while True:
        res = requests.get(url, headers=headers, params={"video_id": video_id})

        if res.status_code != 200:
            print(f"API hatasi: {res.status_code}")
            time.sleep(5)
            continue

        data = res.json().get("data", {})
        status = data.get("status")

        if status == "completed":
            print("\n" + "*" * 40)
            print("VIDEO HAZIR!")
            print(f"INDIR: {data.get('video_url')}")
            print("*" * 40)
            return data.get("video_url")
        if status == "failed":
            print(f"\nBASARISIZ: {data.get('error')}")
            return None

        print(f"Durum: {status}...", end="\r")
        time.sleep(5)


def main():
    # 0. MP3'u WAV'a cevir
    wav_dosya = mp3_to_wav(SES_DOSYASI)

    # 1. WAV dosyasini yukle
    audio_id = ses_yukle(wav_dosya)
    if not audio_id:
        return

    # 2. Video olustur
    video_id = video_olustur(audio_id)
    if not video_id:
        return

    # 3. Takip et
    video_takip(video_id)


if __name__ == "__main__":
    main()
