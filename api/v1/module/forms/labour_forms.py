from django import forms
from labour.models import Labour , LabourReview

# Creating a ModelForm
class LabourForm(forms.ModelForm):
    class Meta:
        model = Labour
        fields = "__all__"

# Creating a ModelForm
class LabourReviewForm(forms.ModelForm):
    class Meta:
        model = LabourReview
        fields = "__all__"