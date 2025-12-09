# wildguard/routes/auth.py 

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from forms import LoginForm

auth = Blueprint('auth', __name__)

@auth.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    """Admin login page."""
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin.dashboard'))
        else:
            return redirect(url_for('pages.home'))
        
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.strip()).first()
        
        if user and user.check_password(form.password.data):
            if not user.is_admin:
                flash('Admin access only.', 'danger')
            else:
                login_user(user)
                flash(f'Welcome back, {user.username}!', 'success')
                return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            
    return render_template('admin_login.html', title='Admin Login', form=form)


@auth.route("/logout")
@login_required
def logout():
    """Admin logout."""
    logout_user()
    flash('Logged out successfully!', 'info')
    return redirect(url_for('pages.home'))