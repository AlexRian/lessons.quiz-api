from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import QuestionSerializer
from .models import Question

class QuestionView(viewsets.ViewSet):

    @action(detail=False, methods=['post'], url_path='check-answer/(?P<question>\w+)')
    def check_answer(self, request, question=None):
        try:
            question = Question.objects.get(id=question)

            if request.POST.get('answer') in question.right_answers.split(','):
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        requested_level = request.GET.get('level')
        requested_subject = request.GET.get('subject')
        if requested_level and requested_subject:
            questions = Question.objects.filter(level=request.GET.get('level').capitalize(), subject=request.GET.get('subject').capitalize())
            serialized_questions = QuestionSerializer(questions, many=True)
            return Response(serialized_questions.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
