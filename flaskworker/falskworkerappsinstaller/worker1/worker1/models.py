from project.app import db, ma 
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.Text, nullable=True)
    password=db.Column(db.Text, nullable=True)
    address=db.Column(db.Text)
    
class UserSchema(ma.Schema):

    class Meta:
        Model=User
        fields = ("id","username","password", "address")
