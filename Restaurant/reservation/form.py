
from django import forms

from reservation.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation

        fields = "__all__"