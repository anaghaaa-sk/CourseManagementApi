from rest_framework import serializers
from app.models import Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"








        
        #git init
        # git add .
        # git commit -m "message "
        #
        # git remote add origin "repositry"
        # git push -u origin brnchnme
        #