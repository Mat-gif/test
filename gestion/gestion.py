from datetime import datetime
import pandas as pd
import subprocess
import math

subprocess.run("clear", shell=True)

user_input = input("Creer un nouveau mois ? (O/n)")
cat = ["courses", "restaurants", "bar","transport", "autre"]

def check_input(x):
    if x.lower() == "o" : return True
    else : return False


def check_cat(x):
    if x not in cat : return True
    else : return False
    


if(check_input(user_input)):
    
    print()
    df_past = pd.read_csv("./data/data.csv")
    df_past.to_csv("./archive/"+df_past.at[0,"date"]+".csv", index=False)
    date_start = datetime.now().date()
    solde_start = float(input("le solde en début de mois :"))
    print()
    solde_start = solde_start+179.30+231-490-4.99-6.99-5.99-7.20-5.55-20.70-15
    data = {'date': [date_start], 'solde': [solde_start], "payment": [0], "catégorie": ["start"]}
    df = pd.DataFrame(data)
    print(df)
    print()
    df.to_csv("./data/data.csv", index=False)
else : 
    new_in = True
    while(new_in) :
        df = pd.read_csv("./data/data.csv")
        print(df)
        print()
        payment_input = float(input("somme dépensée : "))
        categorie_input = input("catégorie : "+str(cat)) 
        while check_cat(categorie_input):
            categorie_input = input("catégorie : "+str(cat)) 
        print()
        solde = float(df['solde'].iloc[-1])-payment_input
        nouvelle_ligne = pd.DataFrame({'date': [datetime.now().date()], 'solde': [solde], "payment": [payment_input], "catégorie": [categorie_input]})
        df = pd.concat([df, nouvelle_ligne], ignore_index=True)
        df.to_csv("./data/data.csv", index=False)
        print(df)
        print()
        
        

        for sous_cat in set(df["catégorie"]):
            if sous_cat != "start" : 
                lignes_selectionnees = df[df["catégorie"] == sous_cat]
                print(str(sous_cat)+" : "+str(lignes_selectionnees["payment"].sum()))

    
        print()
        user_input = input("Nouvelle saisie ? (O/n)")
        print()
        new_in = check_input(user_input)
    
     
    

