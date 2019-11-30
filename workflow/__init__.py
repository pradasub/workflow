import os
# Change the pathname of the init file if path changes
os.chdir('C:/Users/pz413sz/Documents/test_workflows/workflow')
list_all = [i[:-3] for i in os.listdir() if ".py" in i]
list_all.remove("__init__")

__all__ = list_all