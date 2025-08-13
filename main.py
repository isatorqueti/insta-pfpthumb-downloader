import requests
import instaloader

L = instaloader.Instaloader()

usuario = "isatorqueti"
url_imagem = instaloader.Profile.from_username(L.context, usuario).profile_pic_url

imagem = requests.get(url_imagem).content

with open(f"{usuario}.jpg", "wb") as f:
    f.write(imagem)

print("imagem salva")