from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Enrollment, Student
from .serializers import CourseSerializer, EnrollmentSerializer, StudentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action


"""class CourseListView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    
class CourseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        course = self.get_object(pk)

        if course is None:
            return Response(
                {"error": "Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        course.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        """

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):
        # Get the current course
        course = self.get_object()

        # Get all enrollments for this course
        enrollments = course.enrollment_set.all()

        # Extract students
        students = [enrollment.student for enrollment in enrollments]

        # Convert to JSON
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    @action(detail=True, methods=["get"])
    def courses(self, request, pk=None):
        student = self.get_object()

        enrollments = student.enrollment_set.all()

        courses = [e.course for e in enrollments]

        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer