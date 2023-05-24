# buatkan form dengan field dropdown stadium dan calendar
# untuk memilih stadium dan tanggal peminjaman
# ----------------------------------------------------------------------
from django import forms


class PeminjamanStadiumForm(forms.Form):
    stadium = forms.ChoiceField(
        label='Stadium',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Stadium',
            }
        )
    )
    tanggal = forms.DateField(
        label='Tanggal',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tanggal',
                'type': 'date',
            }
        )
    )