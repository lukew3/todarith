from flask import Blueprint, request, render_template
from todarith import db

post = Blueprint('post', __name__)

@app.route("/new", methods=['GET', 'POST'])
def newPost():
    form = EarnForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, description=form.description.data, photo=form.photo.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('explore'))
    return render_template('post/newpost.html', form=form)

@post.route('/edit')
def edit():
    return render_template('post/editpost.html')
