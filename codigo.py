from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave API da variável de ambiente
chave_api = os.getenv("OPENAI_API_KEY")

# Imprimir a chave API para verificação
print(f"Chave API: {"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}")

# Verificar se a chave API foi carregada corretamente
if chave_api is None:
    raise ValueError("A chave API não foi encontrada. Verifique o arquivo .env.")

# Configurar o modelo com a chave API
modelo = ChatOpenAI(model="gpt-3.5-turbo", api_key=chave_api)

# Definir mensagens e parser
mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("Se inscrevam no canal para aprender Python")
]

parser = StrOutputParser()
chain = modelo | parser

# Definir template de mensagem
template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}"),
])

# Criar as mensagens usando o template
input_mensagem = template_mensagem.format_messages(idioma="francês", texto="Dê like no vídeo e comente o que você tá achando")

# Exemplo de invocação final usando a lista de mensagens formatadas
texto = chain.invoke(input_mensagem)
print(texto)
