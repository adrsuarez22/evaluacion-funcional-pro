# =========================================================
# DATOS DE DEMOSTRACION
# =========================================================
# Pacientes ficticios para el modo demo. No existen en Supabase: la app los
# arma en memoria cuando session_state["modo_demo"] es True.
#
# Solo se declaran los valores medidos. Los derivados (IMC, ICC, ICA,
# percentiles, clasificaciones) los calcula app.py con sus propias funciones,
# para que la demo sea coherente con las tablas de referencia reales.
#
# La medicación es toda de laboratorio Novo Nordisk.

DEMO_PACIENTES = [
    {
        "id": 9001,
        "nombre": "Lucía Fernández",
        "sexo": "mujer",
        "fecha_nacimiento": "1979-04-18",
        "talla_m": 1.62,
    },
    {
        "id": 9002,
        "nombre": "Martín Gaitán",
        "sexo": "hombre",
        "fecha_nacimiento": "1972-11-30",
        "talla_m": 1.78,
    },
    {
        "id": 9003,
        "nombre": "Elena Ruiz",
        "sexo": "mujer",
        "fecha_nacimiento": "1956-02-09",
        "talla_m": 1.57,
    },
    {
        "id": 9004,
        "nombre": "Jorge Medina",
        "sexo": "hombre",
        "fecha_nacimiento": "1962-07-22",
        "talla_m": 1.72,
    },
]


# Peso y perímetros. El IMC, el ICC y el ICA los calcula app.py.
DEMO_PESO = {
    9001: [
        {"fecha": "2026-02-10", "peso_kg": 92.4, "cintura_cm": 104.0, "cadera_cm": 118.0},
        {"fecha": "2026-04-14", "peso_kg": 89.1, "cintura_cm": 101.0, "cadera_cm": 116.0},
        {"fecha": "2026-06-16", "peso_kg": 86.5, "cintura_cm": 98.0, "cadera_cm": 114.0},
        {"fecha": "2026-08-18", "peso_kg": 84.8, "cintura_cm": 96.0, "cadera_cm": 112.5},
        {"fecha": "2026-09-22", "peso_kg": 83.9, "cintura_cm": 95.0, "cadera_cm": 112.0},
    ],
    9002: [
        {"fecha": "2026-02-10", "peso_kg": 108.2, "cintura_cm": 118.0, "cadera_cm": 112.0},
        {"fecha": "2026-04-14", "peso_kg": 104.6, "cintura_cm": 114.0, "cadera_cm": 110.0},
        {"fecha": "2026-06-16", "peso_kg": 101.3, "cintura_cm": 110.0, "cadera_cm": 108.0},
        {"fecha": "2026-08-18", "peso_kg": 98.7, "cintura_cm": 107.0, "cadera_cm": 106.5},
        {"fecha": "2026-09-22", "peso_kg": 97.1, "cintura_cm": 106.0, "cadera_cm": 106.0},
    ],
    9003: [
        {"fecha": "2026-02-10", "peso_kg": 78.0, "cintura_cm": 98.0, "cadera_cm": 106.0},
        {"fecha": "2026-04-14", "peso_kg": 76.8, "cintura_cm": 96.0, "cadera_cm": 105.0},
        {"fecha": "2026-06-16", "peso_kg": 75.6, "cintura_cm": 94.0, "cadera_cm": 104.0},
        {"fecha": "2026-08-18", "peso_kg": 74.5, "cintura_cm": 92.5, "cadera_cm": 103.0},
        {"fecha": "2026-09-22", "peso_kg": 74.1, "cintura_cm": 92.0, "cadera_cm": 103.0},
    ],
    9004: [
        {"fecha": "2026-02-10", "peso_kg": 99.4, "cintura_cm": 112.0, "cadera_cm": 107.0},
        {"fecha": "2026-04-14", "peso_kg": 97.6, "cintura_cm": 109.0, "cadera_cm": 105.5},
        {"fecha": "2026-06-16", "peso_kg": 95.8, "cintura_cm": 106.0, "cadera_cm": 104.0},
        {"fecha": "2026-08-18", "peso_kg": 94.1, "cintura_cm": 104.0, "cadera_cm": 103.5},
        {"fecha": "2026-09-22", "peso_kg": 93.2, "cintura_cm": 103.0, "cadera_cm": 103.0},
    ],
}


# Evaluaciones funcionales. El percentil y la clasificación los calcula app.py
# con calcular_resultado(), contra las mismas tablas que usa la carga manual.
DEMO_EVALUACIONES = {
    9001: [
        {"fecha": "2026-02-10", "prueba": "Caminata 6 minutos", "valor_medido": 455.0},
        {"fecha": "2026-02-10", "prueba": "Prensión manual", "valor_medido": 22.5},
        {"fecha": "2026-06-16", "prueba": "Caminata 6 minutos", "valor_medido": 498.0},
        {"fecha": "2026-06-16", "prueba": "Prensión manual", "valor_medido": 24.4},
        {"fecha": "2026-09-22", "prueba": "Caminata 6 minutos", "valor_medido": 540.0},
        {"fecha": "2026-09-22", "prueba": "Prensión manual", "valor_medido": 26.0},
    ],
    9002: [
        {"fecha": "2026-02-10", "prueba": "Caminata 6 minutos", "valor_medido": 498.0},
        {"fecha": "2026-02-10", "prueba": "Prensión manual", "valor_medido": 34.0},
        {"fecha": "2026-06-16", "prueba": "Caminata 6 minutos", "valor_medido": 531.0},
        {"fecha": "2026-06-16", "prueba": "Prensión manual", "valor_medido": 37.2},
        {"fecha": "2026-09-22", "prueba": "Caminata 6 minutos", "valor_medido": 560.0},
        {"fecha": "2026-09-22", "prueba": "Prensión manual", "valor_medido": 40.0},
    ],
    9003: [
        {"fecha": "2026-02-10", "prueba": "Caminata 6 minutos", "valor_medido": 398.0},
        {"fecha": "2026-02-10", "prueba": "Prensión manual", "valor_medido": 16.5},
        {"fecha": "2026-02-10", "prueba": "Levantarse de la silla", "valor_medido": 9.0},
        {"fecha": "2026-06-16", "prueba": "Caminata 6 minutos", "valor_medido": 421.0},
        {"fecha": "2026-06-16", "prueba": "Prensión manual", "valor_medido": 18.1},
        {"fecha": "2026-06-16", "prueba": "Levantarse de la silla", "valor_medido": 11.0},
        {"fecha": "2026-09-22", "prueba": "Caminata 6 minutos", "valor_medido": 440.0},
        {"fecha": "2026-09-22", "prueba": "Prensión manual", "valor_medido": 19.5},
        {"fecha": "2026-09-22", "prueba": "Levantarse de la silla", "valor_medido": 12.0},
    ],
    9004: [
        {"fecha": "2026-02-10", "prueba": "Caminata 6 minutos", "valor_medido": 470.0},
        {"fecha": "2026-02-10", "prueba": "Prensión manual", "valor_medido": 31.0},
        {"fecha": "2026-06-16", "prueba": "Caminata 6 minutos", "valor_medido": 503.0},
        {"fecha": "2026-06-16", "prueba": "Prensión manual", "valor_medido": 34.1},
        {"fecha": "2026-09-22", "prueba": "Caminata 6 minutos", "valor_medido": 530.0},
        {"fecha": "2026-09-22", "prueba": "Prensión manual", "valor_medido": 36.5},
    ],
}


# Composición corporal. El IMC lo calcula app.py a partir del peso y la talla.
DEMO_INBODY = {
    9001: [
        {
            "fecha": "2026-02-10",
            "peso_kg": 92.4,
            "grasa_corporal_pct": 44.2,
            "masa_muscular_kg": 25.8,
            "agua_corporal_pct": 41.0,
            "grasa_visceral": 14.0,
            "metabolismo_basal": 1412.0,
            "observaciones": "Estudio basal previo a inicio de tratamiento.",
        },
        {
            "fecha": "2026-06-16",
            "peso_kg": 86.5,
            "grasa_corporal_pct": 41.0,
            "masa_muscular_kg": 25.9,
            "agua_corporal_pct": 43.2,
            "grasa_visceral": 12.0,
            "metabolismo_basal": 1388.0,
            "observaciones": "Descenso de grasa con masa muscular conservada.",
        },
        {
            "fecha": "2026-09-22",
            "peso_kg": 83.9,
            "grasa_corporal_pct": 38.6,
            "masa_muscular_kg": 26.2,
            "agua_corporal_pct": 44.8,
            "grasa_visceral": 10.0,
            "metabolismo_basal": 1379.0,
            "observaciones": "Mejora sostenida del perfil de composición corporal.",
        },
    ],
    9002: [
        {
            "fecha": "2026-02-10",
            "peso_kg": 108.2,
            "grasa_corporal_pct": 36.4,
            "masa_muscular_kg": 37.1,
            "agua_corporal_pct": 46.5,
            "grasa_visceral": 18.0,
            "metabolismo_basal": 1824.0,
            "observaciones": "Obesidad de predominio abdominal.",
        },
        {
            "fecha": "2026-06-16",
            "peso_kg": 101.3,
            "grasa_corporal_pct": 32.8,
            "masa_muscular_kg": 37.4,
            "agua_corporal_pct": 48.9,
            "grasa_visceral": 15.0,
            "metabolismo_basal": 1801.0,
            "observaciones": "Reducción de grasa visceral con masa magra estable.",
        },
        {
            "fecha": "2026-09-22",
            "peso_kg": 97.1,
            "grasa_corporal_pct": 30.1,
            "masa_muscular_kg": 37.8,
            "agua_corporal_pct": 50.4,
            "grasa_visceral": 13.0,
            "metabolismo_basal": 1793.0,
            "observaciones": "Buena respuesta al plan combinado.",
        },
    ],
    9003: [
        {
            "fecha": "2026-02-10",
            "peso_kg": 78.0,
            "grasa_corporal_pct": 42.8,
            "masa_muscular_kg": 21.4,
            "agua_corporal_pct": 42.1,
            "grasa_visceral": 13.0,
            "metabolismo_basal": 1218.0,
            "observaciones": "Masa muscular baja para la edad.",
        },
        {
            "fecha": "2026-09-22",
            "peso_kg": 74.1,
            "grasa_corporal_pct": 40.1,
            "masa_muscular_kg": 21.9,
            "agua_corporal_pct": 43.6,
            "grasa_visceral": 11.0,
            "metabolismo_basal": 1206.0,
            "observaciones": "Descenso de peso con ganancia leve de masa muscular.",
        },
    ],
    9004: [
        {
            "fecha": "2026-02-10",
            "peso_kg": 99.4,
            "grasa_corporal_pct": 35.1,
            "masa_muscular_kg": 33.6,
            "agua_corporal_pct": 46.8,
            "grasa_visceral": 16.0,
            "metabolismo_basal": 1682.0,
            "observaciones": "Control inicial.",
        },
        {
            "fecha": "2026-09-22",
            "peso_kg": 93.2,
            "grasa_corporal_pct": 31.4,
            "masa_muscular_kg": 34.0,
            "agua_corporal_pct": 49.2,
            "grasa_visceral": 13.0,
            "metabolismo_basal": 1664.0,
            "observaciones": "Mejoría del perfil cardiometabólico.",
        },
    ],
}


# Medicación: toda de laboratorio Novo Nordisk. Los cuatro pacientes siguen el
# mismo esquema de Wegovy semanal, escalado hasta la dosis de mantenimiento
# de 2.4 mg; cambia el ritmo del escalado, no el destino.
DEMO_MEDICACION = {
    9001: [
        {
            "fecha_cambio": "2026-02-10",
            "droga": "Wegovy (semaglutida)",
            "dosis": 0.25,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Inicio del escalado mensual.",
        },
        {
            "fecha_cambio": "2026-03-17",
            "droga": "Wegovy (semaglutida)",
            "dosis": 1.0,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Buena tolerancia digestiva.",
        },
        {
            "fecha_cambio": "2026-06-16",
            "droga": "Wegovy (semaglutida)",
            "dosis": 1.7,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Continúa el escalado.",
        },
        {
            "fecha_cambio": "2026-09-22",
            "droga": "Wegovy (semaglutida)",
            "dosis": 2.4,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Activa",
            "observaciones": "Dosis de mantenimiento. Continúa descenso de peso.",
        },
    ],
    9002: [
        {
            "fecha_cambio": "2026-02-10",
            "droga": "Wegovy (semaglutida)",
            "dosis": 0.25,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Inicio en diabetes tipo 2 con obesidad.",
        },
        {
            "fecha_cambio": "2026-04-14",
            "droga": "Wegovy (semaglutida)",
            "dosis": 0.5,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Escalado al mes de tratamiento.",
        },
        {
            "fecha_cambio": "2026-06-16",
            "droga": "Wegovy (semaglutida)",
            "dosis": 1.7,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Buena respuesta metabólica.",
        },
        {
            "fecha_cambio": "2026-08-18",
            "droga": "Wegovy (semaglutida)",
            "dosis": 2.4,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Activa",
            "observaciones": "Dosis de mantenimiento.",
        },
    ],
    9003: [
        {
            "fecha_cambio": "2026-02-10",
            "droga": "Wegovy (semaglutida)",
            "dosis": 0.25,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Inicio con escalado lento por edad.",
        },
        {
            "fecha_cambio": "2026-04-14",
            "droga": "Wegovy (semaglutida)",
            "dosis": 0.5,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Sin efectos adversos digestivos.",
        },
        {
            "fecha_cambio": "2026-06-16",
            "droga": "Wegovy (semaglutida)",
            "dosis": 1.0,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Se mantiene el escalado gradual.",
        },
        {
            "fecha_cambio": "2026-08-18",
            "droga": "Wegovy (semaglutida)",
            "dosis": 1.7,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Tolerancia conservada.",
        },
        {
            "fecha_cambio": "2026-09-22",
            "droga": "Wegovy (semaglutida)",
            "dosis": 2.4,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Activa",
            "observaciones": "Dosis de mantenimiento alcanzada.",
        },
    ],
    9004: [
        {
            "fecha_cambio": "2026-02-10",
            "droga": "Wegovy (semaglutida)",
            "dosis": 0.25,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Inicio en diabetes tipo 2 con obesidad.",
        },
        {
            "fecha_cambio": "2026-04-14",
            "droga": "Wegovy (semaglutida)",
            "dosis": 1.0,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Escalado al mes de tratamiento.",
        },
        {
            "fecha_cambio": "2026-06-16",
            "droga": "Wegovy (semaglutida)",
            "dosis": 1.7,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Suspendida",
            "observaciones": "Mejora del perfil glucémico.",
        },
        {
            "fecha_cambio": "2026-08-18",
            "droga": "Wegovy (semaglutida)",
            "dosis": 2.4,
            "unidad": "mg",
            "frecuencia": "1 vez por semana",
            "via_administracion": "Subcutánea",
            "estado": "Activa",
            "observaciones": "Dosis de mantenimiento.",
        },
    ],
}
