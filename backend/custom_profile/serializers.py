from rest_framework import serializers
from django_apps.custom_profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "is_student", "is_certified", "work_at",
                  "location", "school_type_students", "career_teachers")