#!/bin/bash
# Publishes Alejandría to github.com/Neorichi/alejandria (run after compilar.py):
#  1. README, these scripts and the OKF bundle md/ (deleted files first, then the rest in batches of ~400 MB:
#     GitHub refuses pushes over 2 GB);
#  2. a release v<version> with what compilar.py made in that version: packs (.sqlite, each under 2 GiB) and
#     OKF archives (.okf.tar.gz);
#  3. manifest.json last, so the app never sees a version whose files are not up yet.
# Uso: tools/enciclopedia/publicar.sh
set -eu
E=/Volumes/Disk1TB/nesi-pocket/enciclopedia
R=$E/alejandria
V=$(cat "$E/paquetes/ultima-version")
cd "$R"
mkdir -p herramientas
cp /Volumes/Disk1TB/nesi-pocket/tools/enciclopedia/*.py /Volumes/Disk1TB/nesi-pocket/tools/enciclopedia/publicar.sh herramientas/
git add -A README.md herramientas
git commit -q -m "Herramientas y README ($V)" || true
git push -q origin HEAD:main
git ls-files -d md | xargs git rm -q --cached --ignore-unmatch
git diff --cached --quiet || { git commit -q -m "Alejandría $V: ficheros quitados"; git push -q origin HEAD:main; }
rm -f /tmp/alejandria-lote-*
{ git ls-files -m md; git ls-files --others --exclude-standard md; } |
  python3 -c "
import os, sys
n, size, out = 0, 0, None
for p in sys.stdin.read().splitlines():
    if out is None or size > 400_000_000:
        n += 1; size = 0; out = open(f'/tmp/alejandria-lote-{n:03d}', 'w')
    out.write(p + '\n'); size += os.path.getsize(p)
"
batch=0
for f in /tmp/alejandria-lote-*; do
  [ -e "$f" ] || continue   # nothing changed: the glob stays literal
  batch=$((batch + 1))
  tr '\n' '\0' < "$f" | xargs -0 git add
  git commit -q -m "Alejandría $V (lote $batch)"
  git push -q origin HEAD:main
  echo "lote $batch subido"
  rm -f "$f"
done
assets=()
while IFS= read -r a; do assets+=("$a"); done < <(python3 - "$V" "$E/paquetes" <<'EOF'
import json, sys
v, paq = sys.argv[1], sys.argv[2]
for p in json.load(open("manifest.json"))["packs"]:
    for key, name in (("url", f"{p['id']}.sqlite"), ("okf", f"{p['id']}.okf.tar.gz")):
        if f"/v{v}/" in p.get(key, ""):
            print(f"{paq}/{name}")
EOF
)
if [ ${#assets[@]} -gt 0 ]; then
  if gh release view "v$V" -R Neorichi/alejandria >/dev/null 2>&1; then
    gh release upload "v$V" "${assets[@]}" --clobber -R Neorichi/alejandria
  else
    gh release create "v$V" "${assets[@]}" -R Neorichi/alejandria --title "Alejandría $V" \
      --notes "Paquetes compilados (SQLite FTS5, texto comprimido) y archivos OKF (.okf.tar.gz) de esta versión. El bundle OKF está en md/."
  fi
fi
git add manifest.json md/index.md md/log.md
git commit -q -m "Versión $V" || true
git push -q origin HEAD:main
echo "publicado v$V: ${assets[*]:-sin ficheros nuevos}"
