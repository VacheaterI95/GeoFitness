from extensions import app, db
from models import BMI, User, Calories

with app.app_context():

    db.drop_all()
    db.create_all()

    admin_user = User(firstname="Vachunchula", lastname="Melikishvili", email="vache.meliqishvili@gmail.com", password="Nahidwin", role="Admin")
    admin_user.create()
