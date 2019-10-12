from django import forms
from reg.models import Student,Teacher, Institute
from django import forms
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherForm(forms.Form):
    name = forms.CharField(label='Teachers Name', max_length=100)
    email = forms.CharField(label='Teachers Email', max_length=100)
    subject = forms.CharField(label='Teachers Subject', max_length=100)

class TeacherFormM(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class InstituteFormC(forms.Form):
    name = forms.CharField(label='Institute Name', max_length=100)
    email = forms.CharField(label='Institute Email', max_length=100)
    website = forms.CharField(label='Institute Website', max_length=100)


class InstituteFormM(forms.ModelForm):
    class Meta:
        model = Institute
        fields = "__all__"