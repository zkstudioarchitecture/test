import os
import json
import uuid

from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# =========================================================
# CORS
# =========================================================

CORS(
    app,
    resources={
        r"/*": {
            "origins": "*"
        }
    },
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
)


# =========================================================
# GROQ
# =========================================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# =========================================================
# LEAD DOSYASI
# =========================================================

LEADS_FILE = "leads.json"


def leads_yukle():

    if not os.path.exists(LEADS_FILE):
        return []

    try:
        with open(LEADS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except Exception as error:

        print("LEAD DOSYASI OKUMA HATASI:", repr(error))

        return []


def leads_kaydet(leads):

    with open(
        LEADS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            leads,
            file,
            ensure_ascii=False,
            indent=2
        )


# =========================================================
# ANA SAYFA
# =========================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "ok",
        "service": "ZK Studio AI Assistant"
    })


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "ok"
    })


# =========================================================
# AI SOHBET
# =========================================================

@app.route("/api/sohbet", methods=["POST"])
def sohbet():

    try:

        data = request.get_json(silent=True)

        if not data:

            return jsonify({
                "hata": "JSON verisi alınamadı."
            }), 400

        mesaj = str(
            data.get("mesaj", "")
        ).strip()

        if not mesaj:

            return jsonify({
                "hata": "Mesaj boş olamaz."
            }), 400

        print("GELEN MESAJ:", mesaj)

        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[

                {
                    "role": "system",

                    "content": (
                        "Sen ZK Studio Architecture & Design "
                        "web sitesinin yapay zeka asistanısın. "

                        "ZK Studio; mimarlık, iç mimarlık, "
                        "ulaşım ve kentsel tasarım, "
                        "3D görselleştirme ve mimari yarışma "
                        "projeleri üzerine çalışan bir tasarım "
                        "stüdyosudur. "

                        "Kullanıcılara Türkçe ve doğal cevaplar ver. "

                        "Sorulan soruya doğrudan cevap ver. "

                        "Her soruya aynı cevabı verme. "

                        "ZK Studio hakkında bilmediğin bilgileri "
                        "uydurma."
                    )
                },

                {
                    "role": "user",
                    "content": mesaj
                }
            ],

            temperature=0.7,

            max_completion_tokens=500
        )

        cevap = response.choices[0].message.content

        print("GROQ CEVABI:", cevap)

        return jsonify({
            "cevap": cevap
        }), 200

    except Exception as error:

        print(
            "HATA TIPI:",
            type(error).__name__
        )

        print(
            "HATA:",
            repr(error)
        )

        return jsonify({
            "hata": str(error)
        }), 500


# =========================================================
# LEAD EKLEME
# =========================================================

@app.route(
    "/api/leads",
    methods=["POST", "OPTIONS"]
)
def lead_ekle():

    # Wix CORS preflight isteği
    if request.method == "OPTIONS":

        return jsonify({
            "status": "ok"
        }), 200

    try:

        data = request.get_json(silent=True)

        if not data:

            return jsonify({
                "hata": "JSON verisi alınamadı."
            }), 400

        isim = str(
            data.get("isim", "")
        ).strip()

        telefon = str(
            data.get("telefon", "")
        ).strip()

        notu = str(
            data.get("not", "")
        ).strip()

        # Zorunlu alanlar
        if not isim:

            return jsonify({
                "hata": "İsim alanı zorunludur."
            }), 400

        if not telefon:

            return jsonify({
                "hata": "Telefon alanı zorunludur."
            }), 400

        # Mevcut leadleri getir
        leads = leads_yukle()

        # Yeni lead
        yeni_lead = {

            "_id": str(uuid.uuid4()),

            "isim": isim,

            "telefon": telefon,

            "not": notu
        }

        # Listeye ekle
        leads.append(yeni_lead)

        # Kaydet
        leads_kaydet(leads)

        print(
            "YENİ LEAD:",
            yeni_lead
        )

        return jsonify({

            "status": "success",

            "mesaj": "Lead başarıyla kaydedildi.",

            "lead": yeni_lead

        }), 201

    except Exception as error:

        print(
            "LEAD HATASI:",
            type(error).__name__
        )

        print(
            "LEAD HATASI DETAY:",
            repr(error)
        )

        return jsonify({
            "hata": str(error)
        }), 500


# =========================================================
# LEADLERİ GETİR
# =========================================================

@app.route(
    "/api/leads",
    methods=["GET"]
)
def leadleri_getir():

    try:

        leads = leads_yukle()

        return jsonify(leads), 200

    except Exception as error:

        print(
            "LEAD LİSTESİ HATASI:",
            repr(error)
        )

        return jsonify({
            "hata": str(error)
        }), 500


# =========================================================
# UYGULAMAYI BAŞLAT
# =========================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
