import logging as lg


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            lg.info(f"Instância única de {cls.__name__} criada")
        return instances[cls]

    return get_instance