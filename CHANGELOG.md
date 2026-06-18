# Changelog

## [v0.1.18] - 2026-06-19

### Changed
- Proper name normalization across all volume-3 files (34 files):

  **Deity names (Greek/Roman context rule applied)**
  - Greek lives: `Cérès`→`Demeter`, `Jupiter`→`Zeus`, `Bacchus`→`Dionysus`,
    `Hercule`→`Heracles`, `Junon`→`Hera`, `Phébus`→`Phoebus`
  - Roman lives: `Vénus`→`Venus`, `Cérès`→`Ceres`, `Bacchus` stays, `Jupiter` stays

  **Proper names (French → English/Latin/Greek) per file**
  - `01-cimon.md` (Greek): `Athènes`→`Athens` (66×), `Lacédémoniens`→`Lacedaemonians`,
    `Stésimbrote`→`Stesimbrotus`, `Hermès`→`Hermes`, `Rhœsacès`→`Rhoesaces`, and ~20 more
  - `02-lucullus.md` (Roman): `Ptolémée`→`Ptolemy`, `Muréna`→`Murena`, `Séleucie`→`Seleucia`,
    `Mésopotamie`→`Mesopotamia`, `Gordyène`→`Gordyene`, and ~25 more
  - `03-comparison-cimon-lucullus.md`: `Orphée`→`Orpheus`, `Athènes`→`Athens`,
    `Léothychide`→`Leotychides`, `Hésiode`→`Hesiod`, `Homère`→`Homer`
  - `04-nicias.md` (Greek): `Athènes`→`Athens` (81×), `Lacédémoniens`→`Lacedaemonians`,
    `Cléon`→`Cleon` (16×), `Hermès`→`Hermes`, `Sphactérie`→`Sphacteria`, and ~35 more
  - `05-crassus.md` (Roman): `Suréna`→`Surena` (28×), `Hyrodès`→`Hyrodes` (16×),
    `Artavasdès`→`Artavasdes`, `Déjotarus`→`Deiotarus`, `Mésopotamie`→`Mesopotamia`, and ~20 more
  - `06-comparison-nicias-crassus.md`: minor fixes
  - `07-sertorius.md` (Roman): `Métellus`→`Metellus` (29×), `Antée`→`Antaeus`,
    `Pyrénées`→`Pyrenees`, `Gadès`→`Gades`, `Bétis`→`Baetis`, and ~15 more
  - `08-eumenes.md` (Greek): `Macédoine`→`Macedonia` (35×), `Cratère`→`Craterus` (22×),
    `Néoptolème`→`Neoptolemus` (17×), `Héphestion`→`Hephaestion`, `Cérès`→`Demeter`, and ~25 more
  - `09-comparison-sertorius-eumenes.md`: `Chersonèse`→`Chersonesus`, `Macédoine`→`Macedonia`
  - `10-agesilaus.md` (Greek): `Lacédémone`→`Lacedaemon` (60×), `Thébains`→`Thebans` (32×),
    `Xénophon`→`Xenophon` (11×), `Béotie`→`Boeotia` (9×), `Thèbes`→`Thebes`, and ~40 more
  - `11-pompey.md` (Roman): `Métellus`→`Metellus` (30×), `Cornélie`→`Cornelia` (14×),
    `Arménie`→`Armenia` (12×), `Cléopâtre`→`Cleopatra`, `Ptolémée`→`Ptolemy`, and ~50 more
  - `12-comparison-agesilaus-pompey.md`: `Sparte`→`Sparta`, `Thébains`→`Thebans`,
    `Lacédémoniens`→`Lacedaemonians`, `Léotychidas`→`Leotychidas`, `Lépidus`→`Lepidus`
  - `13-alexander.md` (Greek): `Macédonie`→`Macedonia` (91×), `Callisthène`→`Callisthenes` (27×),
    `Parménion`→`Parmenion` (25×), `Jupiter`→`Zeus` (12×), `Bacchus`→`Dionysus` (8×),
    `Hercule`→`Heracles` (4×), `Cléopâtre`→`Cleopatra`, `Héphestion`→`Hephaestion`, and ~80 more
  - `14-caesar.md` (Roman): `Pompéia`→`Pompeia` (7×), `Métellus`→`Metellus`,
    `Cléopâtre`→`Cleopatra`, `Scipion`→`Scipio` (16×), `Helvétiens`→`Helvetii`,
    `Idées de mars`→`Ides of March`, `Rhône`→`Rhone`, `Saône`→`Saone`, and ~40 more
  - `15-comparison-alexander-caesar.md`: no changes needed
  - `16-phocion.md` (Greek): `Athénien`→`Athenian` (83×), `Athènes`→`Athens` (35×),
    `Démade`→`Demades` (16×), `Pirée`→`Piraeus`, `Eubée`→`Euboea`, and ~60 more
  - `17-cato-the-younger.md` (Roman): `Métellus`→`Metellus` (26×), `Cépion`→`Caepio`,
    `Ptolémée`→`Ptolemy`, `Muréna`→`Murena`, `Stoïciens`→`Stoics`, and ~25 more
  - `18-comparison-phocion-cato.md`: no changes needed
  - `19-demosthenes.md` (Greek): `Athénien`→`Athenian` (34×), `Macédonie`→`Macedonia` (19×),
    `Démade`→`Demades` (11×), `Déméter`→`Demeter`, `Perséphone`→`Persephone`, and ~50 more
  - `20-cicero.md` (Roman): `Térentia`→`Terentia` (11×), `Verrès`→`Verres` (7×),
    `Céthégus`→`Cethegus` (7×), `Métellus`→`Metellus`, `Carnéade`→`Carneades`, and ~30 more
  - `21-comparison-demosthenes-cicero.md`: `Macédonie`→`Macedonia`, `Mécène`→`Maecenas`,
    `Anaximène`→`Anaximenes`, and ~10 more
  - `22-agis-cleomenes.md` (Greek): `Lacédémone`→`Lacedaemon` (56×), `Achéens`→`Achaeans` (54×),
    `Léonidas`→`Leonidas` (40×), `Junon`→`Hera` (4×), `Hercule`→`Heracles` (4×),
    `Sparte`→`Sparta` (76×), `Ptolémée`→`Ptolemy`, and ~80 more
  - `23-tiberius-gaius-gracchus.md` (Roman): `Cornélie`→`Cornelia` (11×),
    `Lélius`→`Laelius`, `Septimuléius`→`Septimuleius`, `Idées de mars`→`Ides of March`, and ~20 more
  - `24-comparison-agis-gracchus.md`: `Charilaüs`→`Charillus`, `Péloponnèse`→`Peloponnese`
  - `25-demetrius.md` (Greek): `Séleucus`→`Seleucus` (66×), `Athènes`→`Athens` (58×),
    `Ptolémée`→`Ptolemy` (41×), `Cérès`→`Demeter`, `Stratoclès`→`Stratocles`, and ~60 more
  - `26-antony.md` (Roman): `Cléopâtre`→`Cleopatra` (115×), `Lépidus`→`Lepidus` (22×),
    `Arménie`→`Armenia` (22×), `Mèdes`→`Medes` (12×), `Vénus`→`Venus`, and ~70 more
  - `27-comparison-demetrius-antony.md`: `Cléopâtre`→`Cleopatra`, `Athènes`→`Athens`, and ~5 more
  - `28-dion.md` (Greek): `Héraclide`→`Heraclides` (38×), `Athènes`→`Athens` (13×),
    `Gélon`→`Gelo`, `Timée`→`Timaeus`, `Cérès`→`Demeter`, and ~30 more
  - `29-brutus.md` (Roman): `Labéon`→`Labeo`, `Lénas`→`Lenas`, `Pataréens`→`Patareans`,
    `Trébonius`→`Trebonius`, `Lépidus`→`Lepidus`, and ~20 more
  - `30-comparison-dion-brutus.md`: no changes needed
  - `31-artaxerxes.md`: `Ctésias`→`Ctesias` (24×), `Cléarque`→`Clearchus` (20×),
    `Lacédémone`→`Lacedaemon` (16×), `Xénophon`→`Xenophon`, and ~30 more
  - `32-aratus.md` (Greek): `Achéens`→`Achaeans` (75×), `Macédonie`→`Macedonia` (23×),
    `Lysiadès`→`Lysiades` (13×), `Ptolémée`→`Ptolemy` (11×), `Sparte`→`Sparta`, and ~60 more
  - `33-galba.md` (Roman): `Néron`→`Nero` (61×), `Poppée`→`Poppaea` (8×),
    `Sénèque`→`Seneca`, `Suétone`→`Suetonius`, `Tibère`→`Tiberius`, and ~20 more
  - `34-otho.md` (Roman): `Cécina`→`Caecina` (15×), `Néron`→`Nero` (7×),
    `Bédriacum`→`Bedriacum`, `Mésie`→`Moesia`, `Crémone`→`Cremona`

## [v0.1.17] - 2026-06-19

### Changed
- Proper name normalization across all volume-2 files (17 files):

  **Deity names (Greek/Roman context rule applied)**
  - Greek lives: `Cérès`→`Demeter`, `Proserpine`→`Persephone`, `Vénus`→`Aphrodite`,
    `Apollon`→`Apollo`, `Bacchus`→`Dionysus`, `Hercules`→`Heracles`, `Mars`→`Ares`
  - Roman lives: `Vénus`→`Venus`, `Cérès`→`Ceres`, `Cybèle`→`Cybele`

  **Proper names (French → English/Latin/Greek) per file**
  - `04-pelopidas.md` (Greek): `Mélon`→`Melon`, `Tégyre`→`Tegyra`, `Thrasybule`→`Thrasybulus`,
    `Phœbidas`→`Phoebidas`, `Thessalie`→`Thessaly`, `Arcadie`→`Arcadia`, `Messénie`→`Messenia`,
    `Pharsale`→`Pharsalus`, `Mède`→`Mede`, `Iliade`→`Iliad`, `Orphée`→`Orpheus`,
    `Andromaque`→`Andromache`, `Thébé`→`Thebe`, `Phères`→`Pherae`, and ~25 more
  - `05-marcellus.md` (Roman): `Annibal`→`Hannibal` (40×), `Cornélius`→`Cornelius`,
    `Hiéron`→`Hiero`, `Hiéronymus`→`Hieronymus`, `Briarée`→`Briareus`,
    `Néapolis`→`Neapolis`, `Férétrien`→`Feretrian`, `Philoctète`→`Philoctetes`,
    `Vénuse`→`Venusia`, `Valère Maxime`→`Valerius Maximus`, and ~15 more
  - `06-comparison-pelopidas-marcellus.md`: `Tégyre`→`Tegyra`, `Cyropédie`→`Cyropaedia`
  - `07-aristides.md` (Greek): `Phalère`→`Phaleron`, `Cithéron`→`Cithaeron`,
    `Cratérus`→`Craterus`, `Panétius`→`Panaetius`, `Clisthène`→`Cleisthenes`,
    `Tisamène`→`Tisamenus`, `Boëdromion`→`Boedromion`, `Eucléia`→`Eucleia`, and ~15 more
  - `08-marcus-cato.md` (Roman): `Valérius`→`Valerius` (9×), `Achaïe`→`Achaea`,
    `Carnéade`→`Carneades`, `Démosthène`→`Demosthenes`, `Académie`→`Academy`,
    `Pyrénées`→`Pyrenees`, `Odyssée`→`Odyssey`, and ~10 more
  - `09-comparison-aristides-cato.md`: `Hérodote`→`Herodotus`, `Cynégire`→`Cynegirus`,
    `Hésiode`→`Hesiod`
  - `10-philopoemen.md` (Greek): `Mégalopolis`→`Megalopolis`, `Cléomène`→`Cleomenes`,
    `Dinocratès`→`Dinocrates`, `Mantinée`→`Mantinea`, `Diophanès`→`Diophanes`, and ~10 more
  - `11-flamininus.md` (Roman): `Cynoscéphales`→`Cynoscephalae`, `Alcée`→`Alcaeus`,
    `Héraclée`→`Heraclea`, `Magnésie`→`Magnesia`, `Eumène`→`Eumenes`, and ~12 more
  - `12-comparison-philopoemen-flamininus.md`: `Archédémos`→`Archedemus`
  - `13-pyrrhus.md` (Greek): `Cléonyme`→`Cleonymus`, `Gélon`→`Gelon`, `Lévinus`→`Laevinus`,
    `Déidamie`→`Deidameia`, `Bérénice`→`Berenice`, `Héraclée`→`Heraclea`,
    `Alcyonée`→`Alcyoneus`, `Bénévent`→`Beneventum`, and ~25 more
  - `14-marius.md` (Roman): `Métellus`→`Metellus` (38×), `Annibal`→`Hannibal`,
    `Pompéius`→`Pompeius`, `Rhône`→`Rhone`, `Bardiéens`→`Bardyaei`,
    `Aquœ Sextiœ`→`Aquae Sextiae`, `Orphée`→`Orpheus`, and ~30 more
  - `15-lysander.md` (Greek): `Chersonèse`→`Chersonesus`, `Léotychidas`→`Leotychidas`,
    `Théopompe`→`Theopompus`, `Théramène`→`Theramenes`, `Artaxerxès`→`Artaxerxes`,
    `Aphytée`→`Aphytaean`, `Silénus`→`Silenus`, `Athéna`→`Athena`, and ~20 more
  - `16-sulla.md` (Roman): `Métella`→`Metella` (10×), `Muréna`→`Murena` (6×),
    `Préneste`→`Praeneste` (5×), `Céramique`→`Ceramicus`, `Callisthène`→`Callisthenes`,
    `Tarpéienne`→`Tarpeian`, `Chaldée`→`Chaldea`, and ~25 more
  - `17-comparison-lysander-sulla.md`: `Philoclès`→`Philocles`, `Cléombrotus`→`Cleombrotus`

## [v0.1.16] - 2026-06-18

### Changed
- Proper name normalization across Themistocles, Camillus, Pericles and Fabius Maximus:

  **Deity names (Greek/Roman rule applied)**
  - `11-themistocles.md` (Greek): `Hercules`→`Heracles` (3×), `Bacchus`→`Dionysus` (2×),
    `Minerve`→`Athena` (2×), `Apollon Daphnéphore`→`Apollo Daphnephoros`
  - `12-camillus.md` (Roman): `Junon`→`Juno` (5×); `Heraclides` collateral damage fixed
  - `13-pericles.md` (Greek): `Minerve`→`Athena` (4×), `Junon`→`Hera`, `Diane`→`Artemis`,
    `Minerve Hygie`→`Athena Hygieia`

  **Proper names (French → English/Latin/Greek)**
  - `11-themistocles.md`: `Athénée`→`Athenaeus`, `Artémisium`→`Artemisium`,
    `Artémise`→`Artemisia`, `Ariamène`→`Ariamenes`, `Admète`→`Admetus`,
    `Magnésie`→`Magnesia`, `Simonide`→`Simonides`, `Léonidas`→`Leonidas`,
    `Néoclès`→`Neocles`, `Lycomèdes`→`Lycomedes`, `Néanthès`→`Neanthes`,
    `Amphictyonie`→`Amphictyony`, `Théopompe`→`Theopompus`,
    `Timocréon`→`Timocreon`, `Egine`→`Aegina`, `Mèdes`→`Medes`,
    `Magnésie`→`Magnesia`, `Épire`→`Epirus`, and ~25 more
  - `12-camillus.md`: `Cornélius Scipion`→`Cornelius Scipio`, `Mère Matuta`→`Mater Matuta`,
    `Tibre`→`Tiber` (3×), `Ardée`→`Ardea`, `Véies`→`Veii`, `Véiens`→`Veians`,
    `Lucrétius`→`Lucretius`, `Valérius`→`Valerius`, `Féries Latines`→`Feriae Latinae`,
    `Falèries`→`Falerii`, `Leucothée`→`Leucothea`, `Callisthène`→`Callisthenes`,
    `Préneste`→`Praeneste`, `Sénonais`→`Senones`, and ~15 more
  - `13-pericles.md`: `Aspasie`→`Aspasia` (9×), `Aréopage`→`Areopagus`,
    `Acropole`→`Acropolis`, `Éphialte`→`Ephialtes`, `Propylées`→`Propylaea`,
    `Parthénon`→`Parthenon`, `Clisthène`→`Cleisthenes`, `Potidée`→`Potidaea`,
    `Priène`→`Priene`, `Déméter`→`Demeter`, `Stésimbrote`→`Stesimbrotus`,
    `Mnésiclès`→`Mnesicles`, `Clazomène`→`Clazomenae`, and ~20 more
  - `14-fabius-maximus.md`: `Cornélius`→`Cornelius`, `Thrasymène`→`Trasimene`,
    `Trébie`→`Trebia`, `Ibérie`→`Iberia`, `Persée`→`Perseus`, `Rhégium`→`Rhegium`,
    `Faléries`→`Falerii`, `Lévinus`→`Laevinus`, and ~10 more

  **Scholarly attributions (xứ pattern)**
  - `Simonides xứ Ceos`, `Charon xứ Lampsacus`, `Neanthes xứ Cyzicus`
  - `Heraclides xứ Pontus`, `Corœbus xứ Xypete` (Pericles)

  **Terminology**
  - `archonte`→`archon` in Themistocles
  - `các bậc thầy của truyền thống`→`các thầy giáo của truyền thống`

## [v0.1.15] - 2026-06-18

### Changed
- Second round of fine translation corrections on Solon, Publicola and their comparison:

  **Terminology**
  - `tổng tài` → `quan chấp chính` throughout `09-publicola.md` and `10-comparison-solon-publicola.md` (~25 occurrences)
  - `archonte` → `archon` in `08-solon.md`

  **Proper name normalization**
  - `Tibre` → `Tiber` (river, body text and footnotes)
  - `Clinias` → `Cleinias` (correct Greek spelling)
  - `Heraclides of Pontus` → `Heraclides xứ Pontus`
  - `Dionysius of Halicarnassus` → `Dionysius xứ Halicarnassus` (footnotes)
  - `Daimachus of Plataea` → `Daimachus xứ Plataea`
  - `Eumenides` (was `Euménides`) in footnote

  **Vocabulary and style**
  - `nhận lấy [gia sản]` → `thừa hưởng`
  - `một lần nữa` → `một lần khác` (another occasion, not "once more")
  - `uy tín đã lớn lao` → `uy tín lớn lao` (remove redundant `đã` before adjective)
  - `hận thù triệt để` → `hận thù sâu sắc`
  - `bực bội` → `phiền thoái`
  - Long sentences split into two for readability

  **Footnotes**
  - Meta-words rendered in English: `imitateur`→`imitator`, `témoin`→`witness`
  - Chinese character (跛) replaced with Vietnamese text
  - Monetary conversion annotated with source date: `(tiền Pháp năm 1853)`
  - Footnote [^p9]: simplified wording

### Added
- PDF custom headers and footers via `scrlayer-scrpage` (`pdf-header.tex`)
- Auto-versioning: `set-version.py` pre-render script injects git tag into PDF footer

## [v0.1.14] - 2026-06-14

### Changed
- Fine translation corrections across 12 files based on translator's manual revisions:

  **Proper name normalization (French → Latin/English/Greek)**
  - `loi-gioi-thieu.md`: Antony and Cleopatra → Antony và Cleopatra
  - `volume-1/02-theseus.md`: Scythie→Scythia, Sénécion→Senecio, Pitthéus→Pittheus,
    Éthra→Aethra, Érechthée→Erechtheus, Hippolyte→Hippolytus, Phèdre→Phaedra,
    Pirithoüs→Pirithous, Hélène→Helen, Ménesthée→Menestheus, Aïdonéus→Aidoneus,
    Lycomède→Lycomedes, Pasiphaé→Pasiphaë, Apollon→Apollo, Vénus→Aphrodite,
    Dicéarque de Messène→Dicearchus xứ Messana, Dioclès de Péparèthe→Diocles xứ Peparethus
  - `volume-1/03-romulus.md`: Énée→Aeneas, Dioclès de Péparèthe→Diocles xứ Peparethus
  - `volume-1/05-lycurgus.md`: Timée→Timaeus, Créophyle→Creophylus
  - `volume-1/08-solon.md`: Crésus→Croesus, Junon→Hera, Timée→Timaeus,
    Aréopage→Areopagus, Atlantide→Atlantis, Épia→Aepeia, Thètes→Thetes,
    Pentacosiomédimnes→Pentacosiomedimnoi, Exécestide→Execestides
  - `volume-1/09-publicola.md`: Valérius→Valerius (30×), Valéria→Valeria (3×),
    Lucrèce→Lucretia (4×), Lucrétius→Lucretius (4×), Clélie→Cloelia,
    Scévola→Scaevola, Coclès→Cocles, Démarate→Demaratus, Véies→Veii (6×),
    Fidènes→Fidenae (3×), Vélia→Velia, Pentèle→Pentelicus, Épicharme→Epicharmus,
    Athénodore→Athenodorus, Anaximène→Anaximenes, Pluton→Pluto,
    Champs-de-Mars→Campus Martius, Denys d'Halicarnassus→Dionysius of Halicarnassus,
    calendes Mars→Calends of March
  - `volume-1/10-comparison-solon-publicola.md`: Mimnerme→Mimnermus,
    Daïmachus de Plataeas→Daimachus of Plataea, Strabon→Strabo

  **Vocabulary and style improvements (all affected files)**
  - `bậc thầy` → `thầy giáo` when referring to a person
  - `không mảy may quan trọng` → `không mấy quan trọng`
  - `những đức hạnh của mình` → `đức hạnh của mình`
  - `truyền thuyết được tin nhận nhất` → `truyền thuyết đáng tin nhất`
  - `các năm X đến Y` → `năm X đến năm Y` in date ranges
  - Sentence restructuring for better Vietnamese flow throughout

  **`loi-gioi-thieu.md`**
  - Header: `Tầm ảnh hưởng với nền văn minh châu Âu` → `Ảnh hưởng lên nền văn minh châu Âu`
  - Add birth years to Rousseau (1712–1778) and Montaigne (1533–1592) quotes

### Removed
- `PROJET-RESUME.md` (working note, not part of the publication)

## [v0.1.13] - 2026-06-02

### Fixed
- Upgrade `actions/checkout@v4` → `@v5` (Node.js 24) in CI workflow
- Add `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true` for remaining GitHub Actions
  to fix build failure due to Node.js 20 deprecation

## [v0.1.12] - 2026-06-02

### Added
- Add Volume 3 (34 chapters): Cimon, Lucullus, Nicias, Marcus Crassus, Sertorius,
  Eumenes, Agesilaus, Pompey, Alexander, Caesar, Phocion, Cato the Younger,
  Demosthenes, Cicero, Agis & Cleomenes, Tiberius & Gaius Gracchus, Demetrius,
  Antony, Dion, Brutus, Artaxerxes, Aratus, Galba, Otho and their comparisons

### Changed
- Rename all volume-3 files: underscores→hyphens, French names→English/Latin names
- Normalize all H2 chapter headings: `## XXVI — Antoine` → `## ANTONY` format
- Normalize all French proper names in body text and footnotes across 33 files —
  Eumène→Eumenes, Agésilas→Agesilaus, Pompée→Pompey, Alexandre→Alexander,
  César→Caesar, Cléomène→Cleomenes, Démosthène→Demosthenes, Cicéron→Cicero,
  Caïus→Gaius, Démétrius→Demetrius, Antoine→Antony, Artaxerxès→Artaxerxes,
  Othon→Otho, Tibérius→Tiberius, + all forms from volumes 1 & 2
- Remove French punctuation spacing (1 999 occurrences of ` ;` ` :` ` ?` ` !`)
- Fix footnote prefix collision: `cat` → `catu` (Cato the Younger vs Marcus Cato)
- Normalize footnote separators (`---`) across 31 files
- Add `volume-3/index.md` (Vietnamese, style matching volumes 1 & 2)
- Add volume-3 to `_quarto.yml` (34 chapters)
- Update README: Tập 3 marked as "đã xuất bản" with full chapter list

## [v0.1.11] - 2026-06-01

### Changed
- Fix "Đọc trên web" link in README to point to the Lời giới thiệu page instead
  of the Mục lục
- Update README Nội dung section: mark volumes 1 and 2 as "đã xuất bản" (published)
  and list all 6 pairs of volume 2

## [v0.1.10] - 2026-06-01

### Fixed
- Add missing 80 footnotes to `volume-1/11-themistocles.md` — the footnote
  definition section was entirely absent while the body text referenced
  `[^th1]`…`[^th80]`; all 80 notes translated from French into Vietnamese

## [v0.1.9] - 2026-06-01

### Fixed
- Normalize all French proper names in chapter headings (H2) across 22 files —
  THÉSÉE → THESEUS, PÉRICLÈS → PERICLES, ALCIBIADE → ALCIBIADES, TIMOLÉON → TIMOLEON, etc.
- Normalize all French proper names in body text and footnotes across 23 files —
  Alcibiade→Alcibiades, Aristide→Aristides, Coriolan→Coriolanus, Sylla→Sulla,
  Émilius→Aemilius, Lycurgue→Lycurgus, Périclès→Pericles, Milet→Miletus, Camille→Camillus
- Fix footnote prefix collisions between files: `mar` (marcellus→marc, marius→mariu),
  `cam` (comparison-aristides-cato: cam→cac), `comp` (pericles-fabius→compf,
  lysander-sulla→compls)

### Known gap
- `volume-1/11-themistocles.md` — 80 footnote references (`[^th1]`…`[^th80]`) in body
  text but the footnote definition section is entirely absent from the file

## [v0.1.8] - 2026-06-01

### Fixed
- Remove duplicate Phần V section and footnote set in `volume-1/12-camillus.md` —
  the file contained two complete copies; kept the more polished second version
- Normalize footnote separator (`---`) placement across 12 volume-1 files —
  separator now consistently appears before the first footnote definition,
  not after the last one

## [v0.1.7] - 2026-06-01

### Changed
- Remove French spacing before punctuation (`;`, `:`, `?`, `!`) across all 26 files
  in volumes 1 and 2 — Vietnamese does not use a space before these characters

### Reference
- Goatcounter analytics dashboard: https://plutarch-parallel-lives-vi.goatcounter.com/

## [v0.1.6] - 2026-06-01

### Added
- Add "Lời giới thiệu" page before the table of contents, introducing Plutarch,
  the Parallel Lives, its influence on European civilization, and famous readers

## [v0.1.5] - 2026-05-27

### Added
- Add Volume 2 (17 chapters): Timoleon, Aemilius Paullus, Pelopidas, Marcellus,
  Aristides, Marcus Cato, Philopoemen, Flamininus, Pyrrhus, Marius, Lysander, Sulla
  and their respective comparisons

### Changed
- Normalize all proper names and place names from French to English/Latin across volume 2
  - Main characters: Timoleon, Aemilius Paullus, Pelopidas, Philopoemen, Lysander,
    Sulla, Aristides, Gaius Marius
  - Other figures: Demetrius, Scipio, Dionysius, Perseus, Epaminondas, Archimedes,
    Archelaus, Agesilaus, Ptolemy, Cineas, Neoptolemus, Hicetas, Antiochus,
    Themistocles, Homer, Plutarch
  - Places: Athens, Lacedaemon, Macedonia, Corinth, Sicily, Thebes, Peloponnese,
    Plataea, Messene, Crete, Chaeronea, Salamis, Achaea, Phoenicia, Epirus
  - Adjectives: Theban, Lacedaemonian, Athenian, Cretan, Macedonian, Achaean
- Rename all volume-2 files: underscores→hyphens, French names→English/Latin names,
  INDEX.md→index.md (consistent with volume-1 convention)
- Fix structural issues: header corruption in Pyrrhus, Roman numeral prefixes in
  Lysander/Sulla/comparison headers, broken links in index
- Translate all French footnotes to Vietnamese (47 notes in Philopoemen and Flamininus)
- Enrich README with introduction to Plutarch, his influence on European civilization,
  and famous readers (Napoleon, Shakespeare, Rousseau, Montaigne, Emerson, Washington)

## [v0.1.4] - 2026-05-27

### Changed
- Normalize all proper names and place names from French to English/Latin across volume 1
  - Characters: Theseus, Remus, Themistocles, Pericles, Alcibiades, Coriolanus, Camillus, Lycurgus, Hercules, Socrates, Plato, Aristotle, Herodotus, Thucydides, Homer, Caesar, Cicero, Pompey, and ~40 more
  - Places: Athens, Sparta, Lacedaemon, Corinth, Thebes, Delphi, Olympia, Crete, Troy, Peloponnese, Macedonia, Egypt, Sicily, Etruria, Lydia, Ephesus, Miletus, Salamis, Megara, and more
  - Adjectives: Spartan, Lacedaemonian, Theban, Olympic, Milesian

## [v0.1.3] - 2026-05-28

### Added
- Fix Greek letter rendering in PDF via Noto Serif

## [v0.1.2] - 2026-05-28

### Added
- Update footnotes

## [v0.1.1] - 2026-05-27

### Added
- Update index.md of volume 1

## [v0.1.0] - 2026-05-26

### Added
- First publication of Volume 1 (19 chapters)
- HTML, PDF, and EPUB formats
- Goatcounter analytics