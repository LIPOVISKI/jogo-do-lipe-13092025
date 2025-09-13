import random
import streamlit as st

# Configurações básicas
st.set_page_config(page_title="Jogo de Adivinhação de um corno sem ter o que fazer 🎯", layout="centered")

# Um fundinho simples pra não ficar tudo branco
st.markdown("""
<style>
body {
    background: radial-gradient(circle, #fafafa, #eaeaea);
}
.confetti {
    font-size: 36px;
    text-align: center;
    animation: balanco 1s infinite;
}
@keyframes balanco {
    0% {transform: translateY(-5px);}
    50% {transform: translateY(5px);}
    100% {transform: translateY(-5px);}
}
</style>
""", unsafe_allow_html=True)

st.title("🔢 Jogo de Adivinhação de um corno sem ter o que fazer")
st.write("Duvido vc acertar o numero que eu pensei ta de 1 a 70 😏")

# Inicializa variáveis só na primeira vez
if "numero" not in st.session_state:
    st.session_state.numero = random.randint(1, 100)
    st.session_state.tentativas = 0
    st.session_state.msg = ""
    st.session_state.venceu = False

palpite = st.number_input("Seu chute:", 1, 100, step=1)

if st.button("tem certeza que é esse numero?"):
    if not st.session_state.venceu:
        st.session_state.tentativas += 1
        if palpite < st.session_state.numero:
            st.session_state.msg = "🔼 Erro otario é mais alto!"
        elif palpite > st.session_state.numero:
            st.session_state.msg = "🔽 Erro babaca é mais baixo!"
        else:
            st.session_state.msg = f"🎉 aleluia que acerto FDP! Era {st.session_state.numero}! Você precisou de {st.session_state.tentativas} tentativas. 😎"
            st.session_state.venceu = True

st.write(st.session_state.msg)
st.write(f"Tentativas: {st.session_state.tentativas}")

if st.session_state.venceu:
    st.markdown("<div class='confetti'>🎊🎉🥳🎉🎊</div>", unsafe_allow_html=True)
    st.balloons()

if st.button("TE DESAFIO TENTAR MAIS UMA VEZ COCO"):
    st.session_state.numero = random.randint(1, 100)
    st.session_state.tentativas = 0
    st.session_state.msg = "Novo jogo começando... Boa sorte de cu é rola! 🍀"
    st.session_state.venceu = False
