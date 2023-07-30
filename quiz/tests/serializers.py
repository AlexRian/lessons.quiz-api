from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['text',]

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    def get_answers(self, obj):
        serialized_answers = AnswerSerializer(obj.get_question_answers(), many=True) 
        return serialized_answers.data
    
    class Meta:
        model = Question
        fields = ['id', 'level', 'subject', 'text', 'answers', 'type']

class CheckItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    result = serializers.BooleanField()