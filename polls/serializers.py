from dataclasses import fields
from rest_framework import serializers
from .models import Poll, Choice, Vote

class VoteSerializer(serializers.Modelserializers):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.Modelserializers):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'