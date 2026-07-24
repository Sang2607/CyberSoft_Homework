import pandas as pd
from Common.Decorator import handle_exception

@handle_exception
def checkDataFrame(value):
    return isinstance(value, pd.DataFrame)
