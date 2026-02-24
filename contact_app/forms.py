from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(),
        max_length=100,
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'pt-2 text-xl'}),
        max_length=100,
    )
    message = forms.CharField(
        widget=forms.Textarea
    )



    def clean(self):
        cleaned_data = super().clean()

        if 'ciao' in self.cleaned_data['message'] and '@' not in self.cleaned_data['email']:
            raise forms.ValidationError('Nell\'email ci vuole la @ e non puoi scrivere ciao nel messaggio.')
        
        return cleaned_data
    

    def clean_name(self):
        if '@' in self.cleaned_data['name']:
            raise forms.ValidationError('La @ non è permessa nel nome.')
        
        return self.cleaned_data['name']
    

    def send_email(self):
        print(self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['message'])






    # def clean(self):
    #     cleaned_data = super().clean()

    #     if '@' not in self.cleaned_data['email']:
    #         raise forms.ValidationError('Nell\'email ci vuole la @')
        
    #     return cleaned_data

    # def send_email(self):
    #     print(f"Invio email da {self.cleaned_data['name']} dalla mail {self.cleaned_data['email']} con messaggio: {self.cleaned_data['message']}")
