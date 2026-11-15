# Ambiente de trabajo · Canal de YouTube de fútbol histórico

Documento de referencia con toda la información reunida hasta ahora. No es una lista de tareas: es la base de conocimiento para organizar el ambiente de trabajo cuando se quiera.

Última actualización: 2026-11-15.

---

## 1. Qué se quiere construir
- Un canal de YouTube sobre **fútbol histórico español** (Primera y Segunda División), alimentado por los datos del repo `luyspilo/futbol-historico`.
- **Formatos:** todos (Shorts, rankings, efemérides, vídeos largos).
- **Voz:** la del propio usuario, clonada en ElevenLabs, en español.
- **Modo de trabajo:** el usuario revisa cada vídeo primero. Cuando el flujo esté probado y se sepa cómo trabaja, se automatiza (incluida la subida).
- **Meta de fondo:** construir un ecosistema de automatización bien montado, empezando por la base y reorganizándolo después.

## 2. Qué hay en el repo
Repo: `luyspilo/futbol-historico` · rama de trabajo: `claude/youtube-channel-automation-9s6ams` (todo subido; no hay pull request).

| Ruta | Qué es |
|---|---|
| `index.html` | Web estática de estadísticas del fútbol español. |
| `data/primera-pichichi.json` | Pichichi de Primera: 102 filas, temporadas 1928/29 a 2025/26 (campos: temporada, persona, club, goles, partidos). Fuente: RSSSF. |
| `data/primera-zamora.json` | Trofeo Zamora, cobertura **parcial** (estado "partial"). Campos: temporada, portero, club, coeficiente, goles encajados, partidos. |
| `data/app.js` | Código que pinta las tablas de Pichichi y Zamora en la web. |
| `tools/short_pichichi.py` | Genera un Short vertical a partir del JSON del Pichichi. |
| `guiones/001-pichichi-short.md` | Guion, título y descripción del Short 001. |
| `out/locucion.mp3` | Locución de ElevenLabs del Short 001. |
| `out/short-pichichi.mp4` | Vídeo final del Short 001 (con audio). |
| `docs/CONTEXTO.md` | Este documento. |
| `docs/referencias-videos.md` | Transcripciones de los 4 vídeos de terceros analizados. |

### Datos útiles ya calculados (Pichichi)
- Más títulos: Messi 8, Telmo Zarra 6, Alfredo Di Stéfano 5, Quini 5, Hugo Sánchez 5, Ferenc Puskás 4.
- Récord de goles en una temporada: **50**, Messi, FC Barcelona, 2011/12 (37 partidos).
- Otros máximos: Cristiano Ronaldo 48 (2014/15), Messi 46 (2012/13), Cristiano 40 (2010/11), Luis Suárez 40 (2015/16), Zarra 38 (1950/51, 30 partidos).
- Clubes con más Pichichis: Real Madrid 30, FC Barcelona 20, Athletic Bilbao 12, Atlético de Madrid 10, Valencia CF 6.
- Las temporadas con empate conservan varias filas, así que "títulos" cuenta filas por persona.

## 3. Pipeline de vídeo (estado actual)
**Flujo:** datos (JSON) → guion → voz (ElevenLabs) → gráficos y montaje → revisión del usuario → (futuro) subida a YouTube.

### 3.1 Guion y voz
- Guion del Short 001: `guiones/001-pichichi-short.md` (~29 s). Los años y cifras se escriben **en palabras** ("mil novecientos cincuenta, cincuenta y uno") para que la voz los lea bien. Hay que comprobar que se pronuncian bien.
- Voz: ElevenLabs **"Luis CLICK"** (clonada), `voice_id` `F2AZuQ11KpWHmLfhVFT5`.
- Modelo: `eleven_v3`. Una sola toma (`generations_count` 1). Coste de la toma del Short 001: **474 créditos** (~9,5 céntimos de USD según la herramienta).
- Flow de ElevenLabs con la toma: `PqenIbkCFlxSe01Ow9fP`. El enlace de descarga del audio es firmado y **caduca**; el audio ya está guardado en `out/locucion.mp3`.
- Otras voces en español vistas en el workspace (por si se quiere comparar): Bosco (peninsular, meditativa), Rafa N (peninsular, conversacional), Sara Martin (femenina, peninsular, educativa), Julián (peninsular, narrador cálido), Marcos (andaluz), Leandro, Edinson, Mario, Elias, entre otras. Hay más en la lista, que estaba paginada.
- Importante: **no repetir una generación** para "reintentar"; cobra otra vez.

### 3.2 Montaje (`tools/short_pichichi.py`)
- Lenguaje y herramientas: Python 3 con **Pillow** y **ffmpeg** (instalados en el contenedor). Matplotlib no se usa.
- Salida: 1080×1920, 30 fps, h264 + AAC. Dura la locución + 0,5 s.
- Escena 1 (hasta ~62 % del vídeo): barras horizontales animadas de los 6 que más Pichichis tienen. Escena 2: la cifra del récord (50) contando hacia arriba, con el nombre, club y temporada.
- Paleta: fondo azul oscuro `(14, 22, 38)`, texto casi blanco, acento amarillo `(255, 196, 0)`, gris azulado para textos secundarios, barras azules. Fuente DejaVu Sans Bold. Pie: "Fútbol Histórico · Liga española".
- Uso: `python3 tools/short_pichichi.py out/locucion.mp3 out/short-pichichi.mp4`. Si el primer argumento no es un archivo, se interpreta como número de segundos y se genera una vista previa **sin audio**.
- Limitación conocida: las barras aparecen a ritmo fijo, **no sincronizadas** con lo que dice la voz.
- No se ha visto ni escuchado el vídeo final completo. Solo se vieron fotogramas de la versión sin audio y se comprobó formato y duración.

### 3.3 Pendiente de revisión humana (Short 001)
1. ¿La voz pronuncia bien años y cifras?
2. ¿El ritmo de las barras y la cifra 50 acompaña a lo que se dice?
3. ¿El estilo visual gusta (colores, tipografía)? ¿Falta logo o nombre del canal?

## 4. Entorno técnico y restricciones
- Las sesiones de Claude Code en la nube corren en un **contenedor efímero**: todo lo que no esté en GitHub se pierde al cerrar.
- **GitHub:** hubo un 403 al hacer push hasta que se **instaló la app de Claude** en el repo (https://github.com/apps/claude/installations/select_target; en una organización lo hace un admin; también sirve https://claude.ai/connect-github). Los repos se eligen **al crear la sesión**.
- **Red:** el entorno "Default" tiene red limitada. Para descargar los audios de ElevenLabs hay que permitir el host `elevenlabsusercontent.com` (en los ajustes del entorno: Network access → Limited → Allowed domains, con **"Allow package managers"** marcado; esa casilla permite `pip`/`npm`/`apt` sin añadirlos a mano). Ya está añadido por el usuario. La tarjeta de aprobación automática solo mostraba "Denegar", por eso se hizo a mano.
- Los servidores MCP de varias herramientas (Amplitude, Atlassian, Hex, QuickBooks, SuperMe…) fallaron al conectar por el proxy; no se han usado.
- Conectores disponibles en la sesión: ElevenLabs, Canva, Google Drive, Notion, Google Sheets, GitHub.
- Hay un **hook de fin de turno** que exige commit y push de lo pendiente en la rama.
- Los commits llevan al final las líneas de atribución (`Co-Authored-By` y `Claude-Session`).

## 5. Subida a YouTube (aún no hecha)
- Hace falta la **YouTube Data API v3** (`videos.insert`) con credenciales OAuth de Google Cloud.
- Las claves deben guardarse como secreto del entorno o de GitHub Actions. **Nunca pegarlas en el chat.**
- Los vídeos subidos por un proyecto de API **sin verificar** quedan **privados** hasta que Google audite el proyecto, y cada subida gasta mucha cuota diaria.
- Para ejecuciones periódicas: GitHub Actions o tareas programadas de Claude Code (el contenedor no es permanente).
- Política de YouTube: el contenido masivo o repetitivo sin valor añadido puede perder monetización. Conviene revisión humana y aportar algo propio.

## 6. Qué se puede automatizar (mapa de capacidades)
- **Guiones** a partir de los datos del repo.
- **Voz en off** con ElevenLabs.
- **Imágenes y vídeo** con ElevenLabs y Canva (miniaturas, diseños).
- **Subtítulos** (transcripción con ElevenLabs).
- **Montaje** en código con ffmpeg y Pillow (o matplotlib).
- **Títulos, descripciones, etiquetas y capítulos.**
- **Subida y programación** con la API de YouTube.
- **Ejecución periódica** con GitHub Actions o tareas programadas.
- Lo que Claude **no** puede hacer directamente: ver o escuchar enlaces de YouTube/TikTok/Instagram (hay que pasar la transcripción), ni ver lo que sale en pantalla de un vídeo.

## 7. Ideas descartadas o aparcadas
- **Bot que contesta comentarios con un enlace** (típico embudo de captación): no encaja con un canal de datos; los comentarios conviene contestarlos a mano. Riesgo de parecer spam y límites de cuota.
- **Buscador de clientes** (negocios sin web): no tiene relación con el canal; implicaciones legales en España (RGPD y LSSI) y condiciones de uso de las fuentes.
- **"Equipo de agentes" (varios Claude a la vez):** posible, pero duplica el coste y exige coordinación. Primero un flujo con un solo agente.
- **Panel de control** de redes, vídeos y miniaturas: útil, pero al final, cuando haya varios vídeos publicados.
- **Skills de terceros** (traspaso, PDF ligero, cavernícola, find-skills): no se instaló ninguna. Una skill es un conjunto de instrucciones con permisos de ejecución, así que hay que leerla antes de instalarla. Para recortar respuestas basta con pedir "responde breve y directo".

## 8. Hoja de ruta propuesta (orden sugerido, no un compromiso)
1. Cerrar el Short 001 con el feedback del usuario.
2. **Radar diario de ideas:** 3 ideas de vídeo al día a partir de los datos y efemérides, con borrador de guion.
3. **Pipeline por lotes:** que prepare cada vídeo y lo deje en una carpeta para aprobar.
4. **Subida a YouTube** con la API, cuando se confíe en el flujo.
5. **Panel de control**.
6. Más formatos: Shorts de Zamora, efemérides, ranking largo de 8–10 min.
7. Crear un `CLAUDE.md` (con `/init`) que recoja voz, formato del Short y reglas de revisión, para que cualquier sesión futura arranque con el contexto. Aún no existe.

## 9. Evaluación de los 4 vídeos de terceros
Las transcripciones completas están en `docs/referencias-videos.md`. Solo se analizaron por texto; no se verificó ninguna empresa, kit ni afirmación.

1. **Oficina de 19 agentes (empresa de "Guti"):** anuncio con embudo ("escribe *oficina* y te paso el kit"). La arquitectura (coordinador + agentes especializados: ventas, vídeos, ficha de Google, redes) es viable. "Ninguno es humano" es exagerado: una persona decide y resuelve lo que la IA no sabe. Más agentes no mejora el resultado por sí solo.
2. **Tres skills para gastar menos:**
   - *Traspaso* (resumir un chat largo): cierto que cada mensaje relee el historial; la caché de prompts lo abarata, pero el contexto sigue llenándose.
   - *PDF ligero* (PDF a `.md`): suele reducir el coste; comprobar que no se pierden tablas, fórmulas o gráficos.
   - *Cavernícola* (respuestas telegráficas): ahorra algo, pero puede quitar matices y advertencias; el ahorro real es menor de lo que parece.
3. **Cinco automatizaciones** (panel, radar de ideas, asistente de comentarios, buscador de clientes, equipo de agentes): ver sección 7. Solo el radar de ideas encaja de entrada. "Mejoran cada día" no es automático: mejoran si alguien las revisa y ajusta.
4. **Claude Code en 1 minuto:** casi todo es real y ya se usa aquí (Code toca archivos; modos manual, plan y auto; modelos pequeño, intermedio y grande; `/init` y `CLAUDE.md`; skills y conectores; agentes en paralelo; tareas programadas seguibles desde el móvil). No se pudo confirmar **"Claude Duet"**, ni el detalle de que el modo auto lo vigile "un segundo modelo". Los "mods" (cambiar la interfaz de Claude) no se han probado.

## 10. Criterios de calidad acordados
- Un dato histórico erróneo cuesta credibilidad: **revisión humana antes de publicar**.
- Cada dato debe poder rastrearse a su fuente (hoy: RSSSF para el Pichichi; el Zamora tiene cobertura parcial).
- Gastar créditos de ElevenLabs de forma agrupada: reunir los cambios antes de regenerar.
- No publicar nada ni conectar cuentas (YouTube, correo, Google) sin saber quién está detrás de la herramienta.

## 11. Preguntas abiertas
- ¿Qué opina el usuario del Short 001 (voz, ritmo, estilo)?
- ¿Nombre del canal, logo y estilo visual definitivos?
- ¿Qué formato va primero tras el Short: más Shorts, ranking largo o efemérides?
- ¿Cuántos vídeos por semana se quiere sacar y con qué presupuesto de créditos?
- ¿Cuándo se crea el proyecto de Google Cloud para la API de YouTube y quién lo verifica?
- ¿Se amplía la cobertura de datos (Zamora completo, Segunda División, goleadores históricos)?
