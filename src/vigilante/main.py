import pandas as pd


def get_dataframe(path: str, sep: str=",") -> pd.DataFrame|str: 
    if path.endswith(".csv"):
        return pd.read_csv(path, sep=sep)
    if path.endswith(".xlsx"):
        return pd.read_excel(path, sep=sep)
    return "Path inválido!"


def get_numeric_fields(df: pd.DataFrame) -> pd.DataFrame:
    keys = df.keys()
    dict_types = {key: str(df.dtypes[key]) for key in keys}
    list_numeric_fields = [key for key, value in dict_types.items() if value in ["int64", "float64"]]
    return df[list_numeric_fields]


def generate_report(path: str, df_numeric_fields: pd.DataFrame, sep: str=","):
    """Gera um arquivo xlsx com duas planilhas, uma com o conteúdo numérico do csv, e a outra a análise quantitativa"""
    #TODO Pensar a respeito em como terminar isso
    get_dataframe(path=path, sep=sep)
