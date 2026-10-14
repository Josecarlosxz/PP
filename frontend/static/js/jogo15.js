/* ============================================================
   JOGO DOS 15 (FOTO) — IFauna
   A foto é cortada em 4x4 com CSS (background-position).
   Fica dentro de uma função para não conflitar com o flashcards.js.
============================================================ */
(function () {
  "use strict";

  const SIZE = 4;
  const TOTAL = SIZE * SIZE;
  const CHAVE_RECORDE = "ifauna_j15_recorde";

  // Pasta das fotos (frontend/static/img/animais/) e lista de fotos.
  // Para adicionar uma foto: coloque o arquivo na pasta e crie uma linha aqui.
  const PASTA = "/static/img/animais/";
  const FOTOS = [
    ["onca.jpg",  "Onça-pintada"],
    ["arara.jpg", "Arara-azul"],
    ["boto.jpg",  "Boto-cor-de-rosa"]
  ];

  const board = document.getElementById("j15-board");
  const movesEl = document.getElementById("j15-moves");
  const timeEl = document.getElementById("j15-time");
  const bestEl = document.getElementById("j15-best");
  const msgEl = document.getElementById("j15-msg");
  const refImg = document.getElementById("j15-ref-img");
  const refNome = document.getElementById("j15-ref-nome");
  const chkNumeros = document.getElementById("j15-numeros");

  document.getElementById("j15-reset").addEventListener("click", () => novoJogo(false));
  document.getElementById("j15-trocar").addEventListener("click", () => novoJogo(true));
  chkNumeros.addEventListener("change", () =>
    board.classList.toggle("j15-numeros", chkNumeros.checked));

  let tiles, moves, seconds, timer;
  let fotoAtual = Math.floor(Math.random() * FOTOS.length);

  const resolvido = () =>
    [...Array(TOTAL - 1).keys()].map(i => i + 1).concat(0);
  const estaResolvido = () => tiles.every((v, i) => v === (i + 1) % TOTAL);

  const urlFoto = () => PASTA + FOTOS[fotoAtual][0];
  const nomeFoto = () => FOTOS[fotoAtual][1];

  // Posição do pedaço dentro da foto (peça n = posição n-1 na foto original)
  function posicaoPedaco(posicao) {
    const linha = Math.floor(posicao / SIZE);
    const coluna = posicao % SIZE;
    return (coluna * 100 / (SIZE - 1)) + "% " + (linha * 100 / (SIZE - 1)) + "%";
  }

  function vizinhos(i) {
    const r = Math.floor(i / SIZE), c = i % SIZE, v = [];
    if (r > 0) v.push(i - SIZE);
    if (r < SIZE - 1) v.push(i + SIZE);
    if (c > 0) v.push(i - 1);
    if (c < SIZE - 1) v.push(i + 1);
    return v;
  }

  // Embaralha com jogadas válidas: o jogo SEMPRE tem solução.
  function embaralhar() {
    do {
      tiles = resolvido();
      let vazio = TOTAL - 1, anterior = -1;
      for (let k = 0; k < 200; k++) {
        const opcoes = vizinhos(vazio).filter(x => x !== anterior);
        const pick = opcoes[Math.floor(Math.random() * opcoes.length)];
        tiles[vazio] = tiles[pick];
        tiles[pick] = 0;
        anterior = vazio;
        vazio = pick;
      }
    } while (estaResolvido());
  }

  function formatar(s) {
    return String(Math.floor(s / 60)).padStart(2, "0") + ":" +
           String(s % 60).padStart(2, "0");
  }

  function lerRecorde() {
    try { return parseInt(localStorage.getItem(CHAVE_RECORDE), 10) || null; }
    catch (e) { return null; }
  }
  function salvarRecorde(n) {
    try { localStorage.setItem(CHAVE_RECORDE, String(n)); } catch (e) {}
  }
  function mostrarRecorde() {
    const r = lerRecorde();
    bestEl.textContent = r ? r + " mov." : "—";
  }

  function desenhar() {
    board.innerHTML = "";
    tiles.forEach((n, i) => {
      if (n === 0) {
        const vazio = document.createElement("div");
        vazio.className = "j15-vazio";
        board.appendChild(vazio);
        return;
      }
      const b = document.createElement("button");
      b.type = "button";
      b.className = "j15-peca";
      b.style.backgroundImage = 'url("' + urlFoto() + '")';
      b.style.backgroundPosition = posicaoPedaco(n - 1);
      b.setAttribute("aria-label", "Peça " + n);
      b.innerHTML = "<small>" + n + "</small>";
      b.addEventListener("click", () => mover(i));
      board.appendChild(b);
    });
    movesEl.textContent = moves;
    timeEl.textContent = formatar(seconds);
  }

  function mover(i) {
    const vazio = tiles.indexOf(0);
    if (!vizinhos(vazio).includes(i)) return;

    if (!timer) {
      timer = setInterval(() => {
        seconds++;
        timeEl.textContent = formatar(seconds);
      }, 1000);
    }

    [tiles[vazio], tiles[i]] = [tiles[i], tiles[vazio]];
    moves++;
    desenhar();
    if (estaResolvido()) vitoria();
  }

  function vitoria() {
    clearInterval(timer);
    timer = null;

    // Completa a foto: o espaço vazio ganha o último pedaço
    const vazio = board.querySelector(".j15-vazio");
    if (vazio) {
      vazio.classList.add("j15-peca");
      vazio.style.backgroundImage = 'url("' + urlFoto() + '")';
      vazio.style.backgroundPosition = posicaoPedaco(TOTAL - 1);
    }
    board.classList.add("j15-fim");

    let texto = "🎉 Parabéns! " + nomeFoto() + " montada em " + moves +
                " movimentos e " + formatar(seconds) + ".";
    const recorde = lerRecorde();
    if (!recorde || moves < recorde) {
      salvarRecorde(moves);
      mostrarRecorde();
      texto += " Novo recorde!";
    }
    msgEl.textContent = texto;
  }

  // Setas do teclado (com o tabuleiro focado)
  board.addEventListener("keydown", e => {
    const vazio = tiles.indexOf(0);
    const alvo = {
      ArrowUp: vazio + SIZE, ArrowDown: vazio - SIZE,
      ArrowLeft: vazio + 1, ArrowRight: vazio - 1
    }[e.key];
    if (alvo === undefined) return;
    e.preventDefault();
    if (alvo >= 0 && alvo < TOTAL) mover(alvo);
  });

  // Avisa se a foto não for encontrada (caminho ou nome errado)
  function verificarFoto() {
    const teste = new Image();
    teste.onerror = () => {
      msgEl.textContent = "⚠️ Foto não encontrada: " + urlFoto();
    };
    teste.src = urlFoto();
  }

  function novoJogo(trocarFoto) {
    clearInterval(timer);
    timer = null;
    if (trocarFoto) fotoAtual = (fotoAtual + 1) % FOTOS.length;
    moves = 0;
    seconds = 0;
    msgEl.textContent = "";
    board.classList.remove("j15-fim");
    refImg.src = urlFoto();
    refNome.textContent = nomeFoto();
    embaralhar();
    desenhar();
    mostrarRecorde();
    verificarFoto();
  }

  novoJogo(false);
})();