import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Groq API
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "service": "ZK Studio AI Assistant"
    })


@app.route("/api/sohbet", methods=["POST"])
def sohbet():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "hata": "Veri gönderilmedi."
            }), 400

        mesaj = data.get("mesaj", "").strip()

        if not mesaj:
            return jsonify({
                "hata": "Mesaj boş olamaz."
            }), 400

        print("Gelen mesaj:", mesaj)

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": """
Sen ZK Studio Architecture & Design'in
web sitesinde çalışan AI asistansın.

ZK Studio; mimarlık, iç mimarlık,
ulaşım ve kentsel tasarım, 3D görselleştirme
ve mimari yarışma projeleri üzerine çalışan
bir tasarım stüdyosudur.

Kullanıcılara ZK Studio hakkında,
mimarlık, tasarım, projeler ve hizmetler
konusunda yardımcı ol.

Cevaplarını Türkçe ver.

Kullanıcının sorduğu soruya doğrudan cevap ver.
Her soruya aynı cevabı verme.

Bilmediğin bir konuda bilgi uydurma.
"""
                },

                {
                    "role": "user",
                    "content": mesaj
                }
            ],

            temperature=0.7,

            max_tokens=500
        )

        cevap = response.choices[0].message.content

        print("Groq cevabı:", cevap)

        return jsonify({
            "cevap": cevap
        }), 200


    except Exception as error:

        print("HATA:", error)

        return jsonify({
            "hata": "AI yanıtı oluşturulurken bir hata oluştu."
        }), 500


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
