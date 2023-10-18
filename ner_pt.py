import streamlit as st
import spacy

!python -m spacy download pt_core_news_md

# Carrega o modelo spaCy para português
nlp = spacy.load("pt_core_news_sm")

# Título da aplicação
st.title("Extrator de Entidades Nomeadas em Português")

# Caixa de texto para inserir o texto
input_text = st.text_area("Insira o texto em português:")

# Função para extrair as entidades
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Botão para executar a extração de entidades
if st.button("Extrair Entidades"):
    if input_text:
        entities = extract_entities(input_text)
        if entities:
            st.subheader("Entidades Nomeadas Encontradas:")
            for entity, label in entities:
                st.write(f"Entidade: {entity}, Tipo: {label}")
        else:
            st.write("Nenhuma entidade encontrada no texto inserido.")
    else:
        st.write("Por favor, insira um texto para realizar a extração de entidades.")

# Nota informativa sobre o modelo utilizado
st.write("Este aplicativo utiliza o modelo 'pt_core_news_sm' do spaCy para NER em português.")
