import io
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import QuestionSerializer, CheckItemSerializer
from .models import Question

class QuestionView(viewsets.ViewSet):

    parser_classes = [JSONParser]

    @action(detail=False, methods=['post'], url_path='check-answers')
    def check_answer(self, request):
        checks = request.data.get('answers')
        results = []
        
        for check in checks:
            check_answer = check.get('text')
            check_id = check.get('id')

            try:
                question = Question.objects.get(id=check_id)
                if isinstance(check_answer, list):
                    right_answers = 0
                    for answer in check_answer:
                        if str(answer) in question.right_answers.split(','):
                            right_answers += 1

                    result = {"id":check_id, "result": len(check_answer) == right_answers if True else False}
                    results.append(result)
                else:
                    if str(check_answer) in question.right_answers.split(','):
                        results.append({"id":check_id, "result": True})
                    else:
                        results.append({"id":check_id, "result": False})

            except ObjectDoesNotExist:
                results.append({"id":0, "result":False})
            
        checks_serializer = CheckItemSerializer(results, many=True)
        return Response(checks_serializer.data)

    def list(self, request):
        requested_level = request.GET.get('level')
        requested_subject = request.GET.get('subject')
        if requested_level and requested_subject:
            questions = Question.objects.filter(level=request.GET.get('level').capitalize(), subject=request.GET.get('subject').capitalize())
            serialized_questions = QuestionSerializer(questions, many=True)
            return Response(serialized_questions.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
