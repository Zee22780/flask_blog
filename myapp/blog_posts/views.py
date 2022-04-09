from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.blog_posts.forms import BlogPostForm
from myapp.models import BlogPost

blog_posts = Blueprint('blog_posts', __name__)

@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
  form = BlogPostForm()
  if form.validate_on_submit():
    blog_post = BlogPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
    db.session.add(blog_post)
    db.session.commit()
    flash('Blog Post Created')
    print('Blog post was created')
    return redirect(url_for('core.index'))
  return render_template('create_post.html', form=form)
