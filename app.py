from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.route("/")
def ana_sayfa():
    return "ZK Studio API çalışıyor!"


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/api/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json()
    soru = data.get("mesaj", "")

    cevap = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen ZK Studio Architecture & Design için "
                    "çalışan bir yapay zeka asistanısın. "
                    "Mimarlık, tasarım, 3D görselleştirme ve "
                    "ZK Studio hizmetleri hakkında profesyonel "
                    "ve anlaşılır cevaplar ver."
                )
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


if __name__ == "__main__":
    app.run()