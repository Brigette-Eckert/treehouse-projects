from django import forms

from . import models


class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        # fields only includes fields lists
        fields = [
            'title',
            'description',
            'order',
            'total_questions'

        ]
        # exclude leaves off field - includes everything unless excluded
        # exclude = [
        #     'course',
        # ]


class TrueFalseQuestionForm(forms.ModelForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = ['order', 'prompt']


class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
                'order',
                'prompt',
                'shuffle_answers'
                  ]
