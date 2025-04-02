from django import forms
from material.models import *
# creating a form
class MatrialForm(forms.ModelForm):
    class Meta:
        model = Matrial
        fields = "__all__"
        
class MatrialReviewForm(forms.ModelForm):
    class Meta:
        model = MatrialReview
        fields = "__all__"