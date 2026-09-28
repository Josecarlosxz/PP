let flashcards = [];
let indiceAtual = 0;

const pergunta = document.getElementById("pergunta");
const resposta = document.getElementById("resposta");
const tema = document.getElementById("tema");
const progresso = document.getElementById("progresso");

const btnRevelar = document.getElementById("btn-revelar");
const btnProximo = document.getElementById("btn-proximo");
const mensagem = document.getElementById("mensagem");


/* ============================================================
   CARREGAR FLASHCARDS
============================================================ */

async function carregarFlashcards() {

    // Verifica se o usuário está logado
    if (!window.BioSistema.Sessao.exigirLogin()) {
        return;
    }

    try {

        // Usa a API do projeto, que envia o token automaticamente
        flashcards = await window.BioSistema.API.get("/flashcards/");

        if (!flashcards || flashcards.length === 0) {

            pergunta.textContent =
                "Nenhum flashcard encontrado.";

            tema.textContent = "";

            progresso.textContent = "0 / 0";

            btnRevelar.style.display = "none";
            btnProximo.style.display = "none";

            return;
        }

        mostrarFlashcard();

    } catch (erro) {

        console.error("Erro ao carregar flashcards:", erro);

        pergunta.textContent =
            erro.message || "Não foi possível carregar os flashcards.";

        tema.textContent = "";
    }
}


/* ============================================================
   MOSTRAR FLASHCARD
============================================================ */

function mostrarFlashcard() {

    const flashcard = flashcards[indiceAtual];

    pergunta.textContent = flashcard.pergunta;
    resposta.textContent = flashcard.resposta;
    tema.textContent = flashcard.tema;

    progresso.textContent =
        `${indiceAtual + 1} / ${flashcards.length}`;

    // Esconde a resposta
    resposta.classList.add("escondida");

    btnRevelar.textContent =
        "👁️ Revelar resposta";

    mensagem.textContent = "";
}


/* ============================================================
   REVELAR RESPOSTA
============================================================ */

btnRevelar.addEventListener("click", () => {

    if (resposta.classList.contains("escondida")) {

        resposta.classList.remove("escondida");

        btnRevelar.textContent =
            "🙈 Esconder resposta";

    } else {

        resposta.classList.add("escondida");

        btnRevelar.textContent =
            "👁️ Revelar resposta";
    }

});


/* ============================================================
   PRÓXIMO FLASHCARD
============================================================ */

btnProximo.addEventListener("click", () => {

    indiceAtual++;

    if (indiceAtual >= flashcards.length) {

        indiceAtual = 0;

        mensagem.textContent =
            "🎉 Você terminou todos os flashcards!";
    }

    mostrarFlashcard();

});


/* ============================================================
   INICIAR
============================================================ */

carregarFlashcards();