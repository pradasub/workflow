def describe():
    return print(
        f'These are commands for inbuilt functions in pandas to describe data\n'
        f'Run each of them given below one by one for exploratory analysis\n'
        f'data.describe()\n'
        f'data.info() -> Dont forget to check the types of variables\n'
        f'data.corr()\n'f'data.dtypes\n'
        f'data.select_dtypes(include=["object"]).describe()\n'
        f'data.select_dtypes(include=["int64"]).describe()\n'
        f'data.select_dtypes(include=["float64"]).describe()\n'
        f'data.select_dtypes(include=["int64, float64"]).describe()\n'
        f'data.shape\n'
        f'data.shape[0]\n'
        f'data.shape[1]\n'
        f'data.size\n'
        f'data.index\n'
        f'data.index.values\n'
        f'data.index.tolist()\n'
    )