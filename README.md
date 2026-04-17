# univ-flask-astro

Petit projet Flask sur l'astronomie, les appareils photo et les télescopes.

## Installation

1. Installer les dépendances :

```bash
pip install -r requirements.txt
```

2. Installer et configurer MySQL (MariaDB) :

```bash
sudo apt update
sudo apt install mariadb-server -y
sudo service mariadb start
sudo mysql_secure_installation
```

3. Créer la base de données :

```bash
sudo mysql -u root -p -e "CREATE DATABASE astro_db;"
```

4. Lancer l'application :

```bash
python app.py
```

5. Les données de démonstration sont chargées automatiquement au premier démarrage.

> Si vous voulez réinitialiser la base de données et recharger les exemples, supprimez la base et relancez `python populate.py`.

## Base de données

- L'application utilise MySQL (MariaDB) avec Flask-SQLAlchemy.
- URI par défaut : `mysql+pymysql://root:root@localhost/astro_db`

/!\ Attention à bien exporter vos données (schéma et données) avant de rendre votre code.
