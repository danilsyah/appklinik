from app import db
from model import dokter, user, obat, suplier, pendaftaran, pasien


db.create_all()
print("load model")