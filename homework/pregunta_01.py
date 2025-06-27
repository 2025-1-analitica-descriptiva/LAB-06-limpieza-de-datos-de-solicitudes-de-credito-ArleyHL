"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import pandas as pd
def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    data = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";").dropna()

    data["sexo"] = data["sexo"].str.lower()
    data["tipo_de_emprendimiento"] = data["tipo_de_emprendimiento"].str.lower()

    data["idea_negocio"] = (data["idea_negocio"].str.lower().str.replace("_", " ", regex=False).str.replace("-", " ", regex=False).str.strip())

    data["barrio"] = (data["barrio"].str.lower().str.replace("_", " ", regex=False).str.replace("-", " ", regex=False))

    def formatear_fecha(fecha):
        return f"{fecha[8:10]}/{fecha[5:7]}/{fecha[0:4]}" if fecha[0:4].isdigit() else fecha

    data["fecha_de_beneficio"] = data["fecha_de_beneficio"].apply(formatear_fecha)

    data["monto_del_credito"] = (data["monto_del_credito"]
        .str.replace(" ", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    data["línea_credito"] = (data["línea_credito"].str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    data_clear = data.drop_duplicates(subset=[
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "comuna_ciudadano",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ])

    os.makedirs(os.path.dirname("files/output/solicitudes_de_credito.csv"), exist_ok=True)
    data_clear.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

if __name__ == "__main__":
    pregunta_01()