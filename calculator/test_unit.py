from django.test import Client, TestCase
from django.http import HttpResponse, HttpRequest
import requests
from .views import submitquery
from django.urls import reverse
from calculator.models import Numeric_fields

# Create your tests here.      

class QuestionModelTests(TestCase):

        def setUp(self):
                Numeric_fields.objects.create(inp_number1 = 5, inp_number2 = 6, operation_text="add")
                Numeric_fields.objects.create(inp_number1 = 5, inp_number2 = 6, operation_text="sub")
                Numeric_fields.objects.create(inp_number1 = 5, inp_number2 = 6, operation_text="mul")
                Numeric_fields.objects.create(inp_number1 = 5, inp_number2 = 6, operation_text="div")
                Numeric_fields.objects.create(inp_number1 = 5, inp_number2 = 6, operation_text="")

        def test_addm(self):
                n1 = 5
                n2 = 6
                result = str(n1 + n2)
                add_nums = Numeric_fields.objects.get(operation_text="add")
                self.assertEqual(add_nums.__str__(), result)
        
        def test_subm(self):
                n1 = 5
                n2 = 6
                result = str(n1 - n2)
                sub_nums = Numeric_fields.objects.get(operation_text="sub")
                self.assertEqual(sub_nums.__str__(), result)

        def test_mulm(self):
                n1 = 5
                n2 = 6
                result = str(n1 * n2)
                # mul_nums = Numeric_fields(inp_number1 = n1, inp_number2 = n2, operation_text="mul")
                mul_nums = Numeric_fields.objects.get(operation_text="mul")
                self.assertEqual(mul_nums.__str__(), result)

        def test_divm(self):
                n1 = 5
                n2 = 6
                result = str(n1 / n2)
                # div_nums = Numeric_fields(inp_number1 = n1, inp_number2 = n2, operation_text="div")
                div_nums = Numeric_fields.objects.get(operation_text="div")
                self.assertEqual(div_nums.__str__(), result)
        
        def test_div_by_zerom(self):
                n1 = 5
                n2 = 0
                result = "Exception"
                div_nums1 = Numeric_fields(inp_number1 = n1, inp_number2 = n2, operation_text="div")
                self.assertEqual(div_nums1.__str__(), result)

        def test_invalidm(self):
                n1 = 5
                n2 = 6
                result = "Invalid"
                # inv_nums = Numeric_fields(inp_number1 = n1, inp_number2 = n2, operation_text="")
                inv_nums = Numeric_fields.objects.get(operation_text="")
                self.assertEqual(inv_nums.__str__(), result)

class QuestionViewTests(TestCase):

        def test_index(self):
                response = self.client.get('/calculator')
                self.assertEqual(response.status_code, 200)

        def test_add(self):
                client = Client()
                response = self.client.post(reverse('submitquery'),data={'numb1': '1', 'numb2': '2', 'add_nums': True})
                r_return = int(response.context['r_result'])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(r_return, 3)

        def test_sub(self):
                client = Client()
                response = self.client.post(reverse('submitquery'),data={'numb1': '2', 'numb2': '1', 'sub_nums': True})
                r_return = int(response.context['r_result'])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(r_return, 1)
        
        def test_mul(self):
                client = Client()
                response = self.client.post(reverse('submitquery'),data={'numb1': '1', 'numb2': '2', 'mul_nums': True})
                r_return = int(response.context['r_result'])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(r_return, 2)
        
        def test_div(self):
                client = Client()
                response = self.client.post(reverse('submitquery'),data={'numb1': '1', 'numb2': '2', 'div_nums': True})
                r_return = float(response.context['r_result'])
                self.assertEqual(response.status_code, 200)
                self.assertEqual(r_return, 0.5)
                
        def test_div_by_zero(self):
                client = Client()
                response = self.client.post(reverse('submitquery'),data={'numb1': '1', 'numb2': '0', 'div_nums': True})
                r_return = response.context['r_result']
                self.assertEqual(response.status_code, 200)
                self.assertEqual(r_return, "Bad Request")
        
        def test_empty(self):
                client = Client()
                response = self.client.post(reverse('submitquery'),data={'numb1': '', 'numb2': '10', 'add_nums': True})
                r_return = response.context['r_result']
                self.assertEqual(response.status_code, 200)
                self.assertEqual(r_return, "Inputs cannot be Empty")
        


