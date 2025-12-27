def get_disease_info(dis, description, precautions, medications, diets, workout):
    desc = " ".join(description[description['Disease'] == dis]['Description'])
    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.tolist()
    med = medications[medications['Disease'] == dis]['Medication'].tolist()
    die = diets[diets['Disease'] == dis]['Diet'].tolist()
    wrkout = workout[workout['disease'] == dis]['workout'].tolist()

    return desc, pre, med, die, wrkout


def get_severity_for_symptoms(symptom_list, severity_df):
    weights = []
    for symptom in symptom_list:
        sym_row = severity_df[severity_df['Symptom'].str.lower() == symptom.lower()]
        if not sym_row.empty:
            weights.append(sym_row['weight'].values[0])
    if weights:
        avg_weight = round(sum(weights) / len(weights), 2)
        return avg_weight
    else:
        return 'N/A'
