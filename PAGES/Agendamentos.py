import streamlit as st

st.header("Agendamentos de Consultas")
st.logo("./img/LOGOCLINICA.png")

if "role" not in st.session_state or st.session_state.role is "Visitante":
    st.warning("⚠️ Faça login primeiro para acessar esta página.")
    st.stop()

if st.session_state.role != "Secretaria":
    st.warning("⚠️ Acesso negado.")
    st.stop()


def verificarConsulta(A, B, C, D):

    AND1 = A and B and C
    ADD2 = B and C and D
    return (AND1 or ADD2)


def emergencia(E, F, G):
    OR = E and (F or G)
    return (OR)


st.subheader("Selecione os detalhes da consulta:")
A = st.checkbox("Paciente tem agendamento prévio")
B = st.checkbox("Paciente esta com documentação em dia")
C = st.checkbox("Há disponibilidade de médicos")
D = st.checkbox("Pagementos estão em dia")

if st.button("Verificar Agendamento"):
    Pode_consultar = verificarConsulta(A, B, C, D)
    if Pode_consultar:
        st.success("Liberado para a consulta.")
    else:
        st.warning("Nao está liberado para a consulta.")

st.divider()

st.subheader("Condições da Consulta de Emergência:")
E = st.checkbox("Medico disponível no momento")
F = st.checkbox("Paciente possui documentação")
G = st.checkbox("Pagemento em dia")


if st.button("Checar Emergência"):
    Emergencia_consulta = emergencia(E, F, G)
    if Emergencia_consulta:
        st.success("Consulta de emergência autorizada.")
    else:
        st.warning("Consulta de emergência não autorizada.")

st.divider()

def logout():

    if st.button("Logout"):
        st.session_state.role = "Visitante"
        st.success("Logout realizado.")
        st.rerun()

logout()

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
