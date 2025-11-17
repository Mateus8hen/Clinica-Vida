import streamlit as st

st.header("Cadastro de Pacientes")
st.logo("./img/LOGOCLINICA.png")

if "role" not in st.session_state or st.session_state.role is "Visitante":
    st.warning("⚠️ Faça login primeiro para acessar esta página.")
    st.stop()

if st.session_state.role != "Secretaria":
    st.warning("⚠️ Acesso negado.")
    st.stop()


nome = st.text_input("Nome do Paciente")
idade = st.number_input("Idade", step=1)
telefone = st.text_input("Telefone", max_chars=11)

if st.button("Cadastrar Paciente"):
    if not nome:
        st.error("Nome não pode ser vazio.")
    elif idade <= 0 or idade > 110:
        st.error("Idade inválida.")
    elif not telefone:
        st.error("Telefone não pode ser vazio.")
    elif not telefone.isdigit() or len(telefone) < 8:
        st.error("Telefone inválido.")
    else:
        with open("pacientes.txt", "a", encoding="utf8") as file:
            file.write(f"{nome}, {idade}, {telefone}\n")
        st.success(f"Paciente {nome} cadastrado com sucesso!")
def logout():

    if st.button("Logout"):
        st.session_state.role = "Visitante"
        st.success("Logout realizado.")
        st.rerun()

logout()
