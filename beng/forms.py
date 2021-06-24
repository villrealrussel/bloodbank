from django.forms import ModelForm
from .models import blooddetails


class bloodForm(ModelForm):
	class Meta:
		model = blooddetails
		fields = '__all__'