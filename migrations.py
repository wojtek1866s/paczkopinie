from flask_migrate import Migrate
from website import create_app, db

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        # Importuj modele, aby Flask-Migrate je rozpoznał
        from website.models import User, Reviews, Paczkomats, City
        
        # Tworzy tabele dla modeli (tylko jeśli jeszcze nie istnieją)
        db.create_all()