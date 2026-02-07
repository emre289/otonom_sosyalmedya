# Remotion Skill

Bu modül, Minimax sesine senkron görsel katmanlar üretmek için Remotion tabanlı şablondur.

## Kurulum
```bash
npm install
```

## Önizleme
```bash
npm run preview
```

## Render
Örnek render (props ile):
```bash
npm run render -- StoryVideo out/video.mp4 --props='{"title":"Baslik","subtitle":"Kisa aciklama","cards":[{"start":15,"end":120,"title":"Kanca","body":"Ilk 3 saniyede vurgu"}],"heygenVideoSrc":"video/heygen.mp4","audioSrc":"audio/ses.mp3"}'
```

## Dosya Yapısı
- `src/compositions/StoryVideo.tsx`: ana kompozisyon
- `public/video/`: Heygen çıktısı
- `public/audio/`: Minimax ses dosyası

## Görsel Kurallar
- 9:16 kompozisyon
- Koyu mavi dinamik arka plan
- Merkezde Heygen video çerçevesi
- Bilgi kartları: hızlı giriş/çıkış + glow
