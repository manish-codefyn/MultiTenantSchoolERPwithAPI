from rest_framework import serializers
from apps.library.models import *

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = '__all__'

class BookIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = '__all__'

class FinePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinePayment
        fields = '__all__'

class LibraryMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryMember
        fields = '__all__'

class LibraryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryReport
        fields = '__all__'

