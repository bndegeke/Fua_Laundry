from flask import Blueprint , render_template,flash,abort,redirect,url_for
from .forms import BookingForm
from app.models import Booking , db
from flask_login import current_user , login_required


booking = Blueprint('booking' , __name__ , url_prefix='/booking')



@booking.route("/",methods=['GET','POST'])
@login_required
def index():
	form  = BookingForm()
	data = Booking.query.filter_by(user_id = current_user.id).all()
	if form.validate_on_submit():
		booking = Booking(
					date = form.day.data,
				    type_laundry =form.laundry.data,
					payment = form.payment_mode.data,
				    location = form.location.data,
			    	user_id=current_user.id
			    )
		db.session.add(booking)
		db.session.commit()
		flash('Booked Successfully')
		return redirect(url_for('booking.index'))
	return render_template('booking/booking.html'  , form=form , data = data)