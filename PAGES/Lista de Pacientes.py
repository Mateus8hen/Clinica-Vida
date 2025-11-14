import streamlit as st
import pandas as pd


st.header("Lista de Pacientes")
st.logo("./img/LOGOCLINICA.png")

if "role" not in st.session_state or st.session_state.role is "Visitante":
    st.warning("⚠️ Faça login primeiro para acessar esta página.")
    st.stop()

if st.session_state.role != "Secretaria":
    st.warning("⚠️ Acesso negado.")
    st.stop()

df_pacientes = pd.DataFrame()

buscar_pacientes = st.text_input("Buscar Pacientes",)
placeholder = "Digite o nome do paciente"

if buscar_pacientes:
    try:
        df_pacientes = pd.read_csv("pacientes.txt", names=[
                                   "Nome", "Idade", "Telefone"], encoding="utf8")
        df_filtrado = df_pacientes[df_pacientes["Nome"].str.contains(
            buscar_pacientes, case=False, na=False)]
        st.dataframe(df_filtrado)
    except FileNotFoundError:
        st.info("Nenhum paciente cadastrado ainda.")


def carregar_pacientes():
    pacientes = []
    try:
        with open("pacientes.txt", "r", encoding="utf8") as file:
            for line in file:
                nome, idade, telefone = line.strip().split(", ")
                pacientes.append(
                    {"Nome": nome, "Idade": idade, "Telefone": telefone})
    except FileNotFoundError:
        st.info("Nenhum paciente cadastrado ainda.")
    return pacientes


st.dataframe(carregar_pacientes())


def contar_pacientes():
    pacientes = carregar_pacientes()
    return len(pacientes)


st.write("Pacientes cadastrados: ", contar_pacientes())


def calcular_idade_media():
    pacientes = carregar_pacientes()
    if not pacientes:
        return 0
    idades = [int(p["Idade"]) for p in pacientes]
    return sum(idades) / len(idades)


st.write("Idade média dos pacientes: ",
         f"{calcular_idade_media():.0f} anos")


pacientes = carregar_pacientes()
idade_corte = 30

pacientes_mais_velhos = [
    p for p in pacientes if int(p["Idade"]) >= idade_corte]
pacientes_mais_jovens = [p for p in pacientes if int(p["Idade"]) < idade_corte]

st.write(
    f"Pacientes com {idade_corte} anos ou mais: {len(pacientes_mais_velhos)}")
st.write(
    f"Pacientes com menos de {idade_corte} anos: {len(pacientes_mais_jovens)}")


def logout():
    if st.button("Logout"):
        st.session_state.role = "Visitante"
        st.success("Logout realizado.")
        st.rerun()
