import streamlit as st

if "pedidos" not in st.session_state:
    st.session_state.pedidos = []

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
    st.write("---")
# --- DADOS DO CLIENTE ---
nome_cliente = st.text_input("Seu Nome:")

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
    if fruta == "Morango":
        st.image("bombom_ninho.jpg", caption="Bombom de Morango", width=250)
    elif fruta == "Uva":
        st.image("bombom_uva1", caption="Bombom de Uva", width=250)
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
        ["Limao", "Maracuja"]
    )
    # MOSTRAR IMAGEM DA TORTINHA (deve ficar recuado com espaços!)
    if sabor_tortinha == "Limao":
        st.image("tortinha_limao.jpg", caption="Tortinha de Limao", width=250)
    elif sabor_tortinha == "Maracuja":
        st.image("tortinha_maracuja.jpg", caption="Tortinha de Maracuja", width=250)

# Primeiro cria os campos para o usuário preencher
quantidade = st.number_input("Quantidade:", min_value=1, value=1)
observacoes = st.text_area("Observações do Pedido:", placeholder="Ex: Diminuir a quantidade de frutas,  etc.", height=70)

# DEPOIS coloca o botão de enviar
import urllib.parse

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
        numero = st.text_input("Número :")
        
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

if pagamento == "Pix":
    st.info("💡 **Chave PIX (CNPJ):** `67833016000156`\n\n*Copie e cole a chave no seu aplicativo do banco. (Enviar o comprovante de pagamento)*")

elif pagamento == "Dinheiro":
    precisa_troco = st.radio("Precisa de troco?", ["Não", "Sim"])
    if precisa_troco == "Sim":
        valor_troco = st.number_input("Troco para quanto? (R$)", min_value=0.0, step=5.0)
        troco_texto = f" (Troco para R$ {valor_troco:.2f})"

st.success(f"Forma de pagamento selecionada: **{pagamento}**{troco_texto}")

# --- CÁLCULO DO VALOR TOTAL ---
# Define o valor unitário de acordo com a opção escolhida
if "250ml" in comida:
    preco_unitario = 15.00
elif "350ml" in comida:
    preco_unitario = 18.00
elif "Tortinha" in comida:
    preco_unitario = 12.00
else:
    preco_unitario = 0.00

# Considera a taxa de entrega (se 'taxa_entrega' estiver definida)
taxa = taxa_entrega if 'taxa_entrega' in locals() and tipo_entrega == "Entrega (Motoboy)" else 0.00
valor_total = (preco_unitario * quantidade) + taxa

# Exibe o valor total na tela
st.markdown(f"### 💰 **Total do Pedido: R$ {valor_total:.2f}**")

# Botão para enviar/salvar o pedido
if st.button("Finalizar Pedido"):
    if not nome_cliente or comida == "Selecione...":
        st.warning("Por favor, preencha seu nome e escolha um item.")
    else:
        novo_pedido = {
            "Cliente": nome_cliente,
            "Item": comida,
            "Quantidade": quantidade,
            "Total": f"R$ {valor_total:.2f}",
            "Entrega": tipo_entrega,
            "Pagamento": f"{pagamento} {troco_texto}"
        }
        st.session_state.pedidos.append(novo_pedido)
        st.success("Pedido enviado com sucesso!")

# ==========================================
# PÁGINA 2: ÁREA RESTRITA (ADMIN)
# ==========================================
st.write("---")
st.title("🔒 Painel do Administrador")

senha_digitada = st.text_input("Digite a senha de acesso:", type="password", key="senha_admin")

if senha_digitada == "adminmimosa":
    st.success("Acesso autorizado!")
    st.write("---")

    st.subheader("📋 Lista de Pedidos Recebidos")

    if len(st.session_state.pedidos) == 0:
        st.info("Nenhum pedido foi registrado nesta sessão ainda.")
    else:
        for idx, p in enumerate(st.session_state.pedidos, 1):
            with st.expander(f"Pedido #{idx} - {p['Cliente']}"):
                st.write(f"**Item:** {p['Item']} (x{p['Quantidade']})")
                st.write(f"**Total:** {p['Total']}")
                st.write(f"**Entrega:** {p['Entrega']}")
                st.write(f"**Pagamento:** {p['Pagamento']}")

        if st.button("Limpar Histórico de Pedidos"):
            st.session_state.pedidos = []
            st.rerun()
elif senha_digitada != "":
    st.error("Senha incorreta!")
