from app import app, db

class Pasien(db.Model):
    __tablename__ = 'pasien'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(150))
    keluhan = db.Column(db.Text)
    diagnosa = db.Column(db.String(150))
    resep = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pendaftaran_id = db.Column(db.BigInteger, db.ForeignKey('pendaftaran.id'))
    tanggal = db.Column(db.String(100))
    
    def __init__(self, nama, keluhan, diagnosa, resep, user_id, pendaftaran_id, tanggal):
        self.nama = nama
        self.keluhan = keluhan
        self.diagnosa = diagnosa
        self.resep = resep
        self.user_id = user_id
        self.pendaftaran_id = pendaftaran_id
        self.tanggal = tanggal