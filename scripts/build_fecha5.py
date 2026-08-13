# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

TSV = r"""categoria	partido	complejo	cancha	dia	horario
A MASC	Marquez Denis - Ramira Omar vs Matias Nicolas Minigutti - Simón Omar Izza	OPEN	Cancha 1	Jueves	19:00 - 20:30
A MASC	Roman Gercie - Joaquín Ortiz vs Enrique Ariel - Enrique Marcelo	AMERICAS	Cancha 2	Lunes	19:00 - 20:30
A MASC	Fusse Bruno - Rodríguez Marcos vs Imanol Agnoli - Francisco Ruberto	AMERICAS	Cancha 2	Martes	21:30 - 23:00
A MASC	Julián Gea Sánchez - Joaquín Gea Sánchez vs Enrique Ariel - Enrique Marcelo	AMERICAS	Cancha 4	Viernes	21:30 - 23:00
B MASC	Ronaldo Antonio Fontana - Lucas Lautaro Corzo vs Diaz Diego - Fontanetto Emiliano	AMERICAS	Cancha 1	Jueves	17:00 - 18:30
B MASC	Jeronimo Acuña - Luca beltramino vs Balmaceda Matias - Fiore Marcelo	AMERICAS	Cancha 3	Jueves	17:00 - 18:30
B MASC	Diego Godoy - Martín Mendez vs Lautaro albertus - Leonardo Premaries	OPEN	Cancha 1	Lunes	15:00 - 16:30
B MASC	Mateo Mesquida - Adriano Tinganelli vs Altamirano Eduardo - Correa Leandro	PALERMO	Cancha 5	Lunes	16:30 - 18:00
B MASC	Alejandro Acosta - Ignacio Acosta vs Maquiavelo Santiago - Maquiavelo Nicolás	OPEN	Cancha 1	Lunes	18:00 - 19:30
B MASC	Valentín Beltzer - Ariel Jaureguiberry vs Miño cesar hernan - Axel Sartori	TERRAZAS	Cancha 1	Lunes	21:00 - 22:30
B MASC	Delisa Marcos - Grippo Agustin vs Claudio Roldán - Joaquin Roldán	OPEN	Cancha 2	Miércoles	20:00 - 21:.30
B MASC	Roldan Matias - Furlan Marcelo vs Mangioni Diego - Mildemberger Germán	OPEN	Cancha 1	Viernes	19:00 - 20:30
B MASC	Juan Cruz Leban - Germán Truffer vs Francisco Martinez - Lucas Lanzi	AMERICAS	Cancha 3	Viernes	21:00 - 22:30
B MASC	Fernando Munguía - Iván Pérez vs José Ignacio Sagasta - Alexis Sostersich	TERRAZAS	Cancha 1	Viernes	21:00 - 22:30
B MASC	Facundo Retamar - Facundo Cardoso vs Valla Luis - Bregant Sebastian	OPEN	Cancha 1	Viernes	22:00 - 23:30
C MASC	Gaioli Christian - Vega Leandro vs Juan Manuel Palacio - Leonardo Grandoli	OPEN	Cancha 1	Jueves	16:00 - 17:30
C MASC	Valentino Sánchez - Thiago Rivera vs Zapata Valentino - Zapata Joaquín	OPEN	Cancha 2	Lunes	18:00 - 19:30
C MASC	Nicolas Adrian del Mestre - Cristian Agustin Roude vs Facundo Capatto - Miguel Screpis	AMERICAS	Cancha 4	Lunes	21:00 - 22:30
C MASC	Bastidas Exequiel - Arrias Iñaki vs Marzoratti sebastian - Marzoratti miguel	OPEN	Cancha 1	Martes	18:00 - 19:30
C MASC	Pablo Grimaldi - Darío Tejero vs Candillu Enzo Julián - Richard Geronimo	OPEN	Cancha 1	Martes	19:30 - 21:00
C MASC	Francisco Espinoza - Joaquín Rodríguez vs Alejandro Chilotegui - Daniel González	PALERMO	Cancha 2	Miércoles	19:00 - 20:30
C MASC	Diego Germán Ramírez - Martín Rondan vs Buyatti Facundo - Buyatti Matias	AMERICAS	Cancha 1	Viernes	15:30 - 17:00
C MASC	Luna Milagros - Corona Gisela vs Diego Germán Ramírez - Martín Rondan	AMERICAS	Cancha 1	Martes	15:30 - 17:00
C MASC	Milton Reatto - Joaquín Lucero vs Rettore Santiago - Aranda Santiago	PALERMO	Cancha 4	Viernes	17:00 - 18:30
C MASC	Valentino Sánchez - Thiago Rivera vs Martinez A. Javier - Strack José Maria	AMERICAS	Cancha 1	Viernes	21:30 - 23:00
C MASC	Milton Reatto - Joaquín Lucero vs Bautista Bellodi - Solana Bellodi	TERRAZAS	Cancha 1	Miércoles	21:30 - 23:00
C MASC	Gian Lucas Aldana - Fernando Sánchez vs Octavio Claro - Juan Cappeletti	TERRAZAS	Cancha 2	Viernes	21:30 - 23:00
B FEM	Chiara Silvina - Weller Maria Eugenia vs Espina Casas Sol - Roldán Virginia	OPEN	Cancha 1	Jueves	17:30 - 19:00
B FEM	Priscila Oroño - Iara Godoy vs Alvarez Janet - Jotensky Daniela	AMERICAS	Cancha 2	Miércoles	20:00 - 21:30
B FEM	Valentina Gabirondo - Delfina Balla vs Jimena tonutti - Aldana godi	OPEN	Cancha 1	Martes	21:00 - 22:30
B FEM	Greta López Muller - Milagros Patrizi vs Natacha Carmaran - Magdalena Laporta	AMERICAS	Cancha 2	Viernes	15:30 - 17:00
C FEM	Barzola Maria Eugenia - Joubert Florencia Marianela vs Karen Aguilera - Ariana Bourlot	PALERMO	Cancha 2	Jueves	18:30 - 20:00
C FEM	Vittori Andrea - Romero Fabiana vs Evelyn Tonutti - Victoria Córdoba	AMERICAS	Cancha 1	Martes	14:00 - 15:30
C FEM	Romeo Sabrina - Cura Karime vs Jennifer Noro - Maria Gonzalez	OPEN	Cancha 2	Martes	20:30 - 22:00
C FEM	Carina Kriger - Micaela Sinner vs Pereira Sofia - Lorenzon Almendra	OPEN	Cancha 2	Jueves	20:00 - 21:30
C FEM	Garcetti Flor - Estebenet Sandra vs Croce Antonella - Morley Jessie	OPEN	Cancha 1	Sábado	10:00 - 11:30
C FEM	Valentina Bescos - Mara Chaparro vs Gonzalez Micaela - Romero Daiana	OPEN	Cancha 1	Sábado	15:00 - 16:30
C FEM	Cavallaro Florencia - Yancovich Luisina vs Juliana Casablanca - Soledad Albe	AMERICAS	Cancha 1	Viernes	17:00 - 18:30
C FEM	Cantero gladys - Daniela Sosa Benintende vs Gonzalez Micaela - Romero Daiana	OPEN	Cancha 1	Sábado	15:00 - 16:30
C FEM	Pereira Sofia - Lorenzon Almendra vs Cantero gladys - Daniela Sosa Benintende	TERRAZAS	Cancha 3	Viernes	22:00 - 23:30
"""

CAT_MAP = {
    "A MASC": "A Masculina",
    "B MASC": "B Masculina",
    "C MASC": "C Masculina",
    "A FEM": "A Femenino",
    "B FEM": "B Femenino",
    "C FEM": "C Femenino",
}
VENUE_MAP = {
    "OPEN": "Open",
    "AMERICAS": "Américas",
    "PALERMO": "Palermo Pádel",
    "TERRAZAS": "Terrazas",
}


def split_partido(partido: str):
    parts = re.split(r"\s+vs\.?\s+", partido.strip(), flags=re.I)
    def pair(s):
        return re.sub(r"\s*[–—-]\s*", " / ", s.strip())
    if len(parts) >= 2:
        return pair(parts[0]), pair(" vs ".join(parts[1:]))
    return pair(partido), ""


def norm_time(t: str):
    return re.sub(r"(\d):\.(?=\d)", r"\1:", t).strip()


rows = []
for line in TSV.strip().splitlines()[1:]:
    cat, partido, complejo, cancha, dia, horario = line.split("\t")
    home, away = split_partido(partido)
    rows.append({
        "week": "Fecha 5",
        "day": dia.strip(),
        "date": "",
        "temp": "T4",
        "cat": CAT_MAP.get(cat.strip().upper(), cat.strip()),
        "time": norm_time(horario),
        "venue": VENUE_MAP.get(complejo.strip().upper(), complejo.strip()),
        "court": cancha.strip(),
        "home": home,
        "away": away,
        "result": "",
    })

out = Path(__file__).resolve().parents[1] / "src" / "data" / "fixture.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote {len(rows)} matches -> {out}")
