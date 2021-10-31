from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Contract(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    contract_type = models.CharField(max_length=50)
    contract_date = models.DateField()
    contract_duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contract_type

class Document_type(models.Model):
    document_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_type

class Document(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    document_type = models.ForeignKey(Document_type, on_delete=models.CASCADE)
    document_number = models.CharField(max_length=50)
    document_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_number

class Permission_type(models.Model):
    permission_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.permission_type

class Permission(models.Model):
    employee = models.ManyToManyField(Employee)
    permission_type = models.ForeignKey(Permission_type, on_delete=models.CASCADE)
    permission_date = models.DateField()
    permission_duration = models.IntegerField()
    permission_status = models.IntegerField()

    def __str__(self):
        return self.permission_type

    