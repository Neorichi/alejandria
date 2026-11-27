# Alejandría

Una enciclopedia en **Markdown** para usar **sin internet**. La usa [NesiPocket](https://huggingface.co/nesilabs/nesi-nano-GGUF), la app que ejecuta nesi-nano en el iPhone: el modelo busca aquí antes que en internet.

## Cómo está hecho

- **`md/`**: la fuente, en Markdown. Cada fichero lleva varios artículos, y cada artículo empieza con unas líneas de metadatos (`id`, `titulo`, `fuente`, `licencia`, `url`) y sigue con `# Título` y el texto.
- **Releases**: los mismos artículos compilados en **SQLite con índice de texto completo** (FTS5, ranking BM25, sin acentos). Es lo que descarga el iPhone; son demasiado grandes para git.
- **`manifest.json`**: la versión, el tamaño, la huella SHA-256 y el enlace de descarga de cada paquete. La app lo mira al abrirse para saber si tiene la última versión.
- **`herramientas/`**: los scripts que convierten las fuentes a Markdown (`seguridad.py`, `medicina.py`, `wikipedia.py`), compilan los paquetes (`compilar.py`) y los publican (`publicar.sh`).

## Paquetes

| Paquete | Contenido |
|---|---|
| `seguridad` | Vulnerabilidades explotadas (CISA KEV), técnicas, grupos y software de ataque (MITRE ATT&CK), tipos de fallo (MITRE CWE) y artículos de seguridad informática de Wikipedia. |
| `medicina` | Temas de salud de MedlinePlus en español (NLM) y artículos de medicina de Wikipedia. **No sustituye a un médico.** |
| `wikipedia-resumida` | El principio de cada artículo de la Wikipedia en español, con los datos de su ficha. |

## Licencias y fuentes

Cada artículo indica su fuente y su licencia.

- **Wikipedia:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Autores: los editores de Wikipedia; enlace al original en el campo `url`. Los textos se han convertido a Markdown y recortado. Los paquetes que la contienen se distribuyen con la misma licencia.
- **MedlinePlus** (Biblioteca Nacional de Medicina de EE. UU.): resúmenes de los temas de salud.
- **CISA KEV:** dominio público (Gobierno de EE. UU.).
- **MITRE ATT&CK® y CWE™:** © The MITRE Corporation, reproducido y distribuido con su permiso según sus condiciones de uso.
