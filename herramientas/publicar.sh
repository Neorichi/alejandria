#!/bin/bash
# Publishes Alejandría to github.com/Neorichi/alejandria:
#  1. the Markdown in batches of ~400 MB (GitHub refuses pushes over 2 GB), with README and these scripts;
#  2. a release v<version> with the compiled packs (.sqlite, each under 2 GiB);
#  3. manifest.json last, so the app never sees a version whose files are not up yet.
# Uso: tools/enciclopedia/publicar.sh PACK [PACK…]   (the packs compiled in the last compilar.py run)
set -eu
E=/Volumes/Disk1TB/nesi-pocket/enciclopedia
R=$E/alejandria
cd "$R"
V=$(python3 -c "import json,sys; m=json.load(open('manifest.json')); print({p['id']:p['version'] for p in m['packs']}[sys.argv[1]])" "$1")
mkdir -p herramientas
cp /Volumes/Disk1TB/nesi-pocket/tools/enciclopedia/*.py /Volumes/Disk1TB/nesi-pocket/tools/enciclopedia/publicar.sh herramientas/
git add README.md herramientas .gitignore 2>/dev/null || git add README.md herramientas
git commit -q -m "Herramientas y README ($V)" || true
git push -q origin HEAD:main
# Markdown in batches: removed files first, then new/changed ones 100 files (~400 MB) at a time.
git add -u md
git diff --cached --quiet || { git commit -q -m "Markdown $V: ficheros quitados o cambiados"; git push -q origin HEAD:main; }
batch=0
git ls-files --others --exclude-standard md | split -l 100 - /tmp/alejandria-lote-
for f in /tmp/alejandria-lote-*; do
  batch=$((batch + 1))
  xargs git add < "$f"
  git commit -q -m "Markdown $V (lote $batch)"
  git push -q origin HEAD:main
  echo "lote $batch subido"
  rm -f "$f"
done
assets=()
for p in "$@"; do assets+=("$E/paquetes/$p.sqlite"); done
if gh release view "v$V" -R Neorichi/alejandria >/dev/null 2>&1; then
  gh release upload "v$V" "${assets[@]}" --clobber -R Neorichi/alejandria
else
  gh release create "v$V" "${assets[@]}" -R Neorichi/alejandria --title "Alejandría $V" \
    --notes "Paquetes compilados (SQLite FTS5, texto comprimido) de: $*. Los Markdown fuente están en md/."
fi
git add manifest.json
git commit -q -m "Versión $V: $*" || true
git push -q origin HEAD:main
echo "publicado v$V: $*"
