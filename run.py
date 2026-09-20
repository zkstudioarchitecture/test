import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY bulunamadı.")

client = Groq(api_key=api_key)


@app.route("/")
def home():
    return "ZK Studio Python servisi çalışıyor!"


@app.route("/health")
def health():
    return jsonify({
        "durum": "aktif"
    })


@app.route("/api/sohbet", methods=["POST"])
def sohbet():
    try:
        data = request.get_json()

        soru = data.get("soru")

        if not soru:
            return jsonify({
                "hata": "Soru gönderilmedi."
            }), 400

        cevap = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "Sen ZK Studio Architecture & Design için çalışan bir AI asistansın. Mimarlık, tasarım, 3D görselleştirme ve yarışma projeleri hakkında kısa ve anlaşılır cevaplar ver."
                },
                {
                    "role": "user",
                    "content": soru
                }
            ],
            temperature=0.2,
            max_tokens=300
        )

        mesaj = cevap.choices[0].message.content

        return jsonify({
            "cevap": mesaj
        })

    except Exception as e:
        return jsonify({
            "hata": str(e)
        }), 500


if __name__ == "__main__":
    app.run()
