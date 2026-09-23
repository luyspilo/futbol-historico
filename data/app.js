(() => {
  const mount = document.createElement('section');
  mount.className = 'card';
  mount.style.marginTop = '18px';
  mount.innerHTML = '<div class="section"><h2>Datos históricos importados</h2><span class="badge">Fuente: RSSSF</span></div><div class="note">Cargando registros verificados…</div>';
  document.querySelector('main').appendChild(mount);
  fetch('data/primera-pichichi.json?v=20260923-2').then(r => r.json()).then(data => {
    const rows = [...data.rows].sort((a,b) => b.goals - a.goals || a.season.localeCompare(b.season));
    mount.innerHTML = '<div class="section"><h2>Pichichi · registros históricos importados</h2><span class="badge">' + data.rows.length + ' temporadas verificadas</span></div>' + '<table class="table"><thead><tr><th>Temporada</th><th>Jugador</th><th>Club</th><th>Goles</th><th>Partidos</th></tr></thead><tbody>' + rows.map(x => '<tr><td>' + x.season + '</td><td><b>' + x.person + '</b></td><td>' + x.club + '</td><td><span class="badge">' + x.goals + '</span></td><td>' + x.matches + '</td></tr>').join('') + '</tbody></table><div class="note">Cada fila conserva su fuente en el catálogo de datos. La importación continuará temporada por temporada.</div>';
  }).catch(() => { mount.querySelector('.note').textContent = 'No se pudo cargar el catálogo local de datos.'; });
  fetch('data/primera-zamora.json?v=20260923-1').then(r => r.json()).then(data => {
    const zamora = document.createElement('section'); zamora.className = 'card'; zamora.style.marginTop = '18px';
    zamora.innerHTML = '<div class="section"><h2>Zamora · porteros menos goleados</h2><span class="badge">' + data.rows.length + ' temporadas · cobertura parcial</span></div>' + '<table class="table"><thead><tr><th>Temporada</th><th>Portero</th><th>Club</th><th>Coeficiente</th><th>Goles</th><th>Partidos</th></tr></thead><tbody>' + data.rows.map(x => '<tr><td>' + x.season + '</td><td><b>' + x.person + '</b></td><td>' + x.club + '</td><td><span class="badge">' + x.coefficient.toFixed(2) + '</span></td><td>' + x.goalsConceded + '</td><td>' + x.matches + '</td></tr>').join('') + '</tbody></table><div class="note">Bloque histórico inicial verificado con la fuente documentada. Se ampliará hasta la temporada actual.</div>';
    document.querySelector('main').appendChild(zamora);
  });
})();
