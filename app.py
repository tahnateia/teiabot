import streamlit as st
from streamlit.components.v1 import html
import base64

# Configuração da página com título
st.set_page_config(page_title="tah na teia!")

# Função para ler a imagem de fundo e convertê-la em base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Defina a imagem de fundo usando base64 para garantir que o Streamlit carregue corretamente
background_image_path = "tah_na_teia/assets/image.jpg"
background_image_base64 = get_base64_image(background_image_path)

st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/avif;base64,{background_image_base64}");
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
<script src="https://unpkg.com/blip-chat-widget" type="text/javascript"></script>
<script>
    (function () {
        window.onload = function () {
            const blipClient = new BlipChat()
                .withAppKey('dGFobmF0ZWlhOjVkZDE2ZWY4LTMyY2QtNGM5Yi1hODU5LWQwNzQxMGJlZmQxZg==')
                .withButton({
                    "color":"#4d0d9a",
                    "icon":"https://blipmediastore.blip.ai/public-medias/Media_32a3c387-0745-4a33-ad33-2cf194e1aec0",
                    "size": "100"  // Tamanho do ícone ajustado para maior visibilidade
                })
                .withCustomCommonUrl('https://mayconcipriano-4de7c.chat.blip.ai/')
                .withCustomStyle(`
                    .blip-chat-container {
                        width: 100vw;
                        height: 90vh;
                        max-width: 100%;
                        max-height: 100%;
                    }
                `)
                .withEventHandler(BlipChat.LOAD_EVENT, function () {
                    blipClient.widget.open();  // Abre a janela maximizada ao clicar
                })
                .withEventHandler(BlipChat.OPEN_EVENT, function () {
                    // Adiciona botão para resetar a conversa
                    const resetButton = document.createElement('button');
                    resetButton.innerHTML = 'Resetar Conversa';
                    resetButton.style.position = 'absolute';
                    resetButton.style.top = '100px';
                    resetButton.style.right = '10px';
                    resetButton.style.zIndex = '1000';
                    resetButton.style.backgroundColor = '#4d0d9a';
                    resetButton.style.color = 'white';
                    resetButton.style.border = 'none';
                    resetButton.style.padding = '10px';
                    resetButton.style.borderRadius = '5px';
                    resetButton.style.cursor = 'pointer';
                    resetButton.onclick = function () {
                        blipClient.widget._resetChat();
                    };
                    document.querySelector('.blip-chat-container').appendChild(resetButton);
                })
                .build();
        };
    })();
</script>
""", height=600, width=1000, scrolling=True)  # Ajuste a altura se necessário
