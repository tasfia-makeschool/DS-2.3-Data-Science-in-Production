from time import time
import firebase_admin
from firebase_admin import credentials, firestore

def config():
    cred = credentials.Certificate("./config.json")
    firebase_admin.initialize_app(cred)

def add_to_firestore(img, pred):
    db = firestore.client()
    doc_ref = db.collection(u'sampleData').document()
    doc_ref.set({
        u'image': img,
        u'prediction': str(pred),
        u'timestamp': firestore.SERVER_TIMESTAMP
    })
    print("Add to firebase success")
