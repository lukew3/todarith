from todarith import create_app
app = create_app()
app.app_context().push()
from todarith import db, create_app
db.create_all(app=create_app())

#ideally something here would create an anonymous user and a general topic
