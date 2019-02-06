from django import forms

from .models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = [
            'camera',
            'Gender',
            'Age',
            'image_name',
            'head_yaw',
            'head_pitch',
            'head_roll',
            'Timestamp'

        ]
