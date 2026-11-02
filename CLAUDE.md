# App de evaluación funcional

App web (Streamlit + Supabase) para que un profesional evalúe la condición física de sus pacientes: caminata de 6
minutos, fuerza de prensión y levantarse de la silla con percentiles de estudios publicados (CSV de este repo), peso,
IMC, cintura y cadera, InBody, medicación, informes PDF y Excel, modo demo (`demo_data.py`). Versiones anteriores:
`calculadora-funcional` y `calculadora-cristina`. Se trabaja en castellano rioplatense.

**Mapa de todos los proyectos**: antes de trabajar, adjuntá `adrsuarez22/armd-plataforma` y leé `docs/proyectos.md` (plataforma, server, Wapp, Pagos, reclutamiento y Postulantes, contable, app de evaluación funcional, agente, sociedad y negocio: todos relacionados). Las sesiones no ven otras conversaciones: **sin que Adrián lo pida**, cada vez que se decide algo, se termina una tarea o queda algo pendiente, actualizá la ficha del proyecto en ese archivo en el mismo trabajo, y agregá ahí un proyecto o una conversación nueva.

## Reglas
- Tiene datos reales de pacientes en Supabase: nunca subirlos al repo ni mostrarlos; los secretos van en
  `.streamlit/secrets.toml` (ignorado por git): nunca leer ni mostrar sus valores.
- Ampliaciones previstas: armado de dietas con lista del supermercado y plan de ejercicios según la capacidad funcional;
  la app propone y el profesional aprueba (ver regulación en la ficha del mapa).
- Pendiente: pasar este repo y los anteriores a privados (ver antes si Streamlit Community Cloud lo necesita público).
