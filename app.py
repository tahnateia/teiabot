import streamlit as st
from streamlit.components.v1 import html
import base64
import os

# Configuração da página com título
st.set_page_config(page_title="tah na teia!")

# Função para ler a imagem de fundo e convertê-la em base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Defina o caminho relativo da imagem de fundo
background_image_path = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')
background_image_base64 = get_base64_image(background_image_path)

# CSS para o fundo e o título centralizado
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{background_image_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .title {{
            position: absolute;
            top: 10%;
            left: 50%;
            transform: translate(-50%, 190%);
            font-size: 4em;
            color: white;
            text-shadow: 2px 2px 8px #4d0d9a;
            font-weight: bold;
            text-align: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Insere o título centralizado
st.markdown('<div class="title">tah na teia!</div>', unsafe_allow_html=True)

# Função JavaScript para maximizar o Blip Chat e monitorar o botão de reset
maximized_chat_script = """<script src="https://unpkg.com/blip-chat-widget" type="text/javascript"></script>
<script>
    (function () {
        window.onload = function () {
            new BlipChat()
                .withAppKey('dGFobmF0ZWlhOjVkZDE2ZWY4LTMyY2QtNGM5Yi1hODU5LWQwNzQxMGJlZmQxZg==')
                .withButton({"color":"#5233c1","icon":"https://blipmediastore.blip.ai/public-medias/Media_32a3c387-0745-4a33-ad33-2cf194e1aec0"})
                .withCustomCommonUrl('https://mayconcipriano-4de7c.chat.blip.ai/')
                .build();
        }
    })();
</script>
            
            
            
"""

# Renderiza o HTML e JavaScript
html(maximized_chat_script, height=600, width=1000, scrolling=True)
