# ZK Studio AI Assistant

> **ZK Studio Architecture & Design** için geliştirilen yapay zekâ destekli asistan ve lead yönetim sistemi.

##  Proje Hakkında

Bu proje, ZK Studio web sitesi ziyaretçilerinin **yapay zekâ destekli bir asistan** ile mimarlık, iç mimarlık ve tasarım konularında etkileşim kurmasını ve iletişim bilgilerini bırakmasını sağlayan bir **MVP** uygulamasıdır.

Sistem iki temel arayüzden oluşmaktadır:

- **B2C AI Asistan** — Ziyaretçilerin yapay zekâ ile sohbet ettiği arayüz.
- **B2B Yönetim Paneli** — ZK Studio'ya bırakılan lead kayıtlarının görüntülendiği panel.

##  Özellikler

###  AI Asistan

Kullanıcılar mimarlık, iç mimarlık ve tasarım konularında soru sorabilir.

Örnek:

`Modern bir ev tasarlarken nelere dikkat etmeliyim?`

API:

`POST /api/sohbet`

###  Lead Yönetimi

Kullanıcıdan aşağıdaki bilgiler alınarak lead kaydı oluşturulur:

- Ad Soyad
- Telefon
- Not

API:

`POST /api/leads`

Lead kayıtlarını görüntülemek için:

`GET /api/leads`

###  Yönetim Paneli

ZK Studio'ya bırakılan lead kayıtları **B2B Yönetim Paneli** üzerinden görüntülenmektedir.

##  Kullanılan Teknolojiler

| Teknoloji | Kullanım Alanı |
|---|---|
| Python | Backend |
| Flask | API geliştirme |
| Groq API | Yapay zekâ servisi |
| Wix Velo | Frontend |
| JavaScript | Wix bağlantıları |
| Flask-CORS | API bağlantısı |
| python-dotenv | Ortam değişkenleri |
| Gunicorn | Production server |
| Render | Backend deployment |
| GitHub | Versiyon kontrolü |

##  API Yapısı

### Sağlık Kontrolü

`GET /health`

Örnek cevap:

```json
{
  "status": "ok"
}
```

### AI Sohbet

Kullanıcıların mimarlık, iç mimarlık ve tasarım konularında soru sorabildiği yapay zekâ destekli sohbet sistemi.

`POST /api/sohbet`

Örnek istek:

```json
{
  "mesaj": "Modern bir ev tasarlarken nelere dikkat etmeliyim?"
}
```
### Lead Yönetimi

Kullanıcıdan aşağıdaki bilgiler alınarak lead kaydı oluşturulur:

- Ad Soyad
- Telefon
- Not

`POST /api/leads`

Lead kayıtlarını görüntülemek için:

`GET /api/leads`

##  Kullanılan Teknolojiler

| Teknoloji | Kullanım Alanı |
|---|---|
| Python | Backend |
| Flask | API geliştirme |
| Groq API | Yapay zekâ servisi |
| Wix Velo | Frontend |
| JavaScript | Wix bağlantıları |
| GitHub | Versiyon kontrolü |
| Render | Yayınlama |

##  Proje Yapısı

```text
test/
├── run.py
├── test.py
├── requirements.txt
├── README.md
└── .gitignore
```
##  Yayınlama

Backend **GitHub + Render** üzerinden yayınlanmıştır.

**Build Command:**

`pip install -r requirements.txt`

**Start Command:**

`gunicorn run:app`

Hassas bilgiler environment variables üzerinden yönetilmektedir.

>  **Güvenlik Notu:** API anahtarları GitHub üzerinde paylaşılmamalı ve `.env` dosyası repository içerisinde bulunmamalıdır.
##  Sistem Akışı

### AI Asistan Akışı

```text
Ziyaretçi
    ↓
Wix B2C Arayüzü
    ↓
Flask API
    ↓
Groq AI
    ↓
AI Cevabı
```
Ziyaretçi
    ↓
Lead Formu
    ↓
POST /api/leads
    ↓
Lead Kaydı
    ↓
B2B Yönetim Paneli

##  Proje Kontrol Listesi

- [x] Flask backend oluşturuldu
- [x] AI sohbet sistemi oluşturuldu
- [x] `/health` endpointi oluşturuldu
- [x] Lead kayıt sistemi oluşturuldu
- [x] B2C AI Asistan arayüzü oluşturuldu
- [x] B2B Yönetim Paneli oluşturuldu
- [x] Wix Velo bağlantıları tamamlandı
- [x] GitHub repository oluşturuldu
- [x] Render deployment tamamlandı
- [x] Canlı sistem test edildi

##  Proje Amacı

ZK Studio Architecture & Design için **yapay zekâ destekli müşteri iletişimi ve lead toplama sürecini dijitalleştiren**, web tabanlı bir MVP geliştirmektir.

> **Proje Durumu:** MVP tamamlandı ve canlı ortamda çalışmaktadır.
