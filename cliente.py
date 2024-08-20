from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8000/tradutor")
texto = chain_remota.invoke({"idioma": "espanhol", "texto": "Já deu like no vídeo? Se não, dá agora"})
print(texto)