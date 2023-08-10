from labapp.ext.database import db

class Cargo(db.Model):
    __tablename__ = 'Cargo'
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Cargo {self.id} {self.cargo}>'

class Colaboradores(db.Model):
    __tablename__ = 'Colaboradores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    foto = db.Column(db.String(255), nullable=False)
    resumo = db.Column(db.String(400), nullable=False)
    saiba_mais = db.Column(db.String(255), nullable=False)
    cargo_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Colaborador {self.id} {self.nome} {self.cargo_id} {self.resumo}>'

class Biblioteca(db.Model):
    __tablename__ = 'Biblioteca'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Publicação {self.id} {self.titulo} {self.link}>'

class Projeto(db.Model):
    __tablename__ = 'Projeto'
    id = db.Column(db.Integer, primary_key=True)
    resumo = db.Column(db.String(255), nullable=False)
    data_publicacao = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Projeto {self.id} {self.resumo} {self.data_publicacao}>'

class Games(db.Model):
    __tablename__ = 'Games'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    capa = db.Column(db.String(255), nullable=False)
    pagina = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Games {self.id} {self.titulo} {self.link}>'

class DisplayCast(db.Model):
    __tablename__ = 'DisplayCast'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    capa = db.Column(db.String(255), nullable=False)
    link_iframe = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<DisplayCast {self.id} {self.titulo} {self.link_iframe}>'

class Projeto_Games(db.Model):
    __tablename__ = 'Projeto_Games'
    projeto_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'<Projeto_Games {self.projeto_id} {self.game_id}>'

class Projeto_DisplayCast(db.Model):
    __tablename__ = 'Projeto_DisplayCast'
    projeto_id = db.Column(db.Integer, primary_key=True)
    displaycast_id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'<Projeto_DisplayCast {self.projeto_id} {self.displaycast_id}>'