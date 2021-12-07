from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','first_name','last_name']




class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class WorkoutSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Workout
        fields = ['id','name','muscle','intesityLevel','description']
        # extra_kwargs = {
        #     'title': {'required': False, 'allow_null': True},
        #     'content': {'required': False, 'allow_null': True},
        #     'date_posted': {'required': False, 'allow_null': True},
        #     'author': {'required': False, 'allow_null': True},
        # }
