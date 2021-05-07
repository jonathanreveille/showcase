from django import forms

class SearchedPostForm(forms.Form):
    query_search = forms.CharField(label="",max_length=255)