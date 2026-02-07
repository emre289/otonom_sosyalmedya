#!/usr/bin/env python3
"""
Minimax Text-to-Speech API Client
Turkce metinleri seslendirme
"""

import requests
import json
import os
import sys
from dotenv import load_dotenv

# .env dosyasini yukle
load_dotenv()

# API bilgilerini .env'den al
API_KEY = os.getenv("MINIMAX_API_KEY")
GROUP_ID = os.getenv("MINIMAX_GROUP_ID")
VOICE_ID = os.getenv("MINIMAX_VOICE_ID")

# Kontrol et
if not all([API_KEY, GROUP_ID, VOICE_ID]):
    print("[HATA] .env dosyasinda gerekli bilgiler eksik!")
    print("MINIMAX_API_KEY, MINIMAX_GROUP_ID ve MINIMAX_VOICE_ID gerekli.")
    sys.exit(1)

# API ayarlari
ENDPOINT = "https://api.minimax.io/v1/t2a_v2"
OUTPUT_FILE = "ses.mp3"

# Varsayilan ayarlar
DEFAULT_SPEED = 1.2
DEFAULT_VOLUME = 1.2


def text_to_speech(text, speed=DEFAULT_SPEED, volume=DEFAULT_VOLUME):
    """Metni sese cevir"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    params = {
        "GroupId": GROUP_ID
    }

    payload = {
        "model": "speech-2.8-hd",
        "text": text,
        "voice_setting": {
            "voice_id": VOICE_ID,
            "speed": speed,
            "vol": volume,
            "pitch": 0
        },
        "audio_setting": {
            "sample_rate": 24000,
            "bitrate": 128000,
            "format": "mp3",
            "channel": 1
        },
        "language": "tr"
    }

    print("="*60)
    print("MINIMAX TEXT-TO-SPEECH")
    print("="*60)
    print(f"Metin uzunlugu: {len(text)} karakter")
    print(f"Hiz: {speed}")
    print(f"Ses: {volume}")
    print("="*60)

    try:
        print("\nAPI'ye istek gonderiliyor...")
        response = requests.post(ENDPOINT, params=params, headers=headers, json=payload, timeout=30)

        if response.status_code == 200:
            data = response.json()

            # Hata kontrolu
            if 'base_resp' in data and data['base_resp'].get('status_code') != 0:
                print(f"\n[HATA] {data['base_resp'].get('status_msg')}")
                return False

            # Audio data'yi al
            audio_field = None
            if 'data' in data and 'audio' in data['data']:
                audio_field = data['data']['audio']
            elif 'audio' in data:
                audio_field = data['audio']

            if audio_field:
                try:
                    # Hex formatindan decode et
                    audio_data = bytes.fromhex(audio_field)
                    with open(OUTPUT_FILE, 'wb') as f:
                        f.write(audio_data)

                    size = os.path.getsize(OUTPUT_FILE)
                    print(f"\n[BASARILI]")
                    print(f"Dosya: {OUTPUT_FILE}")
                    print(f"Boyut: {size:,} bytes ({size/1024:.1f} KB)")

                    # Windows'ta otomatik oynat
                    if os.name == 'nt':
                        print("\nOynatiliyor...")
                        os.system(f'start "" "{OUTPUT_FILE}"')

                    return True

                except Exception as e:
                    print(f"\n[HATA] Decode hatasi: {e}")
                    return False
            else:
                print("\n[HATA] Audio verisi bulunamadi!")
                return False
        else:
            print(f"\n[HATA] HTTP {response.status_code}")
            return False

    except Exception as e:
        print(f"\n[HATA] {e}")
        return False
    finally:
        print("\n" + "="*60)


def main():
    """Ana fonksiyon"""

    # Metin al
    if len(sys.argv) > 1:
        # Komut satirindan
        text = " ".join(sys.argv[1:])
    else:
        # Kullanicidan
        print("\nMinimax TTS - Turkce Seslendirme\n")
        text = input("Metin girin: ")

    if not text.strip():
        print("[HATA] Metin bos olamaz!")
        sys.exit(1)

    # Seslendirme yap
    success = text_to_speech(text)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
