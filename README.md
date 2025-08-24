# Socials PFP & Thumbnail Downloader

Este projeto é uma aplicação desenvolvida em **Python** e **Streamlit** para realizar o download de **fotos de perfil (PFP = Profile Picture)** e **fotos de capa de posts (Thumbnails)** no Instagram e TikTok.

O objetivo do projeto foi fornecer uma ferramenta prática e rápida para baixar imagens públicas sem necessidade de login ou cookies.

O aplicativo web está disponível publicamente no Streamlit Cloud.
🔗 ~link aqui~

## 📌 Contexto do Projeto
O projeto foi desenvolvido a partir de uma demanda real do time de Business Intelligence da Publination, empresa da qual faço parte. O objetivo é facilitar a inserção das imagens em relatórios e reports de clientes. Antes, o time precisava tirar print da tela ou recorrer a sites de externos com links suspeitos e anúncios invasivos.

## 🚀 Funcionalidades 
- Preview de imagens antes de fazer o download diretamente na interface (vai ajudar a garantir que o usuário faça download da imagem correta).
- Download de **PFP** do Instagram a partir do nome de usuário.
- Download de **Thumbnails** de posts do Instagram ou TikTok a partir da URL.

## 📁 Estrutura do Projeto
```
├── app.py # Configurações da navegação e páginas do Streamlit
├── profile_picture.py # Página: download de PFP
├── thumbnail_reels.py # Página: download de thumbnail de Reels (Instagram)
├── thumbnail_tiktok.py # Página: download de thumbnail do TikTok
├── utils.py # Funções utilitárias
├── .streamlit/
│ └── pages.toml # Definição das páginas e ícones (st_pages)
├── .gitignore # Arquivos a serem ignorados pelo Git
└── pycache/ # Cache do Python (gerado automaticamente)
```

## ⚙️ Como Executar Localmente
1.  **Clone o Repositório:**
    ```bash
    git clone [Link do seu repositório]
    cd [Nome do seu repositório]
    ```
2.  **Crie e Ative um Ambiente Virtual:**
    É uma boa prática usar ambientes virtuais para isolar as dependências do projeto.
    ```bash
    # Cria o ambiente virtual
    python -m venv .venv
    
    # Ativa o ambiente virtual (no Windows)
    .venv\Scripts\activate
    
    # Ativa o ambiente virtual (no macOS/Linux)
    source .venv/bin/activate
    ```
3.  **Instale as Dependências:**
    O arquivo `requirements.txt` lista todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Aplicativo Streamlit:**
    ```bash
    streamlit run app.py
    ```
O app abrirá automaticamente no navegador.

## 🛠️ Tecnologias
- **Python:** A linguagem de programação principal.
- **Streamlit:** Framework para a construção do aplicativo web.
- **Requests:** Para realizar scraping e tratar downloads de imagens.
- **Instaloader:** Para acessar dados públicos do Instagram.

## 👩‍💻 Autor
Este projeto foi desenvolvido por:

- **Nome:** Isadora Torqueti
- **GitHub:** https://github.com/isatorqueti
- **Linkedin:** https://www.linkedin.com/in/isadoratorqueti/

## 📜 Licença

Este projeto está licenciado sob a licença [MIT](~link~). Sinta-se à vontade para usar, modificar e distribuir o código.
---