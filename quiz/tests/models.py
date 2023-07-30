from django.db import models

LEVELS = (
    ('Easy', 'Easy'),
    ('Hard', 'Hard'),
)

SUBJECTS = (
    ('Physics', 'Physics'),
    ('Math', 'Math'),
)

class Question(models.Model):
    level = models.CharField(max_length=300, choices=LEVELS, null=True, blank=True)
    subject = models.CharField(max_length=300, choices=SUBJECTS, null=True, blank=True)
    text = models.TextField(null=False, blank=False)
    answer = models.CharField(max_length=300, null=False, blank=False, help_text="Must be identical to answers added below")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='_question_answer', on_delete=models.CASCADE)
    text = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"