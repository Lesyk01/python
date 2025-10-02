from models import Antibiotic, Vitamin, Vaccine

def midicines(meds):
    for med in meds:
        print(med.info())
    

meds = [
    Antibiotic('Nurofen', 10, 15.3),
    Vitamin('Ascorbic acid', 120, 135.3),
    Vaccine('flu vaccine', 10, 10.0)
]
midicines(meds)