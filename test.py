from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)
CORS(app)



@app.route("/")
def ana_sayfa():
    return "ZK Studio Python servisi çalışıyor!"


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
    soru = data.get("soru", "")

    cevap = client.chat.completions.create(
        model="openai/gpt-oss-120b",
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


if __name__ == "__main__":
    app.run(debug=True)