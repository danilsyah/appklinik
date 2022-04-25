from app import app, db

class Suplier(db.Model):
    __tablename__ = 'suplier'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    perusahaan = db.Column(db.String(200))
    kontak = db.Column(db.String(100))
    alamat = db.Column(db.Text)
    
    def __init__(self, perusahaan, kontak, alamat):
        self.perusahaan = perusahaan
        self.kontak = kontak
        self.alamat = alamat