# Resumen de la conversación · Automatizar el canal de YouTube

## Objetivo
Automatizar un canal de YouTube de fútbol histórico español usando los datos del repo `luyspilo/futbol-historico`. Formatos: todos (Shorts, rankings, efemérides, vídeos largos). Voz: la del usuario, clonada en ElevenLabs. Flujo: **primero revisa el usuario**, y cuando el flujo esté probado se automatiza la subida.

## Estado actual
- **Rama:** `claude/youtube-channel-automation-9s6ams`, subida a GitHub.
- **Voz:** ElevenLabs "Luis CLICK" (`voice_id` F2AZuQ11KpWHmLfhVFT5), modelo `eleven_v3`.
- **Short 001 (Pichichi, 29 s, vertical 1080×1920):** hecho y subido.
  - `tools/short_pichichi.py`: genera el vídeo a partir de `data/primera-pichichi.json`.
  - `guiones/001-pichichi-short.md`: locución, título y descripción.
  - `out/locucion.mp3` y `out/short-pichichi.mp4`: audio y vídeo final.
- **Pendiente del usuario:** revisar el Short (pronunciación de años y cifras, ritmo, estilo visual) y decir qué cambiar.

## Incidencias resueltas
- El push daba 403 hasta que se instaló la app de Claude en el repo.
- El host `elevenlabsusercontent.com` estaba bloqueado. La tarjeta de aprobación solo mostraba "Denegar", así que el usuario lo añadió a mano en los ajustes del entorno (Allowed domains, con "Allow package managers" marcado).

## Vídeos de terceros analizados (solo por transcripción)
1. **"Oficina de 19 agentes":** es un anuncio con embudo de captación. La arquitectura es viable, pero "ninguno es humano" es exagerado.
2. **Tres skills para gastar menos:** consejos razonables (resumir chats largos, convertir PDF a `.md`, respuestas breves). El ahorro real es menor de lo que sugiere y hay que leer las skills antes de instalarlas.
3. **Cinco "cositas" de automatización:** panel, radar de ideas, bot de comentarios, buscador de clientes y equipo de agentes. Solo el radar de ideas encaja bien con el canal. El buscador de clientes tiene implicaciones legales (RGPD/LSSI).
4. **Claude Code en 1 minuto:** casi todo es real y ya se usa en esta sesión. No pude confirmar "Claude Duet".

No se instaló ninguna skill externa. No se verificó ninguno de esos vídeos ni sus "kits".

## Orden de trabajo propuesto
1. Cerrar el Short 001 con el feedback del usuario.
2. Radar diario de ideas, con borradores de guion a partir de los datos.
3. Pipeline que prepare cada vídeo y lo deje en una carpeta para aprobar.
4. Subida a YouTube con la API (necesita credenciales OAuth; los vídeos de un proyecto de API sin verificar quedan privados).
5. Panel de control, al final.

## Límites a recordar
- El contenedor es efímero: lo que no esté en GitHub se pierde.
- La generación con ElevenLabs gasta créditos (la toma del Short 001 costó 474).
- Automatizar todo sin revisión puede chocar con la política de contenido repetitivo de YouTube.
- Idea pendiente: crear un `CLAUDE.md` (con `/init`) con la voz, el formato del Short y las reglas de revisión.
