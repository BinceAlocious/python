from django import forms
import re
def phvalidate(ph):
    x='[6-9][0-9]{9}'
    st=str(ph)
    match=re.fullmatch(x,st)
    if(match==None):
        raise forms.ValidationError("Error Phone No not Valid")
def agecalculate(ag):
    print("HAI")
    print(ag)
    print(type(ag))
    if(ag<18):
        print("Inside block")
        raise forms.ValidationError("Age Below 18")


class Stuform(forms.Form):
    nam=forms.CharField(max_length=150,label="Name")
    add=forms.CharField(label="Address")
    gen=forms.CharField(max_length=1,label="Gender")
    ag=forms.IntegerField(label="Age",validators=[agecalculate])
    em=forms.EmailField(label="Email")
    vem=forms.EmailField(label="Verify Email")
    ph=forms.IntegerField(label="Phone No.",validators=[phvalidate])
    def clean(self):
        all_clean_data=super(Stuform,self).clean()
        email=all_clean_data["em"]
        vmail=all_clean_data["vem"]
        print(email,vmail)
        if email != vmail:
            print("inside if")
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")
        return all_clean_data

