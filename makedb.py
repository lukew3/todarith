from todarith import create_app
app = create_app()
app.app_context().push()
from todarith import db, create_app
db.create_all(app=create_app())
