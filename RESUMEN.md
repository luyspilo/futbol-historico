# Resumen de la conversación · Automatizar el canal de YouTube

## Objetivo
Automatizar un canal de YouTube de fútbol histórico español con los datos del repo `luyspilo/futbol-historico`. Formatos: todos (Shorts, rankings, efemérides, vídeos largos). Voz: la del usuario, clonada en ElevenLabs. Flujo: **el usuario revisa primero**, y cuando el flujo esté probado se automatiza la subida.

## Estado actual
- **Repo y rama:** `luyspilo/futbol-historico`, rama `claude/youtube-channel-automation-9s6ams`. Todo subido; no hay pull request.
- **Voz:** ElevenLabs "Luis CLICK" (`voice_id` F2AZuQ11KpWHmLfhVFT5), modelo `eleven_v3`. La toma costó 474 créditos.
- **Short 001 (Pichichi, 29 s, vertical 1080×1920):** hecho.
  - `tools/short_pichichi.py` genera el vídeo desde `data/primera-pichichi.json`. Uso: `python3 tools/short_pichichi.py out/locucion.mp3 out/short-pichichi.mp4`. Si en vez del audio se pasa un número de segundos, genera una vista previa sin sonido.
  - `guiones/001-pichichi-short.md` tiene la locución, el título y la descripción.
  - `out/locucion.mp3` y `out/short-pichichi.mp4` son el audio y el vídeo final.
- **Pendiente del usuario:** revisar el Short (pronunciación de años y cifras, ritmo de las barras con la voz, estilo visual) y decir qué cambiar.
  - Claude no ha visto ni escuchado el resultado final. Solo comprobó que el formato y la duración son correctos.

## Incidencias resueltas
- El push daba 403 hasta que se instaló la app de Claude en el repo.
- El host `elevenlabsusercontent.com` estaba bloqueado. La tarjeta de aprobación solo mostraba "Denegar", así que el usuario lo añadió a mano en los ajustes del entorno Default (Allowed domains, con "Allow package managers" marcado).

## Vídeos de terceros analizados (solo por transcripción, sin verificar)
1. **Oficina de 19 agentes:** anuncio con embudo de captación. La arquitectura es viable, pero "ninguno es humano" es exagerado.
2. **Tres skills para gastar menos** (traspaso, PDF ligero, cavernícola): consejos razonables. El ahorro real es menor de lo que sugiere, y hay que leer cualquier skill de terceros antes de instalarla.
3. **Cinco automatizaciones** (panel, radar de ideas, bot de comentarios, buscador de clientes, equipo de agentes): solo el radar de ideas encaja bien con el canal. El buscador de clientes tiene implicaciones legales (RGPD y LSSI).
4. **Claude Code en 1 minuto:** casi todo es real y ya se usa en la sesión. No se pudo confirmar "Claude Duet".

No se instaló ninguna skill externa.

## Orden de trabajo propuesto
1. Cerrar el Short 001 con el feedback del usuario.
2. Radar diario de ideas, con borradores de guion a partir de los datos del repo.
3. Pipeline que prepare cada vídeo y lo deje en una carpeta para aprobar.
4. Subida a YouTube con la API (necesita credenciales OAuth; los vídeos de un proyecto de API sin verificar quedan privados).
5. Panel de control, al final.

## Límites a recordar
- El contenedor es efímero: lo que no está en GitHub se pierde.
- La generación con ElevenLabs gasta créditos.
- Automatizar todo sin revisión puede chocar con la política de contenido repetitivo de YouTube, y un dato histórico erróneo cuesta credibilidad.
- Idea pendiente: crear un `CLAUDE.md` (con `/init`) con la voz, el formato del Short y las reglas de revisión.

## Para retomarlo en un chat nuevo
Crear la sesión nueva **con el repo `luyspilo/futbol-historico` seleccionado** y pegar:

> Continúo el proyecto de automatizar mi canal de fútbol histórico. El repo es `luyspilo/futbol-historico`, rama `claude/youtube-channel-automation-9s6ams`. Ya hay un Short 001 hecho. Lee `RESUMEN.md` y `guiones/001-pichichi-short.md`; te doy mi feedback sobre el vídeo y seguimos.
