import re
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person

        fields = [
            "id",
            "person_name",
            "mobile_number",
            "age",
            "city",
            "state",
            "post_code",
            "full_address",
            "created_at",
        ]

        read_only_fields = ["id", "created_at"]

    def validate_person_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Name is required.")

        if len(value) < 2:
            raise serializers.ValidationError(
                "Name must be at least 2 characters long."
            )

        if not re.fullmatch(r"[A-Za-z][A-Za-z '-]*", value):
            raise serializers.ValidationError(
                "Name can contain only letters, spaces, hyphens and apostrophes."
        )

        return value


    def validate_mobile_number(self, value):
        value = value.strip()

        if not re.fullmatch(r"\+?\d{10,15}", value):
            raise serializers.ValidationError(
                "Enter a valid mobile number (10-15 digits)."
            )

        return value


    def validate_city(self, value):
        value = value.strip()

        pattern = r"[A-Za-z][A-Za-z .'-]*"

        if len(value) < 2 or not re.fullmatch(pattern, value):
            raise serializers.ValidationError("Enter a valid city name.")

        return value

    def validate_state(self, value):
        value = value.strip()

        pattern = r"[A-Za-z][A-Za-z .'-]*"

        if len(value) < 2 or not re.fullmatch(pattern, value):
            raise serializers.ValidationError("Enter a valid state name.")

        return value


    def validate_post_code(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Post code is required.")

        return value


    def validate_full_address(self, value):
        value = value.strip()

        
        if len(value) < 8:
            raise serializers.ValidationError("Address must be at least 8 characters.")

        if not re.search(r"[A-Za-z0-9]", value):
            raise serializers.ValidationError(
                "Address must contain letters or numbers."
            )

        if not re.search(r"[A-Za-z]", value):
            raise serializers.ValidationError(
                "Address must contain at least one letter."
            )


        if not re.fullmatch(r"[A-Za-z0-9 ,./#-]+", value):
            raise serializers.ValidationError("Address contains invalid characters.")

        return value


    def validate_age(self, value):

        if value <= 0:
            raise serializers.ValidationError("Age must be a positive number.")

        if value > 120:
            raise serializers.ValidationError("Age must be 120 or less.")

        return value


    def validate(self, attrs):

        required_fields = [
            "city",
            "state",
            "post_code",
            "full_address",
        ]

        for field in required_fields:

            value = attrs.get(field, "")

            if not str(value).strip():
                raise serializers.ValidationError({field: "This field is required."})

            attrs[field] = str(value).strip()

        return attrs
