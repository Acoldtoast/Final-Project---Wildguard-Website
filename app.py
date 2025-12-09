# wildguard/app.py

from flask import Flask
from flask_login import LoginManager
from models import db, User 
from routes.pages import pages
from routes.auth import auth
from routes.animals import animals
from routes.admin import admin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey123'  # Secret key helps keep sessions/forms safe
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wildguard.db'  # Where our data will be saved
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turns off unnecessary tracking
    
db.init_app(app)
    
login_manager = LoginManager()
login_manager.login_view = 'auth.admin_login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'
login_manager.init_app(app)
    
@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))
    
app.register_blueprint(pages)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(animals)
app.register_blueprint(admin)
    
if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
        print("\n✓ Database tables created successfully!")
        
        admin_user = User.query.filter_by(username='Wildguardofficialadmin').first()
        if not admin_user:
            admin_user = User(username='Wildguardofficialadmin', is_admin=True)
            admin_user.set_password('Wildguard2025adminonly')
            db.session.add(admin_user)
            db.session.commit()
            print("✓ Admin user created: Wildguardofficialadmin")
        else:
            print("✓ Admin user already exists.")
    
    print("\n-------------------------------------------------")
    print("🌿 WildGuard Server Starting...")
    print("📍 Running at: http://127.0.0.1:5000")
    print("-------------------------------------------------")

    app.run(debug=True, host='127.0.0.1', port=5000)