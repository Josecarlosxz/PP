/* ============================================================
   BioSistema — Dados do Mapa Interativo
   Fauna e Flora por estado / bioma do Brasil
   ------------------------------------------------------------
   Para editar: altere os campos de cada estado abaixo.
   ============================================================ */

/* Cores oficiais de cada bioma (usadas no mapa e na legenda) */
const BIOMAS = {
  "Amazônia":      { cor: "#1b7a3d", emoji: "🌳" },
  "Cerrado":       { cor: "#d9a521", emoji: "🌾" },
  "Caatinga":      { cor: "#b5451f", emoji: "🌵" },
  "Mata Atlântica":{ cor: "#1f8a8a", emoji: "🌲" },
  "Pantanal":      { cor: "#7b52ab", emoji: "🐊" },
  "Pampa":         { cor: "#4a6fa5", emoji: "🐎" }
};

/* ------------------------------------------------------------
   DADOS POR ESTADO
   sigla -> { nome, bioma, animal, animalIcon, animalDesc,
              vegetacao, vegetacaoIcon, vegetacaoDesc }
   ------------------------------------------------------------ */
const ESTADOS = {

  /* ================= NORTE ================= */
  AC: { nome: "Acre", bioma: "Amazônia",
    animal: "Arara-vermelha", animalIcon: "🦜",
    animalDesc: "Ave de plumagem vermelha vibrante, símbolo das florestas acreanas.",
    vegetacao: "Floresta Ombrófila Aberta", vegetacaoIcon: "🌴",
    vegetacaoDesc: "Floresta tropical úmida com palmeiras e bambus, típica do oeste amazônico." },

  AP: { nome: "Amapá", bioma: "Amazônia",
    animal: "Ariranha", animalIcon: "🦦",
    animalDesc: "Grande lontra amazônica que vive em rios e igarapés.",
    vegetacao: "Floresta de Várzea e Igapó", vegetacaoIcon: "🌊",
    vegetacaoDesc: "Vegetação inundável que acompanha os rios nas cheias sazonais." },

  AM: { nome: "Amazonas", bioma: "Amazônia",
    animal: "Boto-cor-de-rosa", animalIcon: "🐬",
    animalDesc: "Cetáceo de água doce símbolo da Amazônia, cercado de lendas.",
    vegetacao: "Floresta Ombrófila Densa", vegetacaoIcon: "🌳",
    vegetacaoDesc: "A maior floresta tropical do planeta, com altíssima biodiversidade." },

  PA: { nome: "Pará", bioma: "Amazônia",
    animal: "Onça-pintada", animalIcon: "🐆",
    animalDesc: "Maior felino das Américas, predador de topo da cadeia amazônica.",
    vegetacao: "Floresta Densa e Manguezais", vegetacaoIcon: "🌴",
    vegetacaoDesc: "Floresta de terra firme e manguezais no litoral paraense." },

  RO: { nome: "Rondônia", bioma: "Amazônia",
    animal: "Tatu-canastra", animalIcon: "🦔",
    animalDesc: "Maior tatu do mundo, engenheiro do ecossistema que cava grandes tocas.",
    vegetacao: "Floresta Amazônica e Cerrado", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Transição entre floresta úmida e áreas de cerrado no sul do estado." },

  RR: { nome: "Roraima", bioma: "Amazônia",
    animal: "Anta", animalIcon: "🐗",
    animalDesc: "Maior mamífero terrestre do Brasil, importante dispersor de sementes.",
    vegetacao: "Lavrado (Savana Amazônica)", vegetacaoIcon: "🌾",
    vegetacaoDesc: "Campos abertos de savana intercalados com florestas de galeria." },

  TO: { nome: "Tocantins", bioma: "Cerrado",
    animal: "Lobo-guará", animalIcon: "🐺",
    animalDesc: "Maior canídeo da América do Sul, de pernas longas e pelagem avermelhada.",
    vegetacao: "Cerrado", vegetacaoIcon: "🌾",
    vegetacaoDesc: "Savana brasileira com árvores retorcidas, arbustos e gramíneas." },

  /* ================= NORDESTE ================= */
  MA: { nome: "Maranhão", bioma: "Cerrado",
    animal: "Arara-azul-grande", animalIcon: "🦜",
    animalDesc: "Ave de grande porte ameaçada, símbolo da conservação no Brasil.",
    vegetacao: "Mata dos Cocais (Babaçu)", vegetacaoIcon: "🌴",
    vegetacaoDesc: "Floresta de transição dominada por palmeiras de babaçu e carnaúba." },

  PI: { nome: "Piauí", bioma: "Caatinga",
    animal: "Tatu-bola", animalIcon: "🦔",
    animalDesc: "Tatu que se enrola em forma de bola; mascote da Copa de 2014.",
    vegetacao: "Caatinga e Cerrado", vegetacaoIcon: "🌵",
    vegetacaoDesc: "Vegetação xerófila adaptada à seca, com cactos e arbustos espinhosos." },

  CE: { nome: "Ceará", bioma: "Caatinga",
    animal: "Soldadinho-do-araripe", animalIcon: "🐦",
    animalDesc: "Pequena ave endêmica do Ceará, símbolo da Chapada do Araripe.",
    vegetacao: "Caatinga", vegetacaoIcon: "🌵",
    vegetacaoDesc: "Único bioma exclusivamente brasileiro, resistente à longa estiagem." },

  RN: { nome: "Rio Grande do Norte", bioma: "Caatinga",
    animal: "Peixe-boi-marinho", animalIcon: "🐋",
    animalDesc: "Mamífero aquático ameaçado, encontrado no litoral potiguar.",
    vegetacao: "Caatinga e Restinga", vegetacaoIcon: "🌵",
    vegetacaoDesc: "Vegetação seca do sertão e restingas arenosas no litoral." },

  PB: { nome: "Paraíba", bioma: "Caatinga",
    animal: "Peixe-boi-marinho", animalIcon: "🐋",
    animalDesc: "Herbívoro marinho que se alimenta de capim-marinho nas costas do Nordeste.",
    vegetacao: "Caatinga e Mata Atlântica", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Transição entre o sertão seco e remanescentes de floresta atlântica." },

  PE: { nome: "Pernambuco", bioma: "Caatinga",
    animal: "Onça-parda", animalIcon: "🐆",
    animalDesc: "Felino de ampla distribuição, também chamado de suçuarana ou puma.",
    vegetacao: "Caatinga e Mata Atlântica", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Mosaico de caatinga no interior e floresta atlântica na zona da mata." },

  AL: { nome: "Alagoas", bioma: "Mata Atlântica",
    animal: "Peixe-boi-marinho", animalIcon: "🐋",
    animalDesc: "Símbolo da conservação marinha, protegido em Alagoas.",
    vegetacao: "Mata Atlântica e Manguezais", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Floresta costeira e manguezais que abrigam rica vida marinha." },

  SE: { nome: "Sergipe", bioma: "Mata Atlântica",
    animal: "Peixe-boi-marinho", animalIcon: "🐋",
    animalDesc: "Mamífero marinho que habita estuários e águas costeiras sergipanas.",
    vegetacao: "Mata Atlântica e Manguezais", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Remanescentes de floresta atlântica e ecossistemas de mangue." },

  BA: { nome: "Bahia", bioma: "Caatinga",
    animal: "Arara-azul-de-lear", animalIcon: "🦜",
    animalDesc: "Ave criticamente ameaçada, endêmica da Caatinga baiana.",
    vegetacao: "Caatinga, Cerrado e Mata Atlântica", vegetacaoIcon: "🌵",
    vegetacaoDesc: "Estado com três grandes biomas, do sertão seco ao litoral úmido." },

  /* ================= CENTRO-OESTE ================= */
  MT: { nome: "Mato Grosso", bioma: "Pantanal",
    animal: "Onça-pintada", animalIcon: "🐆",
    animalDesc: "Maior felino das Américas, símbolo do Pantanal mato-grossense.",
    vegetacao: "Pantanal, Cerrado e Amazônia", vegetacaoIcon: "🌾",
    vegetacaoDesc: "Encontro de três biomas, com a maior planície alagável do mundo." },

  MS: { nome: "Mato Grosso do Sul", bioma: "Pantanal",
    animal: "Arara-azul", animalIcon: "🦜",
    animalDesc: "Ave de plumagem azul intensa, símbolo do Pantanal sul-mato-grossense.",
    vegetacao: "Pantanal e Cerrado", vegetacaoIcon: "🌾",
    vegetacaoDesc: "Planície inundável com rica vegetação aquática e campos sazonais." },

  GO: { nome: "Goiás", bioma: "Cerrado",
    animal: "Lobo-guará", animalIcon: "🐺",
    animalDesc: "Canídeo de hábitos solitários, típico das savanas do Cerrado.",
    vegetacao: "Cerrado", vegetacaoIcon: "🌾",
    vegetacaoDesc: "Savana com árvores tortuosas, cascas grossas e raízes profundas." },

  DF: { nome: "Distrito Federal", bioma: "Cerrado",
    animal: "Lobo-guará", animalIcon: "🐺",
    animalDesc: "Símbolo do Cerrado, avistado até em áreas urbanas do DF.",
    vegetacao: "Cerrado", vegetacaoIcon: "🌾",
    vegetacaoDesc: "Berço do Cerrado, com áreas de proteção como a Reserva do IBGE." },

  /* ================= SUDESTE ================= */
  MG: { nome: "Minas Gerais", bioma: "Cerrado",
    animal: "Lobo-guará", animalIcon: "🐺",
    animalDesc: "Maior canídeo da América do Sul, presente na Serra da Canastra.",
    vegetacao: "Cerrado e Mata Atlântica", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Mosaico de cerrado, campos de altitude e floresta atlântica." },

  ES: { nome: "Espírito Santo", bioma: "Mata Atlântica",
    animal: "Baleia-jubarte", animalIcon: "🐋",
    animalDesc: "Baleia migratória que visita o litoral capixaba para se reproduzir.",
    vegetacao: "Mata Atlântica e Restinga", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Floresta costeira, restingas e manguezais ao longo do litoral." },

  RJ: { nome: "Rio de Janeiro", bioma: "Mata Atlântica",
    animal: "Mico-leão-dourado", animalIcon: "🐒",
    animalDesc: "Pequeno primata de juba dourada, símbolo da luta pela Mata Atlântica.",
    vegetacao: "Mata Atlântica", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Floresta tropical úmida, uma das mais ricas e ameaçadas do planeta." },

  SP: { nome: "São Paulo", bioma: "Mata Atlântica",
    animal: "Mico-leão-preto", animalIcon: "🐒",
    animalDesc: "Primata endêmico do interior paulista, ameaçado de extinção.",
    vegetacao: "Mata Atlântica e Cerrado", vegetacaoIcon: "🌳",
    vegetacaoDesc: "Floresta atlântica no litoral e cerrado no interior do estado." },

  /* ================= SUL ================= */
  PR: { nome: "Paraná", bioma: "Mata Atlântica",
    animal: "Gralha-azul", animalIcon: "🐦",
    animalDesc: "Ave azul símbolo do Paraná, grande dispersora de sementes de araucária.",
    vegetacao: "Floresta com Araucária", vegetacaoIcon: "🌲",
    vegetacaoDesc: "Floresta de pinheiros araucária, marca registrada do planalto sulista." },

  SC: { nome: "Santa Catarina", bioma: "Mata Atlântica",
    animal: "Papagaio-de-cara-roxa", animalIcon: "🦜",
    animalDesc: "Ave endêmica da costa sul, ameaçada pela perda de habitat.",
    vegetacao: "Floresta com Araucária e Restinga", vegetacaoIcon: "🌲",
    vegetacaoDesc: "Mata de araucárias no planalto e restingas no litoral catarinense." },

  RS: { nome: "Rio Grande do Sul", bioma: "Pampa",
    animal: "Quero-quero", animalIcon: "🐦",
    animalDesc: "Ave símbolo do Rio Grande do Sul, guardiã dos campos gaúchos.",
    vegetacao: "Pampa (Campos Sulinos)", vegetacaoIcon: "🌾",
    vegetacaoDesc: "Campos nativos de gramíneas, único bioma restrito a um só estado." }
};

/* ------------------------------------------------------------
   MAPA DE TÍTULOS DA WIKIPÉDIA
   ------------------------------------------------------------
   Alguns nomes usados no mapa não são exatamente o título do
   artigo na Wikipédia. Este mapa traduz o nome exibido para o
   título correto, garantindo que a página de detalhes encontre
   a imagem real e o texto completo.

   Se um nome não estiver aqui, o detalhe.js usa o próprio nome.
   ------------------------------------------------------------ */
const WIKI_TITULOS = {

  /* ---- ANIMAIS ---- */
  "Arara-vermelha":        "Arara-vermelha",
  "Ariranha":              "Ariranha",
  "Boto-cor-de-rosa":      "Boto-cor-de-rosa",
  "Onça-pintada":          "Onça-pintada",
  "Tatu-canastra":         "Tatu-canastra",
  "Anta":                  "Anta",
  "Lobo-guará":            "Lobo-guará",
  "Arara-azul-grande":     "Arara-azul-grande",
  "Tatu-bola":             "Tatu-bola",
  "Soldadinho-do-araripe": "Soldadinho-do-araripe",
  "Peixe-boi-marinho":     "Peixe-boi-marinho",
  "Onça-parda":            "Onça-parda",
  "Arara-azul-de-lear":    "Arara-azul-de-lear",
  "Arara-azul":            "Arara-azul",
  "Baleia-jubarte":        "Baleia-jubarte",
  "Mico-leão-dourado":     "Mico-leão-dourado",
  "Mico-leão-preto":       "Mico-leão-preto",
  "Gralha-azul":           "Gralha-azul",
  "Papagaio-de-cara-roxa": "Papagaio-de-cara-roxa",
  "Quero-quero":           "Quero-quero",

  /* ---- VEGETAÇÃO ---- */
  "Floresta Ombrófila Aberta":          "Floresta ombrófila aberta",
  "Floresta de Várzea e Igapó":         "Floresta de várzea",
  "Floresta Ombrófila Densa":           "Floresta ombrófila densa",
  "Floresta Densa e Manguezais":        "Manguezal",
  "Floresta Amazônica e Cerrado":       "Amazônia",
  "Lavrado (Savana Amazônica)":         "Lavrado",
  "Cerrado":                            "Cerrado",
  "Mata dos Cocais (Babaçu)":           "Mata dos cocais",
  "Caatinga e Cerrado":                 "Caatinga",
  "Caatinga":                           "Caatinga",
  "Caatinga e Restinga":                "Restinga",
  "Caatinga e Mata Atlântica":          "Caatinga",
  "Mata Atlântica e Manguezais":        "Mata Atlântica",
  "Mata Atlântica":                     "Mata Atlântica",
  "Caatinga, Cerrado e Mata Atlântica": "Caatinga",
  "Pantanal, Cerrado e Amazônia":       "Pantanal",
  "Pantanal e Cerrado":                 "Pantanal",
  "Cerrado e Mata Atlântica":           "Cerrado",
  "Mata Atlântica e Restinga":          "Mata Atlântica",
  "Mata Atlântica e Cerrado":           "Mata Atlântica",
  "Floresta com Araucária":             "Floresta ombrófila mista",
  "Floresta com Araucária e Restinga":  "Floresta ombrófila mista",
  "Pampa (Campos Sulinos)":             "Pampa"
};