import streamlit as st

st.set_page_config(page_title="Meu Cartão Interativo", page_icon="🛍️", layout="centered")

# --- LOGO E TÍTULO LADO A LADO ---
col_logo, col_titulo = st.columns([1, 3])

with col_logo:
    st.image("logo.jpg1", width=100)

with col_titulo:
    st.html("<h1 style='font-size: 1.8rem; font-weight: 700; margin-top: 10px;'>BEM-VINDOS AO SITE DA<br>MIMOSA CONFEITARIA!</h1>")

st.write("Faça seu pedido diretamente pelo nosso formulário abaixo ou entre em contato pelas redes sociais.")
st.set_page_config  (page_title="Meu Cartão Interativo",     page_icon="🛍️", layout="centered")

# Título e Logo
col1, col2, col3 = st.columns([1, 1, 1])

# --- CONTATOS EM TEXTO COM ÍCONE LADO A LADO ---
with col1:
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px;">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="30">
            <span style="font-size: 18px; font-weight: bold;">@mimosaconfeitariaa</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px;">
            <img src="https://cdn-icons-png.flaticon.com/512/3670/3670051.png" width="30">
            <span style="font-size: 18px; font-weight: bold;">(47) 99678-6099</span>
        </div>
        """, 
        unsafe_allow_html=True
    )


# Lista de opções principal
comida = st.selectbox(
    "Escolha o item:",
    ["Selecione...", "BomBom no Pote 250ml - R$ 15,00", "BomBom no Pote 350ml - R$ 18,00", "Tortinha Gourmet - R$ 12,00"]
)

# Condicional: Se a pessoa escolher QUALQUER um dos Bombons no Pote
if "BomBom no Pote" in comida:
    st.write("---")
    st.markdown("### 🍫 Escolha sua fruta")
    
    # Escolha da Fruta
    fruta = st.radio(
        "Escolha a Fruta:",
        ["Morango", "Uva", ]
    )
    
    # Escolha do Creme
    creme = st.selectbox(
        "Escolha o Sabor do Creme:",
        ["Ninho", "Cacau" ]
    )

    # Nova opção: Escolha do Brigadeiro
    brigadeiro = st.selectbox(
        "Escolha o Sabor do Brigadeiro:",
        ["Ninho", "Cacau",  "Maracujá"]
    )
    
    st.success(f"Você escolheu: **{comida}** com **{fruta}**, creme de **{creme}** e brigadeiro **{brigadeiro}**!")

elif comida == "Tortinha Gourmet - R$ 12,00":
    st.write("---")
    sabor_tortinha = st.selectbox(
        "Escolha o Sabor da Tortinha:",
        ["Limão", "Maracujá", ]
)

quantidade = st.number_input("Quantidade:", min_value=1, value=1)
nome_cliente = st.text_input("Seu Nome:")
observacoes = st.text_area("Observações do Pedido:")

if st.button("Enviar Pedido"):
    if nome_cliente:
        st.success(f"Obrigado, {nome_cliente}! Seu pedido de {quantidade}x {comida} foi registrado.")
    else:
        st.warning("Por favor, digite seu nome antes de enviar.")
        st.write("---")

# Opção de entrega ou retirada
tipo_entrega = st.radio(
    "Como deseja receber seu pedido?",
    ["Retirada no Local (Grátis)", "Entrega (Motoboy)"]
)

taxa_entrega = 0.0

if tipo_entrega == "Entrega (Motoboy)":
    st.markdown("#### 📍 Endereço de Entrega")
    
    # Organizando CEP e Bairro em duas colunas pra ficar bem bonito
    col_cep, col_bairro = st.columns(2)
    with col_cep:
        cep = st.text_input("CEP:", placeholder="00000-000")
    with col_bairro:
        bairro = st.text_input("Bairro:")
        
    # Rua e Número na mesma linha
    col_rua, col_num = st.columns([3, 1])
    with col_rua:
        rua = st.text_input("Rua / Avenida:")
    with col_num:
        numero = st.text_input("Número:")
        
    # Ponto de referência e complemento
    complemento = st.text_input("Complemento (Apt, Bloco, etc.):", placeholder="Ex: Apto 102")
    referencia = st.text_area("Ponto de Referência:", placeholder="Ex: Próximo à padaria X", height=70)

  # Cálculo da taxa para Cidade Nova e São Vicente
    if bairro.strip():
        bairro_limpo = bairro.strip().lower()
        if bairro_limpo in ["cidade nova", "são vicente", "sao vicente"]:
            taxa_entrega = 5.00
        else:
            taxa_entrega = 8.00  # Valor padrão para demais bairros
            
        st.info(f"Taxa de entrega para **{bairro.title()}**: **R$ {taxa_entrega:.2f}**")
        # --- FORMAS DE PAGAMENTO ---
st.write("---")
st.markdown("### 💳 Forma de Pagamento")

pagamento = st.radio(
    "Escolha a forma de pagamento:",
    ["Pix", "Dinheiro", "Cartão de Débito", "Cartão de Crédito"]
)

troco_texto = ""
if pagamento == "Dinheiro":
    precisa_troco = st.radio("Precisa de troco?", ["Não", "Sim"])
    if precisa_troco == "Sim":
        valor_troco = st.number_input("Troco para quanto? (R$)", min_value=0.0, step=5.0)
        troco_texto = f" (Troco para R$ {valor_troco:.2f})"

st.success(f"Forma de pagamento selecionada: **{pagamento}**{troco_texto}")
