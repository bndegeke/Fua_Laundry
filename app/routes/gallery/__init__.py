from flask import Blueprint,render_template



gallery = Blueprint('gallery',__name__ ,url_prefix='/gallery')


@gallery.route('/')
def index():
    return render_template('GALLERY/MAMAFUA_GALLERY.html')
