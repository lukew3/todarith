from todarith import create_app
app = create_app()
app.app_context().push()
from todarith import db, create_app
db.create_all(app=create_app())

from todarith.models import Skill, User
User.create(
    username="Anonymous",
    pw_hash="a;sfap3rbijsapvnioc3npas3r",
    email="anonymous@maildrop.cc"
)
Skill.create(
    skillName="Math"
)
Skill.create(
    skillName="generated"
)
