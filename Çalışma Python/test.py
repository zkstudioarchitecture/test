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

