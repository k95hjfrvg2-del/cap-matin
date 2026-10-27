# Cap Matin — recette de production

Podcast quotidien en français, 7 jours sur 7, pour Nicolas (Londres ; famille et attaches à Paris,
Asnières-sur-Seine et Audierne, dans le Finistère). Publié dans le fil Apple Podcasts **avant 6h00,
heure de Paris** (la tâche démarre à 4h07 heure de Paris, car la recherche et le rendu de la voix prennent environ 1 heure). Fil : `https://k95hjfrvg2-del.github.io/cap-matin/feed.xml`.

Ce dépôt ne contient que Cap Matin. Ne jamais toucher au dépôt `le-petit-matin` (autre podcast).

## 0. Avant tout : un seul épisode par jour

1. Après `git pull`, si `scripts/cap_matin_<date du jour, heure de Paris>.txt` **existe déjà** sur
   main, une autre session s'occupe déjà de l'épisode du jour : **ne rien faire**, ne rien
   committer, et répondre en une phrase « Cap Matin du jour déjà pris en charge par une autre
   tâche ».
2. Sinon, **dès que le script est écrit**, le committer et le pousser tout de suite sur main
   (message « Cap Matin <date> : script »), **avant** de lancer le rendu de la voix. Cela réserve
   l'épisode du jour et évite qu'une autre tâche le fasse en double.

## Règles de Nicolas (non négociables)

- **Durée : 7 à 8 minutes maximum** (viser 5 min 30 à 7 min 30, soit environ 950 à 1 150 mots).
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
- Anniversaire du jour d'une personne de la liste : l'annoncer en premier, avec chaleur
  (« Aujourd'hui, on souhaite un très joyeux anniversaire à Camille ! »). Le 20 juillet : souhaiter
  directement son anniversaire à Nicolas.
- **Personnes décédées** (`"decede": true`, ex. Mémé et Pépé) : ne JAMAIS dire « joyeux
  anniversaire ». Rappeler sobrement que c'est leur jour de naissance et l'âge qu'ils auraient eu
  (année en cours moins `annee_naissance`) : « Aujourd'hui, c'est le jour de naissance de Pépé :
  il aurait eu cent ans. » Sans âge si l'année est inconnue.
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

`###` **Section 7 bis — Une histoire de marin et de la mer** (≈ 90 mots) : une histoire vraie et
vérifiée de marins ou de mer — naufrage, sauvetage, exploit, phare, gardien de phare, course au
large, pêcheurs, légende bretonne (en la présentant comme une légende), découverte
océanographique… De préférence en Bretagne ou en France, sinon dans le monde. Raconter comme une
histoire (un personnage, un moment, un dénouement), avec un lieu et une date.

`###` **Section 7 ter — Le poisson du jour** (≈ 70 mots) : un poisson (ou animal marin) à chaque
fois différent, avec **toujours** : son nom courant, **son nom latin** (genre et espèce, dit
lentement, par ex. « Dicentrarchus labrax »), **son poids** (moyen et record ou maximum), **où on le
trouve** (mers, profondeur, côtes bretonnes si c'est le cas), **qui le mange** (ses prédateurs,
et l'homme si c'est le cas) **et comment on le mange** (une façon de le cuisiner, ou comment ses
prédateurs le chassent). Sources fiables : FishBase, DORIS (doris.ffessm.fr), Ifremer, MNHN.
Privilégier les poissons de l'Atlantique et de la Manche, sans négliger le reste du monde.

`###` **Section 8 — Le fait culturel** (≈ 70 mots), avec un détail vivant.

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
  culturel, un événement historique, un philosophe ou une citation, ni une histoire de marin ;
  **ne jamais répéter un poisson** déjà présenté (champ `poisson`). Ajouter l'épisode du jour en
  tête de `history.json` (même format, avec la voix utilisée et les champs `marin` et `poisson`).

## 3. Écrire pour l'oreille

- Nombres, dates, heures en toutes lettres (« seize heures treize », « coefficient
  quatre-vingt-deux », « mille neuf cent quarante-cinq »).
- Paragraphes courts (moins de 90 mots), un paragraphe par ligne, sections séparées par une ligne
  `###` (voir déroulé). Le script : `scripts/cap_matin_YYYY-MM-DD.txt`.
- Vérifier le nombre de mots : `wc -w` (950 à 1 150).

## 4. Prononciation (règles de Nicolas)

- **Asnières se dit « Anière »** : on ne prononce jamais les S (déjà dans `prononciation.txt`).
- **Les noms, prénoms et mots courants anglais se disent avec l'accent anglais**, jamais « à la
  française » (Trump, Elon Musk, New York, Central Park, Starlink…). Plus généralement, chaque mot
  étranger se dit comme dans sa langue d'origine.
- La voix lit tout « à la française » : pour chaque nom anglais ou étranger du script qui n'est pas
  encore dans `prononciation.txt`, ajouter une ligne `Orthographe => graphie phonétique française`
  qui imite la prononciation d'origine (ex. `Donald Trump => Donald Treumpe`,
  `New York => Niou Yorque`). Garder l'orthographe correcte dans le script : le remplacement est
  appliqué automatiquement avant la lecture. Faire de même pour les noms bretons difficiles.

## 5. Audio

Voix : **Kyutai TTS 1.6B en_fr, voix « L »** — la même que Petit Matin Good Vibes, gratuite et libre
(licence CC-BY 4.0). Une seule voix, tous les jours. Ne pas la changer sans l'accord de Nicolas.
Jamais de voix Microsoft (conditions d'usage incertaines pour un podcast public).

Musique et sons (dans `assets/`, ne pas régénérer) : générique breton acoustique au début et à la
fin ; vague après la météo ; harpe ou piano au hasard entre les autres sections ; pauses courtes.

Installation (≈5 minutes, à lancer en arrière-plan **dès le début**, pendant la recherche) :

```bash
pip install --break-system-packages -q torch torchaudio moshi
```

(Le modèle Kyutai, ≈3 Go, se télécharge tout seul depuis huggingface.co au premier rendu.)

Rendu : **compter 7 à 8 fois la durée audio, soit 40 à 55 minutes** pour un épisode de 6 minutes.
Le lancer en arrière-plan dès que le script est final (reprise possible : les paragraphes déjà
rendus sont conservés dans le dossier de travail) :

```bash
python3 tools/make_episode.py scripts/cap_matin_YYYY-MM-DD.txt /tmp/Cap_Matin_YYYY-MM-DD.mp3 YYYY-MM-DD > /tmp/render.log 2>&1
```

Suivre la progression dans /tmp/render.log (une ligne « i n » par paragraphe). Vérifier la durée
affichée à la fin (**7 min 30 maximum**).

**TRÈS IMPORTANT — ne jamais terminer la session avant la fin du rendu.** Dans une tâche
automatique, tout ce qui tourne encore en arrière-plan est coupé dès que la session répond pour la
dernière fois : le 26 octobre, l'épisode n'a pas été publié à cause de ça. Après avoir lancé le
rendu, **attendre activement** qu'il soit fini, par tranches de moins de 10 minutes, par exemple :

```bash
until grep -qE "^OK |Error|Traceback" /tmp/render.log; do sleep 20; done; tail -3 /tmp/render.log
```

(à relancer autant de fois que nécessaire, avec un délai d'attente de 10 minutes). Si une attente
est coupée, relancer la même commande de rendu : elle reprend là où elle s'était arrêtée. Ne
répondre à Nicolas qu'**après** la publication et le push.

## 6. Publication

```bash
python3 publish_episode.py . https://k95hjfrvg2-del.github.io/cap-matin /tmp/Cap_Matin_YYYY-MM-DD.mp3 "<Jour JJ mois> : <titre de 3 à 6 mots>" "<une phrase résumant l'épisode>" YYYY-MM-DD
```

Puis commit (auteur Claude <noreply@anthropic.com>, message « Cap Matin YYYY-MM-DD ») de
`episodes/`, `episodes.json`, `feed.xml`, `history.json`, `scripts/`, `prononciation.txt` ; push
sur main. Jamais de force-push ni de réécriture d'historique.
