from gamelibrary import db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    console = db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return f'<name {self.name}>'
    
class Usuarios(db.Model):
    nickname = db.Column(db.String(30), primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<name \'{self.name}\'>'