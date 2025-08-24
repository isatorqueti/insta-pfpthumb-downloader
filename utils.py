import re
import requests
import instaloader

# Função pra baixar a pfp
def download_pfp(usuario):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, usuario)
    url_imagem = profile.profile_pic_url
    imagem = requests.get(url_imagem).content
    nome_arquivo = f"{usuario}_pfp.jpg"
    with open(nome_arquivo, "wb") as f:
        f.write(imagem)
    return nome_arquivo

# Função pra baixar a thumbnail reels
def download_thumbnail(url: str, nome_arquivo: str = ""):
    L = instaloader.Instaloader(download_pictures=False, download_videos=False, download_video_thumbnails=False)
    match = re.search(r"(?:reel|p)/([A-Za-z0-9_-]+)", url)
    if not match:
        raise ValueError("Não foi possível completar o download")
    shortcode = match.group(1)
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    if nome_arquivo == "":
        nome_arquivo = f"{post.owner_username}thumb.jpg"
    thumb_url = post.url
    response = requests.get(thumb_url)
    response.raise_for_status()
    with open(nome_arquivo, "wb") as f:
        f.write(response.content)
    return nome_arquivo

# Função pra baixar a thumbnail tiktok
def download_tiktok_thumbnail(url: str, nome_arquivo: str = ""):
    api_url = "https://www.tiktok.com/oembed"
    params = {'url': url}
    response = requests.get(api_url, params=params)
    data = response.json()
    thumb_url = data.get('thumbnail_url')
    username = data.get('author_name', 'tiktok')
    if nome_arquivo == "":
        nome_arquivo = f"{username}tiktokthumb.jpg"
    thumb_response = requests.get(thumb_url)
    with open(nome_arquivo, "wb") as f:
        f.write(thumb_response.content)
    return nome_arquivo, thumb_url
