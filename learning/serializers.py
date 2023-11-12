from rest_framework import serializers

from learning.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('course', 'title', 'description', 'image', 'video_url')


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, source='lesson_set',)

    class Meta:
        model = Course
        fields = ('name', 'description', 'image', 'lesson_count', 'lessons')

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user', 'payment_date', 'course', 'lesson', 'amount', 'payment_method')
