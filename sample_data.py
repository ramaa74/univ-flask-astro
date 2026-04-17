from datetime import date

cameras_data = [
    {"category": "Amateur", "brand": "Canon", "model": "EOS Rebel T7", "release_date": date(2018, 3, 1), "score": 4},
    {"category": "Amateur", "brand": "Nikon", "model": "D3500", "release_date": date(2018, 8, 30), "score": 4},
    {"category": "Amateur sérieux", "brand": "Sony", "model": "A7 III", "release_date": date(2018, 2, 27), "score": 5},
    {"category": "Amateur sérieux", "brand": "Canon", "model": "EOS 6D Mark II", "release_date": date(2017, 6, 29), "score": 4},
    {"category": "Professionnel", "brand": "Nikon", "model": "D5", "release_date": date(2016, 1, 6), "score": 5},
    {"category": "Professionnel", "brand": "Canon", "model": "EOS-1D X Mark II", "release_date": date(2016, 2, 2), "score": 5},
]

telescopes_data = [
    {"category": "Pour enfants", "brand": "Celestron", "model": "FirstScope", "release_date": date(2016, 1, 1), "score": 3},
    {"category": "Pour enfants", "brand": "Orion", "model": "StarBlast II", "release_date": date(2010, 1, 1), "score": 4},
    {"category": "Automatisés", "brand": "Celestron", "model": "NexStar 8SE", "release_date": date(2015, 1, 1), "score": 5},
    {"category": "Automatisés", "brand": "Meade", "model": "LX200", "release_date": date(1998, 1, 1), "score": 4},
    {"category": "Complets", "brand": "Celestron", "model": "EdgeHD 14", "release_date": date(2014, 1, 1), "score": 5},
    {"category": "Complets", "brand": "Takahashi", "model": "TOA-130", "release_date": date(2005, 1, 1), "score": 5},
]

photos_data = [
    {
        "title": "Voie Lactée",
        "description": "Une belle photo de la Voie Lactée.",
        "image_path": "/static/images/milky_way.svg",
    },
    {
        "title": "Nébuleuse d'Orion",
        "description": "La célèbre nébuleuse d'Orion.",
        "image_path": "/static/images/orion_nebula.svg",
    },
    {
        "title": "Galaxie d'Andromède",
        "description": "La galaxie d'Andromède vue de près.",
        "image_path": "/static/images/andromeda.svg",
    },
]

vlogs_data = [
    {
        "title": "Balade sous les étoiles",
        "description": "Une exploration en direct sur les meilleures constellations du moment.",
        "link": "#",
    },
    {
        "title": "Comment choisir un télescope",
        "description": "Conseils pour débuter dans le vlog astronomique et choisir son matériel.",
        "link": "#",
    },
    {
        "title": "Photo astro pour débutants",
        "description": "Méthodes simples pour capturer des images de la Lune et des étoiles.",
        "link": "#",
    },
]
