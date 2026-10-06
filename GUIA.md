# Guia de operação — Instagram @naptfit

Este repositório é a base de trabalho dos posts do NaptFit. Toda execução da rotina
começa lendo, nesta ordem: este GUIA.md, `briefing-original.md`, `funcionalidades.md`
e `historico.md`.

## 1. Regras do responsável (prevalecem sobre qualquer outra coisa)

1. **Siga integralmente o `briefing-original.md`**: não inventar dados, revisão científica,
   português impecável, tom de voz, checklist da seção 21, regra de incerteza.
2. **Nada de perguntas ou chamadas para comentar.** Nenhum post termina com pergunta ao
   público ("E você...?", "Conta nos comentários", "Qual é o seu...?"). Os comentários
   ficam desativados. CTAs permitidos: salvar, compartilhar, conclusão/reflexão afirmativa,
   apresentar o NaptFit ou um recurso real do app — variando entre eles.
3. **Frequência:** 1 post por dia útil (segunda a sexta), às **10h** (America/Fortaleza).
   Sem posts em sábado e domingo.
4. **Limite do plano gratuito do Metricool: 20 posts agendados por mês.** Antes de criar
   um post, conte no `historico.md` quantos posts já existem no mês da publicação.
   Se já houver 20, não crie; registre que o limite foi atingido.
5. **Publicação automática autorizada** pelo responsável (06/10/2026): o post é criado
   no Metricool com `draft: false` e `autoPublish: true`.
6. **Funcionalidades do app:** somente as de `funcionalidades.md`, com os detalhes
   exatamente como estão lá. Nunca diga que um recurso ⭐ é gratuito. Não cite
   "Comunidade" enquanto não houver descrição.
7. **Proporção:** a maioria dos posts é conteúdo útil; no máximo 1 post por semana
   centrado no produto. Nos demais, o NaptFit entra só quando fizer sentido.

## 2. Identidade visual

- Formato: carrossel ou post único em **1080 × 1350 px** (4:5). Carrossel de 4 a 7 slides.
- Cores: verde da marca `#20AC53`, preto `#111111`, fundo creme `#EEEDE6`, branco `#FFFFFF`,
  texto secundário `#5E5E58`. Slides escuros: fundo `#111111`.
- Tipografia: títulos em **Montserrat** 700–800 (mesma família da logo); texto corrido em **Inter**.
- Logo: `modelo/logo-word-dark.png` (fundo claro) e `modelo/logo-word-light.png` (fundo escuro),
  no canto superior esquerdo, 54 px de altura. Também há `logo-icon.png` e os lockups com o
  slogan "Viva sua melhor versão".
- Número do slide (1/5) no canto superior direito; fonte de dados no rodapé quando houver números.
- Primeiro e último slides em fundo escuro; miolo em fundo creme. Pode variar, mantendo a paleta.
- Referência pronta: `2026-10-06-arroz-cru-cozido/slides.html`. Copie o `<style>` e adapte o layout.
- Pouco texto por slide, uma ideia por slide, letras grandes (legível no celular).

## 3. Passo a passo de cada post

1. **Planejar:** leia o `historico.md` e escolha um tema e um tipo de conteúdo diferentes dos
   últimos posts (veja a lista da seção 8 do briefing). Varie gancho, estrutura e CTA.
2. **Pesquisar e verificar ANTES de escrever:** toda afirmação factual precisa de fonte
   confiável. Composição de alimentos: PDF oficial da TACO 4ª ed.
   (https://nepa.unicamp.br/wp-content/uploads/sites/27/2023/10/taco_4_edicao_ampliada_e_revisada.pdf)
   ou TBCA (https://www.tbca.net.br). Fisiologia: literatura revisada por pares ou
   instituições oficiais. Se não confirmar, não use. Nunca use sites agregadores
   como fonte de números.
3. **Escrever** a arte e a legenda. Legenda com fonte no final ("Fonte: TACO / NEPA-UNICAMP")
   e 3 a 5 hashtags específicas.
4. **Revisar** com o checklist da seção 21 do briefing + a regra 2 deste guia (sem perguntas).
   Releia o português como revisor profissional.
5. **Gerar as imagens:** crie a pasta `AAAA-MM-DD-tema-curto/` com `slides.html`
   (logos via `../modelo/`, fontes via `../node_modules/`), depois:
   `npm install` (uma vez) e `python3 modelo/render.py AAAA-MM-DD-tema-curto`.
   Abra as imagens geradas e confira se nada quebrou (texto cortado, número quebrando linha).
6. **Salvar a legenda** em `legenda.txt` na pasta do post.
7. **Publicar no GitHub:** `git add -A && git commit && git push` na branch `main`.
   Confirme que as imagens respondem em
   `https://raw.githubusercontent.com/naptfit/naptfit-posts/main/<pasta>/<arquivo>.png`.
8. **Agendar no Metricool** (brand/blogId `7270616`, Instagram), com `createScheduledPost`:
   - `date`: `AAAA-MM-DDT10:00:00-03:00`
   - `info`: `{"autoPublish": true, "draft": false, "descendants": [], "firstCommentText": "",
     "hasNotReadNotes": false, "media": [<URLs raw na ordem dos slides>], "mediaAltText": [],
     "providers": [{"network": "instagram"}], "publicationDate": {"dateTime": "AAAA-MM-DDT10:00:00",
     "timezone": "America/Fortaleza"}, "shortener": false, "smartLinkData": {"ids": []},
     "text": <legenda>, "instagramData": {"type": "POST", "collaborators": [],
     "showReelOnFeed": true, "isAiGenerated": false}}`
9. **Registrar** a linha no `historico.md` (com o uuid retornado) e fazer push.

## 4. Observações

- Comentários: o Metricool não desativa comentários no Instagram. O responsável desativa
  manualmente no app após a publicação.
- O Metricool copia as imagens para o servidor dele ao agendar; o GitHub serve só de ponte.
