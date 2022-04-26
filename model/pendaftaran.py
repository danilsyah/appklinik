from os import stat
from app import app, db

class Pendaftaran(db.Model):
    __tablename__ = 'pendaftaran'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(150))
    tempat_lahir = db.Column(db.String(150))
    tgl_lahir = db.Column(db.String(150))
    jenis_kelamin = db.Column(db.String(100))
    status = db.Column(db.String(100))
    profesi = db.Column(db.String(100))
    alamat = db.Column(db.Text)
    keterangan = db.Column(db.String(100))
    db.relationship('Pasien', backref=db.backref('pendaftaran', lazy=True))
    
    def __init__(self, nama, tempat_lahir, tgl_lahir, jenis_kelamin, status, profesi, alamat, keterangan):
        self.nama = nama
        self.tempat_lahir = tempat_lahir
        self.tgl_lahir = tgl_lahir
        self.jenis_kelamin = jenis_kelamin
        self.status = status
        self.profesi = profesi
        self.alamat = alamat
        self.keterangan = keterangan