from flask import Flask, request, redirect, url_for
from backend.controller.animal_controller import cadastrar_animal, atualizar_animal,deletar_animal

app = Flask(__name__)

@app.route("/animais", methods=["POST"])
def rota_cadastrar_animal():
    dados_formulario = request.form.to_dict() 
    
    resultado = cadastrar_animal(dados_formulario)
    
    return f"Sucesso: {resultado['mensagem']}"


@app.route("/animais/<int:animal_id>", methods=["POST"])  
def rota_atualizar_animal(animal_id):
    dados_formulario = request.form.to_dict()
    
    resultado = atualizar_animal(animal_id, dados_formulario)
    return f"Sucesso: {resultado['mensagem']}"


@app.route("/animais/<int:animal_id>/deletar", methods=["POST"])
def rota_deletar_animal(animal_id):
    resultado = deletar_animal(animal_id)
    
    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"
        
    return f"Sucesso: {resultado['mensagem']}"

if __name__ == "__main__":
    app.run(debug=True)