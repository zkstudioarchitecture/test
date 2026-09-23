import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "service": "ZK Studio AI Assistant"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/api/sohbet", methods=["POST"])
def sohbet():

    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "hata": "JSON verisi alınamadı."
            }), 400

        mesaj = str(data.get("mesaj", "")).strip()

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
                        "ZK Studio hakkında bilmediğin bilgileri uydurma."
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

        print("HATA TIPI:", type(error).__name__)
        print("HATA:", repr(error))

        return jsonify({
            "hata": str(error)
        }), 500


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
