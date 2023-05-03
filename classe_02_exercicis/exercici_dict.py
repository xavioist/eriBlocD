"""ex_04-1: Fes una funció (top_student) que amb la fitxa (dic1, dic2, dic3) de tres alumnes i les notes dels dos últims parcials
retorni el nom del/a estudiant amb la millor mitjana.

    Returns:
        {"Alumne" : "Joanet", "NIU" : 1329902, "Nota 1": 8.5, "Nota 2" : 4.5},
        {"Alumne" : "Paula", "NIU" : 1429902, "Nota 1": 8.5, "Nota 2" : 8.5},
        {"Alumne" : "Genis", "NIU" : 1326302, "Nota 1": 5, "Nota 2" : 4} -> "Paula"
    """


dic1 = {"Alumne": "Joanet", "NIU": 1331616, "Nota_1": 8.5, "Nota_2": 4.5}
dic2 = {"Alumne": "Paula", "NIU": 1429902, "Nota_1": 7, "Nota_2": 8.5}
dic3 = {"Alumne": "Genis", "NIU": 1526302, "Nota_1": 5, "Nota_2": 4}


"""def top_student(dic1, dic2, dic3):
    hof = []
    init_val = 0
    list_of_dics = [dic1, dic2, dic3]
    for dic in list_of_dics:
        nota = (dic["Nota_1"] + dic["Nota_2"]) / 2
        if nota >= init_val:
            hof = [dic["Alumne"]]
            init_val = nota
    return hof[0]"""
