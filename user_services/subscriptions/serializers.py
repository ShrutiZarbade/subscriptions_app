from rest_framework import serializers
from .models import UserDetails

class DataValidator(serializers.Serializer):

    email = serializers.EmailField(
            max_length=255,
            required=True,
            allow_blank=False,
            error_messages={
                'invalid': 'Enter a valid email address.',
                'blank': 'This field may not be blank.',
            }
        )
    
    # is_subscribed = serializers.BooleanField(required=True)
    
    # def validate(self, data):
    #     if 'is_subscribed' not in data:
    #         data['is_subscribed'] = False  # Set default if not provided
    #     return data


# class DataValidator(serializers.Serializer):
#     """
#     Serializer for validating input data

#     """
#     attributes = UserSerializer(
#         # required=True,
#         error_messages={"required": "Mandatory input attributes is missing"},
#     )