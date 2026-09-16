/* ============================================================
   BioSistema — Mapa Interativo (Fauna & Flora do Brasil)
   Tecnologia: Leaflet + OpenStreetMap + GeoJSON
   Depende de: mapa_data.js (BIOMAS e ESTADOS)
   ============================================================ */

document.addEventListener("DOMContentLoaded", function () {

  const elMapa = document.getElementById("mapaBrasil");
  if (!elMapa) return; // segurança: só roda se o mapa existir na página

  /* ----------------------------------------------------------
     1) Inicializa o mapa
     ---------------------------------------------------------- */
  const mapa = L.map("mapaBrasil", {
    center: [-14.5, -52],
    zoom: 4,
    minZoom: 3,
    maxZoom: 9,
    zoomControl: true,
    scrollWheelZoom: false // evita "sequestrar" o scroll da página
  });

  /* ----------------------------------------------------------
     2) Camada base (OpenStreetMap)
     ---------------------------------------------------------- */
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(mapa);

  /* ----------------------------------------------------------
     3) Legenda de biomas
     ---------------------------------------------------------- */
  const elLegenda = document.getElementById("mapaLegenda");
  if (elLegenda) {
    Object.entries(BIOMAS).forEach(([nome, cfg]) => {
      const item = document.createElement("div");
      item.className = "legenda-item";
      item.innerHTML =
        `<span class="legenda-cor" style="background:${cfg.cor}"></span>${cfg.emoji} ${nome}`;
      elLegenda.appendChild(item);
    });
  }

  /* ----------------------------------------------------------
     4) Estilo de cada estado conforme o bioma
     ---------------------------------------------------------- */
  function estilo(feature) {
    const sigla = feature.properties.sigla;
    const info = ESTADOS[sigla];
    const cor = info && BIOMAS[info.bioma] ? BIOMAS[info.bioma].cor : "#9aa7b3";
    return {
      color: "#ffffff",
      weight: 1.2,
      fillColor: cor,
      fillOpacity: 0.75
    };
  }

  /* ----------------------------------------------------------
     5) Elementos do painel
     ---------------------------------------------------------- */
  const painelVazio   = document.getElementById("painelVazio");
  const painelConteudo = document.getElementById("painelConteudo");
  const biomaBadge    = document.getElementById("biomaBadge");
  const estadoNome    = document.getElementById("estadoNome");
  const animalIcone   = document.getElementById("animalIcone");
  const animalNome    = document.getElementById("animalNome");
  const animalDesc    = document.getElementById("animalDesc");
  const vegIcone      = document.getElementById("vegIcone");
  const vegNome       = document.getElementById("vegNome");
  const vegDesc       = document.getElementById("vegDesc");

  /* Cards clicáveis (levam à página de detalhes) */
  const cardAnimal    = document.getElementById("cardAnimal");
  const cardVegetacao = document.getElementById("cardVegetacao");

  let camadaAtiva = null;
  let estadoAtual = null; // guarda a sigla do estado selecionado

  /* ----------------------------------------------------------
     5.1) Abre a página de detalhes de um item
     ---------------------------------------------------------- */
  function abrirDetalhe(tipo) {
    if (!estadoAtual) return;
    const info = ESTADOS[estadoAtual];
    if (!info) return;

    const nome = tipo === "vegetacao" ? info.vegetacao : info.animal;
    const desc = tipo === "vegetacao" ? info.vegetacaoDesc : info.animalDesc;

    const params = new URLSearchParams({
      tipo: tipo,
      nome: nome,
      estado: info.nome,
      bioma: info.bioma,
      desc: desc
    });

    window.location.href = "/detalhe?" + params.toString();
  }

  if (cardAnimal) {
    cardAnimal.addEventListener("click", function () { abrirDetalhe("animal"); });
    cardAnimal.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); abrirDetalhe("animal"); }
    });
  }

  if (cardVegetacao) {
    cardVegetacao.addEventListener("click", function () { abrirDetalhe("vegetacao"); });
    cardVegetacao.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); abrirDetalhe("vegetacao"); }
    });
  }

  /* ----------------------------------------------------------
     6) Preenche o painel lateral
     ---------------------------------------------------------- */
  function mostrarPainel(sigla) {
    const info = ESTADOS[sigla];
    if (!info) return;

    estadoAtual = sigla;

    painelVazio.style.display = "none";
    painelConteudo.style.display = "block";

    biomaBadge.textContent = info.bioma;
    biomaBadge.style.background =
      BIOMAS[info.bioma] ? BIOMAS[info.bioma].cor : "#18a999";

    estadoNome.textContent = info.nome;

    animalIcone.textContent = info.animalIcon;
    animalNome.textContent = info.animal;
    animalDesc.textContent = info.animalDesc;

    vegIcone.textContent = info.vegetacaoIcon;
    vegNome.textContent = info.vegetacao;
    vegDesc.textContent = info.vegetacaoDesc;
  }

  /* ----------------------------------------------------------
     7) Interações por estado
     ---------------------------------------------------------- */
  function aoCriarFeature(feature, layer) {
    const sigla = feature.properties.sigla;
    const nome  = feature.properties.name;
    const info  = ESTADOS[sigla];

    layer.on({
      mouseover: function (e) {
        e.target.setStyle({ weight: 2.5, color: "#18a999", fillOpacity: 0.92 });
        e.target.bringToFront();
      },
      mouseout: function (e) {
        if (camadaAtiva) camadaAtiva.setStyle(estilo(camadaAtiva.feature));
        e.target.setStyle(estilo(feature));
      },
      click: function (e) {
        camadaAtiva = e.target;
        mostrarPainel(sigla);

        const popup = `
          <div class="popup-titulo">${nome} (${sigla})</div>
          <div class="popup-linha">🐾 <b>${info ? info.animal : "—"}</b></div>
          <div class="popup-linha">🌳 <b>${info ? info.vegetacao : "—"}</b></div>
          <div class="popup-linha">🌎 ${info ? info.bioma : "—"}</div>
        `;
        e.target.bindPopup(popup, { maxWidth: 260 }).openPopup();
      }
    });
  }

  /* ----------------------------------------------------------
     8) Carrega o GeoJSON dos estados
     ---------------------------------------------------------- */
  fetch("/static/data/br_estados.json")
    .then(function (r) { return r.json(); })
    .then(function (geo) {
      L.geoJSON(geo, {
        style: estilo,
        onEachFeature: aoCriarFeature
      }).addTo(mapa);
    })
    .catch(function (err) {
      console.error("Erro ao carregar o GeoJSON:", err);
      elMapa.innerHTML =
        '<p style="padding:20px;font-family:Arial">Não foi possível carregar o mapa.</p>';
    });

});
