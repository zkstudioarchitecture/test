#import os
#from dotenv import load_dotenv

#load_dotenv()

#api_key = os.getenv("GROQ_API_KEY")

#print("Anahtar yüklendi" , api_key)

#from groq import Groq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")

# client = Groq(api_key=api_key)

# cevap = client.chat.completions.create(

#     model="openai/gpt-oss-120b",
#     messages=[{"role":"system", "content": "Sen Deneyimli bir Python eğitmeni misin?"
#                                             "Cevapları kısa ve öz bir şekilde ver"},
#         {
#             "role":"user",
#             "content":"Liste nedir?"
#         }]
# )

# mesaj= cevap.choices[0].message.content
# print(mesaj)

# from groq import Groq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")

# client = Groq(api_key=api_key)

# cevap = client.chat.completions.create(

#     model="openai/gpt-oss-120b",
#     messages=[ {
#             "role":"user",
#             "content":"Python nedir?"
#         }],
#         temperature=0.2,
#         max_tokens=150,

# )

# mesaj= cevap.choices[0].message.content
# print(mesaj)

# kullanim=cevap.usage
# print("Gönderilen", kullanim.prompt_tokens)
# print("Alınan", kullanim.completion_tokens)
# print("Toplam", kullanim.total_tokens)

# from groq import Groq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")

# client = Groq(api_key=api_key)
# while True:


#     soru = input("Siz: ")


#     if soru.lower() in ["q", "çıkış", "exit"]:
#         print("Görüşmek üzere!")
#         break


#     cevap = client.chat.completions.create(
#         model="openai/gpt-oss-120b",
#         messages=[
#             {
#                 "role": "user",
#                 "content": soru
#             }
#         ]
#     )
#     print("Bot:", cevap.choices[0].message.content)

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

print("Bot", end="")

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

cevap = client.chat.completions.create(

     model="openai/gpt-oss-120b",
     messages=[ {
             "role":"user",
             "content":"Python nedir?"
         }],

    stream=True


 )

for parca in cevap:
    icerik = parca.choices[0].delta.content
    if icerik is not None:
        print(icerik, end="", flush=True)

print()
