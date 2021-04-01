<h1 align="center">
    🍔 Foodfy MVC application
</h1>

## 📌 Content

- [About](#-about)
- [Technology](#-technology)
- [Installation and Configuration](#installation-and-configuration)
   - [Virtual environment](#virtual-environment)
   - [Database](#database)
   - [Installation of Dependencies](#installation-of-dependencies)
   - [Flask Env](#flask-env)
- [Running the Application](#gear-running-the-application)
- [Issues](#-issues)
- [Contribution](#-contribution)
- [License](#balance_scale-license)

## 🚀 About

This repository contains the source code of the Foodfy recipe management system. The technologies used are described in Technology. This project is still under development and can be consulted [here](https://github.com/fredsonchaves07/foodfy/projects/1)


## 💻 Technology

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [pip](https://pypi.org/project/pip/)
- [Wtforms](https://wtforms.readthedocs.io/en/2.3.x/)
- [Dynaconf](https://www.dynaconf.com/)
- [Postgres](https://www.postgresql.org/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## 🛠️ Installation and Configuration

To execute the project in a development environment, it is necessary to have the tools installed. Can be consulted in the technology section

### Virtual environment

It is recommended to create a [virtual development environment](https://docs.python.org/3/library/venv.html)


### Database

Required has the most updated version of [postgres] (https://www.postgresql.org/). Change the `SQLALCHEMY_DATABASE_URI` variable in the `settings.toml` configuration file

```toml
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/foodfydb'
```

### Installation of Dependencies

Run the command to perform the dependency installation

```bash
pip install -r requirements.txt
```

### Flask Env

It is necessary to configure the flask environment variables with the values `FLASK_ENV='development'` e `FLASK_APP=app/app.py`


## :gear: Running the Application

Run Application in development mode after installation and configuration

```bash
flask run
```

## 🐛 Issues

I would love to review your pull request! Open a new [issue](https://github.com/fredsonchaves07/foodfy/issues)

## 🤝 Contribution

Feel free to contribute to the project. I am open for suggestions. Click [here](https://github.com/fredsonchaves07/christmas-letter-api/issues) to open a new issue or take part in the development [project](https://github.com/fredsonchaves07/foodfy/projects/1) :smile:

## :balance_scale: License

This project uses MIT License. Click [here](https://github.com/fredsonchaves07/foodfy/blob/main/LICENSE) to access


---
Developed :blue_heart: by  Fredson Chaves