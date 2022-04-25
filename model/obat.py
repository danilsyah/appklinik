from app import app, db

class Obat(db.Model):
    __tablename__ = 'obat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_obat = db.Column(db.String(150))
    jenis_obat = db.Column(db.String(150))
    harga_beli = db.Column(db.Integer)
    harga_jual = db.Column(db.Integer)
    suplier_id = db.Column(db.Integer, db.ForeignKey('suplier.id'))
    
    def __init__(self, nama_obat, jenis_obat, harga_beli, harga_jual, suplier_id):
        self.nama_obat = nama_obat
        self.jenis_obat = jenis_obat
        self.harga_beli = harga_beli
        self.harga_jual = harga_jual
        self.suplier_id = suplier_id