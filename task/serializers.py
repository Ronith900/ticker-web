from rest_framework import serializers
from .models import TaskLabel, Task


class RESTHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)
    updated_by = serializers.SerializerMethodField(read_only=True)

    # permissions = SerializerMethodField()

    class Meta:
        extra_kwargs = {
            'created_by': {'lookup_field': 'username'},
            'updated_by': {'lookup_field': 'username'}
        }
        audit_fields = ('created_time', 'update_time', 'created_by', 'updated_by')
        fields = '__all__'

    @staticmethod
    def get_created_by(instance):
        if instance.created_by is None:
            return None
        return instance.created_by.username

    @staticmethod
    def get_updated_by(instance):
        if instance.created_by is None:
            return None
        return instance.created_by.username

class TaskLabelSerializer(RESTHyperlinkedModelSerializer):

    class Meta(RESTHyperlinkedModelSerializer.Meta):
        model = TaskLabel
        fields = ('url','label') + RESTHyperlinkedModelSerializer.Meta.audit_fields


class TaskSerializer(RESTHyperlinkedModelSerializer):
    class Meta(RESTHyperlinkedModelSerializer.Meta):
        model = Task
        fields = ('url','id','name','label','completed') + RESTHyperlinkedModelSerializer.Meta.audit_fields