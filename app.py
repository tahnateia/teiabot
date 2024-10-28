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

# Insira o título centralizado
st.markdown('<div class="title">tah na teia!</div>', unsafe_allow_html=True)

# Insira o script do Blip Chat com função de reset e janela maximizada
html("""
<script>
window.embeddedChatbotConfig = {
chatbotId: "Q5GlC0cLhsUWSsi2n3_F1",
domain: "www.chatbase.co"
}
</script>
<script
src="https://www.chatbase.co/embed.min.js"
chatbotId="Q5GlC0cLhsUWSsi2n3_F1"
domain="www.chatbase.co"
defer>
</script>
""", height=600, width=1000, scrolling=True)
