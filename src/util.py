import yaml


def read_yaml(path):
    with open(path) as file:
        config = yaml.safe_load(file)

    return config