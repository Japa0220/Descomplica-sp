import requests
import PyPDF2
import docx
import csv

def carregar_documento(caminho):
    if caminho.endswith('.pdf'):
        with open(caminho, 'rb') as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            texto = ""
            for pagina in leitor.pages:
                texto += pagina.extract_text()
        return texto
    
    elif caminho.endswith('.docx'):
        doc = docx.Document(caminho)
        return "\n".join([paragrafo.text for paragrafo in doc.paragraphs])
    
    elif caminho.endswith('.csv'):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            return "\n".join([" ".join(linha) for linha in leitor])
    
    elif caminho.endswith('.txt'):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    
    return "Formato de arquivo não suportado"

documentos = [
    carregar_documento('Alvará de Execução de Demolição'),  
    carregar_documento('Alvará para Residência Unifamiliar'),  
    carregar_documento('Alvarás de Aprovação e Execução de Reforma'),
    carregar_documento('Alvarás de Autorização para Tapume'),
    carregar_documento('Alvarás e documentos referente à Segurança da Edificação e Controle do Uso de Imóveis'),
    carregar_documento('Alvarás e solicitações para Parcelamento do Solo'),
    carregar_documento('Alvarás para Habitação de Interesse Social'),
    carregar_documento('Aprova Rápido 1'),
    carregar_documento('Regularização da Edificação 1'),
    carregar_documento('Certificado de conclusão 1'),
    carregar_documento('Ficha Técnica 1'),
    ]

def buscar_conhecimento(entrada, documentos):
    conhecimento_relevante = []
    for doc in documentos:
        if entrada.lower() in doc.lower():
            conhecimento_relevante.append(doc)
    
    return " ".join(conhecimento_relevante) if conhecimento_relevante else None


AZURE_ENDPOINT = "https://aipn10062.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions"
API_KEY = "8423ec5386db431981f5e8f793929d81"
API_VERSION = "2024-08-01-preview"

CONTEXTO_INICIAL = f"""
Você é um chatbot de atendimento especializado no projeto Portal de Licenciamento.
Suas características:
- Fale de forma amigável e informal
- Responda de forma completa e detalhada
- Forneça explicações claras e abrangentes
- Uso de qualquer Lingua
-Perguntas e respostas focadas apenas no Portal de Licenciamento

Documentos de referência carregados:
{documentos[:2]}  # Limita para não estourar o contexto
"""

print("Chatbot: Olá! Sou o Bruno. ChatBot pessoal do Portal de Licenciamento. Como posso te ajudar?")
print("Digite 'sair' para encerrar.")

historico_mensagens = [
    {"role": "system", "content": CONTEXTO_INICIAL}
]

while True:
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        print("Chatbot: Até mais!")
        break
    try:
        conhecimento = buscar_conhecimento(entrada, documentos)
        
        if conhecimento:
            entrada += f"\n\nInformação adicional relevante dos documentos: {conhecimento}"
        
        historico_mensagens.append({"role": "user", "content": entrada})
        
        headers = {
            "Content-Type": "application/json",
            "api-key": API_KEY
        }
        
        payload = {
            "messages": historico_mensagens,
            "max_tokens": 500,
            "temperature": 0.5,
            "top_p": 0.95,
            "presence_penalty": 0.5,
            "frequency_penalty": 0.5
        }
        
        response = requests.post(
            f"{AZURE_ENDPOINT}?api-version={API_VERSION}", 
            headers=headers, 
            json=payload
        )
        
        if response.status_code == 200:
            resposta = response.json()['choices'][0]['message']['content']
            print(f"Chatbot: {resposta}")
            
            historico_mensagens.append({"role": "assistant", "content": resposta})
            
            if len(historico_mensagens) > 10:
                historico_mensagens = historico_mensagens[-10:]
        
        else:
            print(f"Erro na requisição: {response.status_code}")
            print(f"Detalhes: {response.text}")
        
    except Exception as e:
        print("Chatbot: Ocorreu um erro. Tente novamente mais tarde.")
        print(f"Erro: {e}")
        
        