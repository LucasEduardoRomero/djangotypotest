from rest_framework import serializers

from django_typomatic import ts_interface, generate_ts

from main.models import Task


@ts_interface()
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'title', 'description', 'deadline', 'is_completed']


generate_ts('./main/types.ts')
