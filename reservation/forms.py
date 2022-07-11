from .models import ReserveModel
from django.forms import ModelForm, TextInput, Select, DateInput, TimeInput, Textarea

class ReserveForm(ModelForm):
    class Meta:
        model = ReserveModel
        fields = ['name', 'email', 'phone', 'number_of_guests', 'date', 'time', 'message']
        widgets = {
            'name': TextInput(attrs={
                'name':'name',
                'type':'text',
                'id':'name',
                'placeholder':'Your Name*',
                'required':'',
            }),
            'email': TextInput(attrs={
                'name':'email',
                'type':'email',
                'id':'name',
                'placeholder':'Your Email Address',
                'required':'',
            }),
            'phone': TextInput(attrs={
                'name':'phone',
                'type':'text',
                'id':'phone',
                'placeholder':'Phone Number*',
                'required':'',
            }),
            'number_of_guests': Select(choices=ReserveModel.NUMBER_CHOICES),
            'date': DateInput(attrs={
                'class':'form-control',
                'placeholder':'yyyy-mm-dd',
            }),
            'time': TimeInput(attrs={
                'class':'form-control',
                'placeholder':'hh:mm',
            }),
            'message': Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Message',
                'name':'message',
                'rows':'6',
                'id':'message',
                'required':'',
                
                
            }),

            
        }