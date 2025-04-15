import yaml
from utils.logger import setup_logging
from core.database import connect_databases

def main():
    setup_logging()

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    xenforo = connect_databases(config)

    xenforo.close()

if __name__ == "__main__":
    main()