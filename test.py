from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)
CORS(app)

# Lead kayıtları
leads = []


@app.route("/")
def ana_sayfa():
    return "ZK Studio Python servisi çalışıyor!"


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/hakkimda")
def hakkimda():
    return "ZK Studio Architecture & Design"


@app.route("/selam/<isim>")
def selam(isim):
    return f"Merhaba, {isim}!"


@app.route("/kare/<int:sayi>")
def kare(sayi):
    sonuc = sayi * sayi
    return f"{sayi} sayısının karesi: {sonuc}"


@app.route("/ara")
def ara():
    kelime = request.args.get("kelime", "")
    limit = request.args.get("limit", 10)

    return jsonify({
        "aranan": kelime,
        "limit": limit,
        "sonuc": f"'{kelime}' için arama yapıldı"
    })


@app.route("/api/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json()
    soru = data.get("mesaj", "")

    cevap = client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "system",
                "content": "Sen ZK Studio Architecture & Design için çalışan bir yapay zeka asistanısın. Mimarlık, iç mimarlık, tasarım ve ZK Studio hizmetleri hakkında profesyonel ve anlaşılır cevaplar ver."
            },
            {
                "role": "user",
                "content": soru
            }
        ]
    )

    return jsonify({
        "cevap": cevap.choices[0].message.content
    })


# Lead kaydetme
@app.route("/api/leads", methods=["POST"])
def lead_ekle():
    data = request.get_json()

    isim = data.get("isim", "")
    telefon = data.get("telefon", "")
    notu = data.get("not", "")

    if not isim or not telefon:
        return jsonify({
            "hata": "İsim ve telefon zorunludur."
        }), 400

    yeni_lead = {
        "_id": str(len(leads) + 1),
        "isim": isim,
        "telefon": telefon,
        "not": notu
    }

    leads.append(yeni_lead)

    return jsonify({
        "mesaj": "Lead başarıyla kaydedildi.",
        "lead": yeni_lead
    }), 201


# Lead listesini getir
@app.route("/api/leads", methods=["GET"])
def leadleri_getir():
    return jsonify(leads)


if __name__ == "__main__":

    app.run(debug=True)

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def ana_sayfa():
#     return"Merhaba, Flask çalışıyor"

# @app.route("/hakkimda")
# def hakkimda():
#     return"Bu bir Python servisidir"

# if __name__ == "__main__":
#     app.run(debug= True)

# from flask import Flask

# app = Flask(__name__)



# # URL'den isim yakala
# @app.route("/selam/<isim>")
# def selam(isim):
#     return f"Merhaba, {isim}!"

# # Sadece sayı kabul et
# @app.route("/kare/<int:sayi>")
# def kare(sayi):
#     sonuc = sayi * sayi
#     return f"{sayi} sayısının karesi: {sonuc}"

# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # URL'den isim yakala
# @app.route("/selam/<isim>")
# def selam(isim):
#     return f"Merhaba, {isim}!"


# # Sadece sayı kabul et
# @app.route("/kare/<int:sayi>")
# def kare(sayi):
#     sonuc = sayi * sayi
#     return f"{sayi} sayısının karesi: {sonuc}"


# # Query parametrelerini oku
# # Örnek: /ara?kelime=python&limit=5
# @app.route("/ara")
# def ara():
#     kelime = request.args.get("kelime", "")
#     limit = request.args.get("limit", 10)

#     return jsonify({
#         "aranan": kelime,
#         "limit": limit,
#         "sonuc": f"'{kelime}' için arama yapıldı"
#     })


# if __name__ == "__main__":
#     app.run(debug=True)

