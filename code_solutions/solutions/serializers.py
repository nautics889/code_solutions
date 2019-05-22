from rest_framework import serializers
from solutions.models import Solution, Topic


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('title', 'price', 'content', )



class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('title', 'description')
