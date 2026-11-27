# Alejandría

Una enciclopedia en **Markdown** para usar **sin internet**. La usa [NesiPocket](https://huggingface.co/nesilabs/nesi-nano-GGUF), la app que ejecuta nesi-nano en el iPhone: el modelo busca aquí antes que en internet.

Está en formato **[OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)** (Open Knowledge Format), así que cualquier agente o herramienta que entienda OKF puede usarla tal cual.

## Cómo está hecho

- **`md/`** es un *bundle* OKF: **un fichero Markdown por concepto**, con metadatos YAML arriba y el texto debajo.
  - Metadatos: `type` (por ejemplo «Vulnerabilidad explotada», «Técnica de ataque», «Tema de salud» o «Artículo de enciclopedia»), `title`, `description`, `resource` (el original), `tags`, `sources` (de dónde sale y cuándo cambió la fuente), `license`, `generated` (cuándo se escribió), `status` y `stale_after` (a partir de cuándo hay que darlo por viejo: 30 días en las vulnerabilidades, un año en la Wikipedia).
  - Los conceptos se enlazan con enlaces Markdown normales: una vulnerabilidad con su tipo de fallo (CWE), un grupo de ataque con las técnicas y el software que usa, una técnica con sus mitigaciones, un tema de salud con los temas relacionados.
  - Cada carpeta tiene un `index.md` con lo que hay dentro y su descripción. `md/index.md` declara la versión de OKF y `md/log.md` guarda los cambios.
- **La Wikipedia resumida** son dos millones de conceptos: demasiados ficheros para git. Va en la release como `wikipedia-resumida.okf.tar.gz`, con las mismas rutas: se descomprime dentro de `md/`.
- **Releases**: los mismos conceptos compilados en **SQLite con índice de texto completo** (FTS5, ranking BM25, sin acentos). Es lo que descarga el iPhone; son demasiado grandes para git.
- **`manifest.json`**: la versión, el tamaño, la huella SHA-256 y el enlace de descarga de cada paquete (y de su archivo OKF). La app lo mira al abrirse para saber si tiene la última versión.
- **`herramientas/`**: los scripts que convierten las fuentes a OKF (`seguridad.py`, `medicina.py`, `wikipedia.py`, con `comun.py`), compilan los paquetes (`compilar.py`) y los publican (`publicar.sh`).

## Paquetes

| Paquete | Contenido |
|---|---|
| `seguridad` | Vulnerabilidades explotadas (CISA KEV), técnicas, grupos, software, mitigaciones y campañas de ataque (MITRE ATT&CK), tipos de fallo (MITRE CWE) y artículos de seguridad informática de Wikipedia. |
| `medicina` | Temas de salud de MedlinePlus en español (NLM) y artículos de medicina de Wikipedia. **No sustituye a un médico.** |
| `wikipedia-resumida` | El principio de cada artículo de la Wikipedia en español, con los datos de su ficha. |

## Licencias y fuentes

Cada concepto indica su fuente (`sources`) y su licencia (`license`).

- **Wikipedia:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Autores: los editores de Wikipedia; enlace al original en `resource`. Los textos se han convertido a Markdown y recortado. Los paquetes que la contienen se distribuyen con la misma licencia.
- **MedlinePlus** (Biblioteca Nacional de Medicina de EE. UU.): resúmenes de los temas de salud.
- **CISA KEV:** dominio público (Gobierno de EE. UU.).
- **MITRE ATT&CK® y CWE™:** © The MITRE Corporation, reproducido y distribuido con su permiso según sus condiciones de uso.
