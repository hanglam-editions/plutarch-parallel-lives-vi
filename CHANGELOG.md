# Changelog

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