import numpy as np
import pickle

svc, le, all_symptoms = pickle.load(open('models/svc.pkl', 'rb'))

def predict_from_symptoms(symptom_list):
    formatted_syms = [s.strip().replace(' ', '_').lower() for s in symptom_list]
    input_vector = np.array([1 if s in formatted_syms else 0 for s in all_symptoms])
    pred_idx = svc.predict([input_vector])[0]
    return le.inverse_transform([pred_idx])[0]
