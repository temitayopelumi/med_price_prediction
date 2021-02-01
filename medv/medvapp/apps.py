from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class MedvappConfig(AppConfig):
    name = 'medvapp'

def getPredictions(CHAS, RM, LOG_NOX, LOG_DIS,LOG_LSTAT):
    path = os.path.join(settings.MODELS, 'finalized_model.sav')
    with open(path, 'rb') as pickled:
       model = pickle.load(pickled)
    # model = pickle.load(open("finalized_model.sav", "rb"))

    path2 = os.path.join(settings.MODELS, 'scaler.sav')
    with open(path2, 'rb') as pickled:
        scaled  = pickle.load(pickled)
    # scaled = pickle.load(open("scaler.sav", "rb"))
    prediction = model.predict(scaled.fit_transform([[CHAS, RM, LOG_NOX, LOG_DIS,LOG_LSTAT]]))
    
    return ('The median value is', prediction)
