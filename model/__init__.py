from app import app, db
from model import user, dokter, obat, suplier, pendaftaran, pasien

db.create_all()

print("load model")