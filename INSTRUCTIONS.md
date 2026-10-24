# Cap Matin — recette de production

Podcast quotidien en français, 7 jours sur 7, pour Nicolas (Londres ; famille et attaches à Paris,
Asnières-sur-Seine et Audierne, dans le Finistère). Publié dans le fil Apple Podcasts **avant 6h00,
heure de Paris**. Fil : `https://k95hjfrvg2-del.github.io/cap-matin/feed.xml`.

Ce dépôt ne contient que Cap Matin. Ne jamais toucher au dépôt `le-petit-matin` (autre podcast).

## Règles de Nicolas (non négociables)

- **Durée : 7 à 8 minutes maximum** (viser 5 min 30 à 7 min 30, soit environ 800 à 1 050 mots).
- **Une seule voix par épisode**, celle du jour (voir section 5). Jamais de duo ni de mélange de voix.
- **Ton dynamique = énergie, pas vitesse** : phrases courtes, exclamations, questions au public,
  petites réactions (« Bravo ! », « Impressionnant ! »). Ne jamais accélérer le débit de la voix.
- **Aucune info sur la route, la circulation, les bouchons ou Bison Futé.**
- **Transitions naturelles** : chaque sujet s'enchaîne au précédent par une phrase de liaison
  (« Après ces nouvelles un peu lourdes, on respire un grand coup… », « De New York, on revient à
  Paris… », « Et ce changement d'heure nous amène tout naturellement à… »). Jamais « rubrique
  suivante », jamais de numérotation.

## 1. Déroulé (toujours dans cet ordre)

**Section 1 — Ouverture** : « Bonjour à tous, et bienvenue dans Cap Matin ! Nous sommes le <jour>
<date>… »

**Fêtes et anniversaires de la famille (dans la section 1, SEULEMENT s'il y en a aujourd'hui)** :
lire `anniversaires.json` et comparer avec la date du jour (heure de Paris).
- Anniversaire du jour d'une personne de la liste : l'annoncer en premier, avec chaleur mais
  sobriété (certaines personnes sont décédées) : « Aujourd'hui, on pense à Mémé, dont c'est
  l'anniversaire. » Le 20 juillet : souhaiter directement son anniversaire à Nicolas.
- Fête du prénom : uniquement si un prénom de `prenoms_pour_les_fetes` est fêté aujourd'hui dans le
  calendrier français (vérifier sur nominis.cef.fr ou un calendrier des fêtes). Jamais le saint du
  jour s'il n'est pas dans la liste.
- **Jamais** de rappel la veille ou à l'avance, **jamais** « pensez à l'appeler / lui écrire ».
- **S'il n'y a ni anniversaire ni fête de la famille aujourd'hui : ne rien dire du tout** sur ce
  sujet ; enchaîner directement vers la météo (« … et on commence tout de suite par le ciel. »).

`###`

**Section 2 — Météo express (30 à 45 secondes, 75 à 110 mots maximum)** :
Audierne (temps, vent si notable, températures), température de la mer, pleine mer et basse mer de
l'après-midi/soirée avec le coefficient (heures françaises, en toutes lettres), grandes marées si
coefficient ≥ 90 ; Asnières-sur-Seine (temps, températures) ; une phrase sur demain seulement s'il
y a un vrai changement. Changement d'heure : le signaler la veille et le jour même.

`###` (une vague est jouée ici automatiquement)

**Section 3 — France** (2 ou 3 infos, ≈ 50 mots chacune) : les sujets importants des dernières
24 heures. Factuel, neutre. Pas de circulation.

`###` **Section 4 — Le monde** (1 info, ≈ 55 mots).

`###` **Section 5 — Deux bonnes nouvelles** (≈ 60 mots chacune), récentes (moins d'une semaine),
vérifiées.

`###` **Section 6 — Paris** (≈ 60 mots) : une nouvelle de Paris ou d'Asnières / Hauts-de-Seine.
**S'il y a de nouvelles expositions à Paris** (ouvertes dans les 7 derniers jours ou ouvrant dans
les 7 prochains), en citer une ou deux (lieu + titre) — sources : timeout.fr, sortiraparis.com.

`###` **Section 7 — Audierne / Cap Sizun / Finistère** (≈ 60 mots). Sources : audierne.bzh,
Ouest-France, Le Télégramme, France 3 Bretagne, meteo.bzh.

`###` **Section 8 — Le fait culturel** (≈ 80 mots), avec un détail vivant.

`###` **Le mercredi seulement — Les sorties cinéma** (≈ 100 mots) : deux ou trois films qui sortent
ce mercredi en France, de préférence français, européens, d'auteur ou asiatiques ; **jamais de
blockbusters américains** (super-héros, Marvel, DC, grandes franchises).

`###` **Section 9 — Le fait historique** (≈ 80 mots), de préférence survenu à la même date.

`###` **Section 10 — La minute philo** (≈ 100 mots) : une idée d'un philosophe, citation
authentique et vérifiée, application concrète pour la journée. Varier les auteurs.

`###` **Clôture** (≈ 25 mots) : un clin d'œil à la météo du jour, « Très bonne journée à tous, et à
demain ! » (le week-end : « Très bon week-end »).

## 2. Recherche (≈ 15 minutes)

Le terminal n'a pas accès aux sites web : utiliser **WebSearch** puis **WebFetch** sur les liens
trouvés.
- Marées Audierne : maree.info/87 (prédictions SHOM, heures et coefficients du jour).
- Météo Audierne / Bretagne : meteo.bzh (bulletin régional du jour), lachainemeteo, franceinfo
  météo. Vigilances : audierne.bzh.
- Mer : « température eau Audierne » (cabaigne.net, seatemperature.net) ; à défaut une valeur
  approchée (« autour de quatorze degrés »).
- Asnières / Paris : meteo.franceinfo.fr, sortiraparis.com (météo du week-end).
- Actualité : sources fiables et datées (franceinfo, Le Monde, AFP, France 24, Ouest-France…).
  Bonnes nouvelles : lemediapositif.com, bonnesnouvellesdujour.fr — toujours vérifier ailleurs.
- Ne rien inventer ; paraphraser.
- **Anti-répétition** : lire `history.json`. Ne pas répéter dans les 30 derniers jours un fait
  culturel, un événement historique, un philosophe ou une citation. Ajouter l'épisode du jour en
  tête de `history.json` (même format, avec la voix utilisée).

## 3. Écrire pour l'oreille

- Nombres, dates, heures en toutes lettres (« seize heures treize », « coefficient
  quatre-vingt-deux », « mille neuf cent quarante-cinq »).
- Paragraphes courts (moins de 90 mots), un paragraphe par ligne, sections séparées par une ligne
  `###` (voir déroulé). Le script : `scripts/cap_matin_YYYY-MM-DD.txt`.
- Vérifier le nombre de mots : `wc -w` (800 à 1 050).

## 4. Prononciation

Les voix Microsoft lisent bien les noms. Si un nom est mal lu, ajouter une ligne
`Orthographe => graphie phonétique` dans `prononciation.txt`.

## 5. Audio

Voix : Microsoft (edge-tts), **une par jour**, choisie automatiquement par `tools/make_episode.py`
selon le jour de la semaine (heure de Paris) :
lundi Vivienne, mardi Henri, mercredi Denise, jeudi Rémy, vendredi Ava, samedi Ariane,
dimanche Rémy. Ne pas changer sans l'accord de Nicolas.

Musique et sons (dans `assets/`, ne pas régénérer) : générique breton acoustique au début et à la
fin ; vague après la météo ; harpe ou piano au hasard entre les autres sections ; pauses courtes.

```bash
pip install --break-system-packages -q edge-tts
python3 tools/make_episode.py scripts/cap_matin_YYYY-MM-DD.txt /tmp/Cap_Matin_YYYY-MM-DD.mp3 YYYY-MM-DD
```

Le script utilise automatiquement le proxy (`HTTPS_PROXY`) et refait toute phrase dont l'audio sort
tronqué. Vérifier la durée affichée (**7 min 30 maximum** ; sinon raccourcir le texte et relancer).

## 6. Publication

```bash
python3 publish_episode.py . https://k95hjfrvg2-del.github.io/cap-matin /tmp/Cap_Matin_YYYY-MM-DD.mp3 "<Jour JJ mois> : <titre de 3 à 6 mots>" "<une phrase résumant l'épisode>" YYYY-MM-DD
```

Puis commit (auteur Claude <noreply@anthropic.com>, message « Cap Matin YYYY-MM-DD ») de
`episodes/`, `episodes.json`, `feed.xml`, `history.json`, `scripts/`, `prononciation.txt` ; push
sur main. Jamais de force-push ni de réécriture d'historique.
