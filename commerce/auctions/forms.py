

from django import forms


class CreateListing(forms.Form):
    title = forms.CharField(required=True, max_length=30, min_length=3, label="Title" , widget=forms.TextInput(attrs={'class': 'border border-gray-400 w-1/2 flex flex-wrap'}))
    description = forms.CharField(required=True, max_length=1200, min_length=100, label="Description" , widget=forms.TextInput(attrs={'class': 'border border-gray-400 w-1/2 flex flex-wrap'}))
    image = forms.CharField(required=False, label="Image link" , widget=forms.TextInput(attrs={'class': 'border border-gray-400 w-1/2 flex flex-wrap'}))
    starting_bid = forms.IntegerField(required=True, label="Starting price" , widget=forms.TextInput(attrs={'class': 'border border-gray-400 w-1/2 flex flex-wrap'}))

class BidForm(forms.Form):
    bid = forms.IntegerField( required = True, label = 'bid' ,widget=forms.TextInput(attrs={'class': 'border border-gray-400 w-1/2'}))

    def __init__(self, *args, **kwargs):
        min_value = kwargs.pop('min_value', None)
        super().__init__(*args, **kwargs)
        if min_value is not None:
            self.fields['bid'].widget.attrs['min'] = min_value
            