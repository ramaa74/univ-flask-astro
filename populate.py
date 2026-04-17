from app import app, db, Camera, Telescope, Photo
from sample_data import cameras_data, telescopes_data, photos_data

with app.app_context():
    db.create_all()
    if Camera.query.first() or Telescope.query.first() or Photo.query.first():
        print("Des données existent déjà dans la base. Aucun nouvel enregistrement ajouté.")
    else:
        for cam in cameras_data:
            db.session.add(Camera(**cam))
        for tel in telescopes_data:
            db.session.add(Telescope(**tel))
        for ph in photos_data:
            db.session.add(Photo(**ph))
        db.session.commit()
        print("Données d'exemple ajoutées.")
