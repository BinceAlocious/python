from app1.models import Course,Batch,User,Register
from django import forms
class RegCourse(forms.ModelForm):
    class Meta():
        model=Course
        fields='__all__'
class RegBatch(forms.ModelForm):
    class Meta():
        model=Batch
        fields='__all__'
class RegUser(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
class NewUser(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'
    def clean(self):
        all_clean_data = super(NewUser,self).clean()
        email = all_clean_data["Email"]
        vmail = all_clean_data["Verify_Email"]
        print(email, vmail)
        if email != vmail:
            print("inside if")
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")
        return all_clean_data


