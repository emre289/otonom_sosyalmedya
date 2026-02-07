# otonom_sosyalmedya

Bu repo, uçtan uca otonom sosyal medya video üretim hattını tek yerde toplar. Amaç; **konu -> konuşma metni -> ses -> avatar video -> dinamik montaj** akışını standardize etmek ve adım adım onayla ilerlemektir.

## Genel Akış
1. **sosyal_medya_prompt**
   - Kullanıcıdan gelen herhangi bir `konu`dan **Türkçe konuşma metni** üretir.
   - Kurallar `talimatlar.md` / `talimatlar.json` içindeki yönergelere göre uygulanır.

2. **minimax**
   - Üretilen konuşma metni Minimax API'ye gönderilir.
   - Sonuç: **ses dosyası** (ör. `ses.mp3`).

3. **heygen-video-generator**
   - Minimax ses dosyası Heygen'e gönderilir.
   - Sonuç: **avatar konuşma videosu**.
   - Bu adım **uzun sürebilir**.

4. **remotion**
   - Heygen videosu ve Minimax sesini alır.
   - **9:16** formatta dinamik kartlar, grafikler, animasyonlar ve görsel katmanlar ekler.
   - Sonuç: **final video** (dinamik görsellerle destekli).
   - Bu adım **uzun sürebilir**.

## Agent Çalışma Kuralları (Onaylı Aşamalar)
Agent her adımı tamamladığında kullanıcıdan **onay almak zorundadır**. Onay gelmeden bir sonraki aşamaya geçmez.

Her adım sonrasında agent'ın göndereceği şablon:

✅ ADIM X TAMAM!

X dosyası gönderildi

Onayın nedir?

A) ✅ Tamam, devam et
B) Değişiklik yap
C) ❌ Hayır, iptal

## Zamanlama ve Takip (Heygen + Remotion)
Heygen ve Remotion adımları uzun sürebileceği için agent şu şekilde davranır:

- **Heygen aşaması:**

  ### ⛔ KRİTİK UYARI — HEYGEN İSTEK LİMİTİ ⛔

  **Agent, HeyGen API'ye TEK BİR İSTEK atar. İkinci istek YASAKTIR.**

  Kurallar:
  1. Agent, HeyGen'e **yalnızca 1 (bir) kez** video oluşturma isteği gönderir.
  2. İstek gönderildikten sonra agent **bekler**. Durum kontrolünü (status polling) her 1 dakikada bir yapar ama **yeni bir video oluşturma isteği KESINLIKLE göndermez**.
  3. Herhangi bir hata alınırsa (timeout, API hatası, 4xx, 5xx vb.) agent **ikinci bir istek ATMAZ**. Bunun yerine:
     - Hatayı olduğu gibi kullanıcıya bildirir.
     - Kullanıcıdan talimat bekler.
     - Kullanıcı açıkça "tekrar dene" demedikçe agent hiçbir şekilde yeniden istek göndermez.
  4. **Retry, tekrar deneme, otomatik yeniden gönderim gibi davranışlar tamamen yasaktır.**
  5. Bu kural istisnasızdır. Agent ne kadar emin olursa olsun, kendi başına ikinci bir HeyGen isteği atamaz.

  > **Neden?** HeyGen API'de her istek kredi harcar. Gereksiz veya tekrarlanan istekler doğrudan maliyet oluşturur. Bu yüzden agent **tek atış** kuralına uymak zorundadır.

  - Video üretimi başladıktan sonra agent **her 1 dakikada bir** durum kontrolü yapar (bu sadece status check'tir, yeni istek DEĞİLDİR).
  - Video biter bitmez kullanıcıdan beklemeden **sonucu iletir**.
  - Ardından onay ister.

- **Remotion aşaması:**
  - Render başladıktan sonra agent **her 1 dakikada bir** durum kontrolü yapar.
  - Render biter bitmez kullanıcıdan beklemeden **final videoyu iletir**.
  - Ardından onay ister.

## Remotion Detayları
Remotion katmanı; görsel dinamizm ve senkronizasyonu sağlar:
- Konuşma metnine göre **zaman damgalı kartlar**
- Kısa başlık + açıklama kartları
- Grafik/ikon **pulse** animasyonları
- Koyu mavi arka plan + hafif glow efektleri
- Heygen videosu merkezde, mavi çerçeve içinde
- 9:16 safe-area uyumu

## Amaç
Bu sayfaya gelen agent, akışın **ne yaptığını** ve **nasıl onayla ilerlemesi gerektiğini** net şekilde görmelidir.
