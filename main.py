import yaml


def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config


def main():
    config = load_config()

    db_host = config['client']['host']
    db_port = config['client']['port']

    print(f" {db_host}:{db_port}")


if __name__ == '__main__':
    main()
