from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

# Create your models here.

class Numeric_fields(models.Model):
    inp_number1 = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    inp_number2 = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    # result = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$')])
    result = models.CharField(max_length=10)
    operation_text = models.CharField(max_length=3)
    def find_result(self): 
        if self.operation_text == "add":
            self.result = str(int(self.inp_number1) + int(self.inp_number2))
        elif self.operation_text == "sub":
            self.result = str(int(self.inp_number1) - int(self.inp_number2))
        elif self.operation_text == "mul":
            self.result = str(int(self.inp_number1) * int(self.inp_number2))
        elif self.operation_text == "div":
           if self.inp_number2 == 0:
            self.result = "Exception"
           else:
            self.result = str(int(self.inp_number1) / int(self.inp_number2))
        else:
            self.result = "Invalid"
        return self.result

    def __str__(self):
        # if self.operation_text == "add":
        #     self.result = str(int(self.inp_number1) + int(self.inp_number2))
        # elif self.operation_text == "sub":
        #     self.result = str(int(self.inp_number1) - int(self.inp_number2))
        # elif self.operation_text == "mul":
        #     self.result = str(int(self.inp_number1) * int(self.inp_number2))
        # elif self.operation_text == "div":
        #    if self.inp_number2 == 0:
        #     self.result = "Exception"
        #    else:
        #     self.result = str(int(self.inp_number1) / int(self.inp_number2))
        # else:
        #     self.result = "Invalid"
        return self.find_result()
    
# class Operation(models.Model):
#     numbers = models.ForeignKey(Numeric_fields, on_delete=models.CASCADE)
#     operation_text = models.CharField(max_length=1)
#     def __str__(self): 
#         return self.operation_text 

