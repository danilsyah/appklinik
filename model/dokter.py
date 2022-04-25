from app import app, db


class Dokter(db.Model):
    __tablename__ = 'dokter'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(150))
    jadwal = db.Column(db.Text)
    
    def __init__(self, nama, jadwal):
        self.nama= nama
        self.jadwal = jadwal