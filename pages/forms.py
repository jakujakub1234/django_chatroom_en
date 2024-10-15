from django import forms
from .models import Nicks

class HomeForm(forms.Form):
    nick = forms.CharField(label="Enter your nickname:", max_length=100, required=False, widget=forms.TextInput(attrs={"class": "form-input"}))
    
    key_from_qualtrics = forms.CharField(
        label="Enter your Qualtrics key:",
        max_length=100,
        error_messages={'required': 'your custom error message'},
        widget=forms.TextInput(attrs={"class": "form-input"})
    )

    is_positive_manipulation = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    def clean_key_from_qualtrics(self):
        key_from_qualtrics = self.cleaned_data['key_from_qualtrics']
        is_positive_manipulation = self.data['is_positive_manipulation']

        key_from_qualtrics = key_from_qualtrics[:-2]

        control_number = key_from_qualtrics[-5:]

        if control_number != "76392" and control_number != "76393":
            self._errors["key_from_qualtrics"] = ["The key is incorrect, please enter a valid key."]

        if control_number == "76392":
            self.data = self.data.copy()
            self.data['is_positive_manipulation'] = "True"
        elif control_number == "76393":
            self.data = self.data.copy()
            self.data['is_positive_manipulation'] = "False"
        else:
            self._errors["key_from_qualtrics"] = ["The key is incorrect, please enter a valid key."]

        key_from_qualtrics = key_from_qualtrics[:-5]

        # TODO wylaczone zabezpieczenie

        # TODO wylaczenie bazy
        #is_key_in_db = Nicks.objects.filter(qualtrics_id=key_from_qualtrics).first()
        #if is_key_in_db != None:
        #    self._errors["key_from_qualtrics"] = ["Klucz z Qualtricsa został już wcześniej użyty - w badaniu można wziąć udział tylko raz"]

        return key_from_qualtrics