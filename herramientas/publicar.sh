#!/bin/bash
# Publishes Alejandría: the Markdown, manifest.json, README and these scripts to github.com/Neorichi/alejandria,
# then a GitHub release v<version> with the compiled packs (a release needs a commit first).
# Uso: tools/enciclopedia/publicar.sh PACK [PACK…]   (the packs compiled in the last compilar.py run)
set -eu
E=/Volumes/Disk1TB/nesi-pocket/enciclopedia
R=$E/alejandria
cd "$R"
V=$(python3 -c "import json,sys; m=json.load(open('manifest.json')); print({p['id']:p['version'] for p in m['packs']}[sys.argv[1]])" "$1")
assets=()
for p in "$@"; do assets+=("$E/paquetes/$p.sqlite"); done
mkdir -p herramientas
cp /Volumes/Disk1TB/nesi-pocket/tools/enciclopedia/*.py /Volumes/Disk1TB/nesi-pocket/tools/enciclopedia/publicar.sh herramientas/
git add -A
git commit -q -m "Versión $V: $*" || true
git push -q origin HEAD:main
if gh release view "v$V" -R Neorichi/alejandria >/dev/null 2>&1; then
  gh release upload "v$V" "${assets[@]}" --clobber -R Neorichi/alejandria
else
  gh release create "v$V" "${assets[@]}" -R Neorichi/alejandria --title "Alejandría $V" \
    --notes "Paquetes compilados (SQLite FTS5) de: $*. Los Markdown fuente están en md/ con el mismo commit."
fi
echo "publicado v$V: $*"
