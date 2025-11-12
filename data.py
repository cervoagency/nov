import pandas as pd

# data -patente
test_df = {
    'Emplacement': ['Montreal','Toronto','Vancouver','Hamilton','Quebec',
            'Quebec city','Granby','Ottawa','Sainte Anne',
                    'Longueil','laval'],
    'montant': [17,17,13,18,13,14,13.50,25,15,15,12]
}

final_data = pd.DataFrame(test_df)