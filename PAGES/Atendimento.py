import streamlit as st

st.title("Atendimento")
st.subheader("Fila de atendimento")
st.logo("./img/LOGOCLINICA.png")

if "role" not in st.session_state or st.session_state.role is "Visitante":
    st.warning("⚠️ Faça login primeiro para acessar esta página.")
    st.stop()

if st.session_state.role != "Secretaria" and st.session_state.role != "Medico1" and st.session_state.role != "Medico2":
    st.warning("⚠️ Acesso negado.")
    st.stop()

if 'fila_atendimento' not in st.session_state:
    st.session_state.fila_atendimento = []

st.divider()

st.header("Adicionar pacientes na fila:")

with st.form(key="form_add_paciente", clear_on_submit=True):
    nomePaciente = st.text_input("Digite o nome do paciente:")
    cpfPaciente = st.text_input("Digite o CPF do paciente:", max_chars=11)

    submitted = st.form_submit_button("Adicionar")

    if submitted:
        if nomePaciente and cpfPaciente:
            st.session_state.fila_atendimento.append({
                "nome": nomePaciente,
                "cpf": cpfPaciente
            })
            st.success(f"Paciente {nomePaciente} adicionado a fila.")
        else:
            st.error("Por favor, preencha todos os campos.")

st.divider()

st.header("Chamar paciente da fila:")

if st.button("Chamar paciente"):
    if st.session_state.fila_atendimento:
        paciente_chamado = st.session_state.fila_atendimento.pop(0)
        st.success(
            f"Paciente {paciente_chamado['nome']} CPF: {paciente_chamado['cpf']} chamado.")
    else:
        st.warning("Nenhum paciente na fila.")

st.divider()

st.header("Fila")

if st.session_state.fila_atendimento:
    st.write("Proximo Paciente: ")
    for i, paciente in enumerate(st.session_state.fila_atendimento):
        st.write(
            f"{str(i+1)} - {paciente['nome']}, CPF: {paciente['cpf']}")
else:
    st.info("Nenhum paciente na fila.")
st.divider()

st.header("Remover paciente da fila:")

if st.session_state.fila_atendimento:
    pacienteRemover = st.selectbox(
        "Remover paciente",
        options=st.session_state.fila_atendimento,
        format_func=lambda paciente: f"{paciente['nome']}, CPF: {paciente['cpf']}",
        index=None,
    )

    if pacienteRemover:
        st.session_state.fila_atendimento.remove(pacienteRemover)
        st.success(f"Paciente {pacienteRemover['nome']} removido da fila.")
        st.rerun()
    else:
        st.warning("Por favor, selecione um paciente para remover.")
else:
    st.info("")
