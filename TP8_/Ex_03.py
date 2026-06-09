from collections import ChainMap

config_default={"theme":"clair","langue":"fr"}

config_user={"theme":"sombre"}

config=ChainMap(config_user, config_default)

print(dict(config))

print(config["theme"])
print(config["langue"])

#theme vaut sombre car config_user est prioritaire

config_user["volume"]=80

print(dict(config))