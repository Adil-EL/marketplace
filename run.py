from app.factory import create_app

import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.config['LAPTOPS_DB_URI'] = config['PROD']['LAPTOPS_DB_URI']
    app.config['LAPTOPS_DB_NAME'] = config['PROD']['LAPTOPS_DB_NAME']
    app.config['SECRET_KEY'] = config['PROD']['SECRET_KEY']

    app.run()