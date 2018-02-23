# How to get started developing the backend

```bash
cd backend
# create a virtualenv
python3 -m venv venv
# activate the virtualenv and set some env variables
. activate.sh
# install dependencies
pip3 install -r requirements.txt
# create the database
flask db upgrade
```

You can then run the server by:
```bash
flask run
```
Every time you start another shell and want to develop on the backend:

```bash
. activate.sh
```

If you modify database models, you will need to migrate and upgrade the database
```bash
flask db migrate
flask db upgrade
```
