# Résumé du projet — Plutarch Parallel Lives VI (Vietnamien)

Ce document résume l'ensemble des travaux réalisés sur ce projet et peut servir
de guide ou de prompt de démarrage pour un projet similaire (autre livre, autre langue).

---

## 1. Contexte et objectif

**Projet :** Traduction vietnamienne de *Những cuộc đời song hành* (Les Vies parallèles
de Plutarque), publiée en deux tomes (36 chapitres + comparaisons).

**Traductrice :** Hằng Lãm

**Outil de publication :** [Quarto](https://quarto.org/) — génère HTML (GitHub Pages),
PDF (XeLaTeX) et EPUB depuis des fichiers Markdown.

**Dépôt :** GitHub — CI/CD via GitHub Actions, hébergement via GitHub Pages.

**Analytique :** Goatcounter (cookieless, sans tracking) :
`https://plutarch-parallel-lives-vi.goatcounter.com/`

---

## 2. Structure du projet

```
plutarch-parallel-lives-vi/
├── _quarto.yml              # Configuration Quarto (chapitres, formats, thème)
├── index.md                 # Mục lục (table des matières)
├── loi-gioi-thieu.md        # Page d'introduction (avant le Mục lục)
├── analytics.html           # Snippet Goatcounter injecté dans le HTML
├── CHANGELOG.md             # Historique des versions
├── README.md                # Présentation du projet sur GitHub
├── .github/
│   └── workflows/
│       └── publish.yml      # CI/CD : build + deploy HTML + release PDF/EPUB
├── volume-1/
│   ├── index.md             # Sommaire du tome 1
│   ├── 01-essay-on-plutarch.md
│   ├── 02-theseus.md
│   ├── ...                  # 18 fichiers numérotés
│   └── 18-comparison-alcibiades-coriolanus.md
└── volume-2/
    ├── index.md             # Sommaire du tome 2
    ├── 01-timoleon.md
    ├── ...                  # 17 fichiers numérotés
    └── 17-comparison-lysander-sulla.md
```

---

## 3. Configuration Quarto (`_quarto.yml`)

```yaml
project:
  type: book
  output-dir: _book

book:
  title: "Những cuộc đời song hành"
  subtitle: "Plutarch — Tiểu sử các vĩ nhân Hy Lạp và La Mã"
  author: "Plutarch"
  date: today
  language: vi
  output-file: "nhung-cuoc-doi-song-hanh"

  chapters:
    - loi-gioi-thieu.md       # Page d'introduction (avant le mục lục)
    - index.md                # Table des matières globale
    - part: "volume-1/index.md"
      chapters:
        - volume-1/01-essay-on-plutarch.md
        - volume-1/02-theseus.md
        # ...
    - part: "volume-2/index.md"
      chapters:
        - volume-2/01-timoleon.md
        # ...

  search: true
  sidebar:
    style: docked
    collapse-level: 1

lang: vi

format:
  html:
    theme: cosmo
    toc: true
    toc-depth: 2
    fontsize: 1.05em
    linestretch: 1.6
    include-in-header: analytics.html
  pdf:
    documentclass: scrbook
    pdf-engine: xelatex
    mainfont: "Noto Serif"
    sansfont: "Noto Sans"
    monofont: "Noto Sans Mono"
    fontsize: 11pt
    linestretch: 1.4
    geometry:
      - margin=2.5cm
    toc: true
    toc-depth: 2
  epub:
    toc: true
    toc-depth: 2
```

**Points clés :**
- `documentclass: scrbook` pour PDF de qualité livre (KOMA-Script)
- `pdf-engine: xelatex` obligatoire pour les polices Unicode/vietnamiennes
- Polices Noto pour la compatibilité vietnamienne et grecque en PDF
- `include-in-header: analytics.html` pour injecter Goatcounter dans chaque page HTML

---

## 4. CI/CD — GitHub Actions (`.github/workflows/publish.yml`)

```yaml
name: Render and publish

on:
  push:
    branches: [main]
    tags: ['v*']
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - uses: actions/checkout@v4
      - uses: quarto-dev/quarto-actions/setup@v2
        with:
          tinytex: true
      - name: Install Vietnamese-friendly fonts
        run: |
          sudo apt-get update
          sudo apt-get install -y fonts-noto-core fonts-noto-cjk
      - run: quarto render
      - name: Publish HTML to GitHub Pages
        if: github.event_name == 'push' && github.ref == 'refs/heads/main'
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_book
          publish_branch: gh-pages
      - name: Create Release with PDF and EPUB
        if: startsWith(github.ref, 'refs/tags/v')
        uses: softprops/action-gh-release@v2
        with:
          files: |
            _book/*.pdf
            _book/*.epub
          generate_release_notes: true
```

**Comportement :**
- Tout push sur `main` → rebuild HTML et déploiement sur GitHub Pages
- Tout tag `v*` → rebuild + création d'une release GitHub avec PDF et EPUB en pièces jointes

**Créer un tag et déclencher une release :**
```bash
git tag -a v0.1.8 -m "v0.1.8 — Description courte"
git push origin v0.1.8
```

---

## 5. Format des fichiers Markdown

### Structure d'un chapitre

```markdown
# Tên nhân vật

## Giới thiệu (optionnel)

Texte d'introduction...

### Phần I — Titre de la section

Contenu...

### Phần II — ...

---

[^fn1]: Texte de la note de bas de page 1.
[^fn2]: Texte de la note de bas de page 2.
```

### Règles de format (conventions établies)

1. **Séparateur des notes de bas de page :** `---` placé *avant* la première
   définition `[^...]`, jamais après la dernière. Aucun `---` en fin de fichier.

2. **Nommage des notes :** préfixe par personnage (`cam1`, `cam2`... pour Camillus ;
   `the1`, `the2`... pour Theseus, etc.) — évite les conflits entre fichiers.

3. **Références inline :** `[^cam1]` dans le corps du texte.

4. **En-têtes de sections :** `### Phần I — Titre` (numérotation romaine vietnamienne).

5. **Nommage des fichiers :** `NN-nom-latin.md` (ex: `02-theseus.md`, `12-camillus.md`),
   tirets à la place des espaces ou underscores, noms en latin/anglais (pas français).

6. **Fichiers de comparaison :** `NN-comparison-nom1-nom2.md`.

---

## 6. Règles typographiques vietnamiennes

Le vietnamien n'utilise **pas d'espace avant** les signes de ponctuation `;`, `:`, `?`, `!`
(contrairement au français qui utilise une espace fine ou normale).

**Correction en batch :**
```bash
find volume-1 volume-2 -name "*.md" -exec sed -i '' \
  's/ ;/;/g; s/ :/:/g; s/ ?/?/g; s/ !/!/g' {} \;
```

**Vérification :**
```bash
grep -rn ' [;:?!]' volume-1/ volume-2/
```

---

## 7. Analytique Goatcounter

Fichier `analytics.html` à la racine :
```html
<script data-goatcounter="https://MON-PROJET.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
```

Référencé dans `_quarto.yml` :
```yaml
format:
  html:
    include-in-header: analytics.html
```

Créer un compte gratuit sur [goatcounter.com](https://www.goatcounter.com/),
choisir un code de site, et remplacer `MON-PROJET` par ce code.

---

## 8. Page d'introduction (`loi-gioi-thieu.md`)

Placée en premier dans `chapters:` de `_quarto.yml`, avant `index.md`.
Contient :
- Biographie de l'auteur
- Présentation de l'œuvre
- Influence sur la civilisation (Renaissance, Shakespeare, Révolutions)
- Lecteurs célèbres (citations de Rousseau, Montaigne, Napoleon, Emerson, Washington)
- Présentation de la traduction

Ce modèle est réutilisable pour tout projet de traduction littéraire.

---

## 9. Workflow Git et versioning

### Convention de versioning

`v0.MAJEUR.MINEUR` — pas encore en v1.x (œuvre incomplète, travail en cours).

| Version | Contenu |
|---------|---------|
| v0.1.0  | Première publication du Tome 1 (19 chapitres) |
| v0.1.1–v0.1.3 | Corrections index, notes, polices PDF |
| v0.1.4  | Normalisation noms propres Tome 1 (français → latin/anglais) |
| v0.1.5  | Ajout Tome 2 (17 chapitres), normalisation noms propres Tome 2, traduction notes françaises |
| v0.1.6  | Page "Lời giới thiệu" ajoutée avant le Mục lục |
| v0.1.7  | Suppression espaces devant ponctuation (`;:?!`) sur 26 fichiers |
| v0.1.8  | Correction doublon Camillus, uniformisation séparateurs notes |

### Commandes courantes

```bash
# Voir l'état
git status
git log --oneline

# Commit + push
git add fichier1.md fichier2.md
git commit -m "Description courte"
git push

# Créer et pousser un tag (déclenche release PDF/EPUB)
git tag -a v0.X.Y -m "v0.X.Y — Description"
git push origin v0.X.Y
```

---

## 10. Corrections réalisées — recettes réutilisables

### Correction d'une section dupliquée (Python)

Lorsqu'un fichier contient deux copies d'une même section, identifier les deux
en-têtes et supprimer la première version (moins complète) :

```python
with open('fichier.md', 'r') as f:
    content = f.read()

first  = '### Phần V — Titre version 1'
second = '### Phần V — Titre version 2'

i1 = content.find(first)
i2 = content.find(second)

# Garde tout avant la première version, puis tout à partir de la seconde
new_content = content[:i1] + content[i2:]

with open('fichier.md', 'w') as f:
    f.write(new_content)
```

### Normalisation des séparateurs de notes (Python)

```python
import os, re

def fix_footnote_separator(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')

    # Trouver première et dernière note
    fn_lines = [i for i, l in enumerate(lines) if re.match(r'^\[\^', l)]
    if not fn_lines:
        return

    first_fn = fn_lines[0]
    last_fn  = fn_lines[-1]

    # Supprimer le --- trailing après la dernière note
    while lines and lines[-1].strip() in ('---', ''):
        if lines[-1].strip() == '---':
            lines.pop()
            break
        lines.pop()

    # Recalculer après suppression
    fn_lines2 = [i for i, l in enumerate(lines) if re.match(r'^\[\^', l)]
    if not fn_lines2:
        return
    first_fn2 = fn_lines2[0]

    # Vérifier si --- est déjà présent avant la première note
    has_sep = any(lines[j].strip() == '---'
                  for j in range(max(0, first_fn2-3), first_fn2))

    if not has_sep:
        lines.insert(first_fn2, '')
        lines.insert(first_fn2, '---')

    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))

for root, _, files in os.walk('.'):
    for fn in sorted(files):
        if fn.endswith('.md') and fn != 'index.md':
            fix_footnote_separator(os.path.join(root, fn))
```

### Vérification du format notes (Python)

```python
import os, re

problems = []
for root, _, files in os.walk('.'):
    for fn in sorted(files):
        if not fn.endswith('.md') or fn == 'index.md':
            continue
        path = os.path.join(root, fn)
        with open(path) as f:
            lines = f.readlines()
        fn_lines = [i for i, l in enumerate(lines) if re.match(r'^\[\^', l)]
        if not fn_lines:
            continue
        first_fn = fn_lines[0]
        last_fn  = fn_lines[-1]
        has_sep_before = any(lines[j].strip() == '---'
                             for j in range(max(0, first_fn-3), first_fn))
        has_trailing   = any(l.strip() == '---'
                             for l in lines[last_fn+1:])
        if not has_sep_before or has_trailing:
            problems.append(f"{path}: sep_before={'OK' if has_sep_before else 'MISSING'} | "
                            f"{'TRAILING_SEP' if has_trailing else 'OK'}")

if problems:
    for p in problems:
        print(p)
else:
    print("Verification done. 0 problems.")
```

---

## 11. Checklist pour un nouveau projet de livre

### Initialisation

- [ ] Créer le dépôt GitHub (public ou privé)
- [ ] Initialiser `_quarto.yml` (adapter titre, auteur, langue, `output-file`)
- [ ] Créer `analytics.html` avec le code Goatcounter du projet
- [ ] Créer `.github/workflows/publish.yml` (copier le modèle ci-dessus)
- [ ] Créer `.gitignore` (exclure `_book/`, `.quarto/`, `*.tex`, `*.log`, `.DS_Store`)
- [ ] Activer GitHub Pages sur la branche `gh-pages` (Settings → Pages)
- [ ] Créer un compte Goatcounter et noter l'URL du tableau de bord

### Structure des fichiers

- [ ] `loi-gioi-thieu.md` (ou équivalent) — page d'introduction avant le mục lục
- [ ] `index.md` — table des matières
- [ ] `volume-N/index.md` — sommaire de chaque tome
- [ ] Chapitres nommés `NN-nom-latin.md` avec numérotation à deux chiffres

### Qualité du contenu

- [ ] Noms propres normalisés (pas de formes françaises si texte en vietnamien)
- [ ] Pas d'espace avant `;`, `:`, `?`, `!`
- [ ] Notes de bas de page avec préfixe unique par fichier (`nom_abrege + numéro`)
- [ ] Séparateur `---` avant la première note, rien après la dernière
- [ ] Notes françaises dans la source originale → traduites en vietnamien

### Versioning

- [ ] `CHANGELOG.md` tenu à jour à chaque version
- [ ] Tags annotés `v0.X.Y` pour chaque release significative
- [ ] Premier tag `v0.1.0` après publication initiale

---

## 12. Prompt de démarrage pour un nouveau projet

> Je travaille sur un livre traduit en vietnamien, publié avec Quarto en HTML/PDF/EPUB
> et déployé sur GitHub Pages via GitHub Actions. Le projet suit la même architecture
> que *plutarch-parallel-lives-vi* : fichiers Markdown par chapitre, séparés par tome,
> avec notes de bas de page préfixées, séparateur `---` avant les notes, Goatcounter
> pour l'analytique, et tags Git pour déclencher les releases PDF/EPUB.
>
> Les conventions à respecter :
> - Nommage fichiers : `NN-nom-latin.md`
> - Ponctuation vietnamienne : pas d'espace avant `;`, `:`, `?`, `!`
> - Format notes : `[^prefNN]:` en fin de fichier, séparé du corps par `---`
> - Polices PDF : Noto Serif / Noto Sans via XeLaTeX
> - CI/CD : `.github/workflows/publish.yml` avec `quarto render` + `peaceiris/actions-gh-pages`
>
> [Décrire ici le contenu spécifique du nouveau livre, l'état actuel des fichiers,
> et les tâches à réaliser.]
