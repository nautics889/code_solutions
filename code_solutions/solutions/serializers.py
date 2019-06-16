from rest_framework import serializers
from solutions.models import Solution, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('title', 'description')


class NestedTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'description')
        read_only_fields = ('title', 'description')


class SolutionSerializer(serializers.ModelSerializer):
    #topics = NestedTopicSerializer(many=True)

    class Meta:
        model = Solution
        fields = ('title', 'price', 'content', 'topics')


class SolutionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        depth = 1
        fields = ('title', 'price', 'topics')
