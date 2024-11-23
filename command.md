install venv
.\venv\Scripts\activate
pip install setuptools wheel
pip install -r requirements.txt
python odoo-bin -r odooUser -w admin --addons-path=addons,modules -d DB
