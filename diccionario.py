meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY":"aterrador,siniestro",
            "ROFL":"una respuesta a una broma",
            "SHEESH":"ligera desaprobacion",
            "AGGRO":"ponerse agresivo o enojado",
            "PIOLA":"TRANQUILO FRESCO O RELAJADO",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
            
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("pus no esta q pena")
