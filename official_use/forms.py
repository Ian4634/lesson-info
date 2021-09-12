from django import forms
from django.forms import ModelForm 
from .models import Lesson, Category

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = (
            'name',
            'category',
            'location',
            'start_time',
            'end_time',
            'eligibility',
            'link',
            'discription',
            'image'
        ) # 家東西進去
        widgets = {
            'start_time':forms.DateTimeInput(attrs= {'type':'datetime-local'}),
            'end_time':forms.DateTimeInput(attrs= {'type':'datetime-local'}),
        }
    category = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'discription',
            'image'
        )
    