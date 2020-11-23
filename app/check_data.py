def raise_err_cls(data_type):
    if data_type in ["int64", "O"]:
        pass
    else:
        raise Exception
def raise_err_reg(data_type):
    if data_type in ["int64", "float64"]:
        pass
    else:
        raise Exception

def check_data_type(model,data_type):
    """
    csvファイルのA列のデータ型と、modelを受け取り、
    正しい型かチェックする関数
    """
    if model == "regression":
        try:
            raise_err_reg(data_type)
        except Exception :
            return "abon"
    if model == "classification":
        try:
            raise_err_cls(data_type)
        except Exception :
            return "abon"