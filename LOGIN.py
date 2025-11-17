import streamlit as st


st.title("Clinica Vida+")
st.logo("./img/LOGOCLINICA.png")

if "role" not in st.session_state:
    st.session_state.role = "Visitante"

st.write(f"{st.session_state.role}")

Usuarios = [
    "Visitante",
    "Medico1",
    "Medico2",
    "Secretaria",
]


def menu():
    cadastro = st.sidebar.button("Cadastro de Pacientes")
    Estatisticas = st.sidebar.button("Estatísticas")
    buscar = st.sidebar.button("Buscar Pacientes")
    lista = st.sidebar.button("Lista de Pacientes")
    return cadastro, Estatisticas, buscar, lista


def login():
    st.subheader("Login")
    usuario = st.selectbox("Selecione o usuário", Usuarios, index=0)
    if st.button("Entrar"):
        if usuario:
            st.session_state.role = usuario
            st.success(f"Logado como {usuario}")
            st.rerun()
        else:
            st.error("Por favor, selecione um usuário.")


def logout():
    if st.button("Logout"):
        st.session_state.role = "Visitante"
        st.success("Logout realizado.")
        st.rerun()


st.markdown("""
<style>
.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 20px;
    border: none;
    padding: 10px 24px;
}
    [data-testid="stAppViewContainer"] {
    background-color: A9A9A9;
    color: black;
}      
[data-testid="stHeader"] {
    background-color: #228B22 ;
    display:  none;
}
</style>
""", unsafe_allow_html=True)
