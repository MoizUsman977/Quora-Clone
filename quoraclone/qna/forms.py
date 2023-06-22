from django import forms
from qna.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]

class AnswerForm(forms.ModelForm):
    question_id = forms.IntegerField(widget=forms.HiddenInput() , required=False)
    answer_text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Answer Here'}) , required=True)

    class Meta:
        model = Answer
        fields = ["answer_text", "question_id"]
        