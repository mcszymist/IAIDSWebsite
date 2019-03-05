from django.test import TestCase
from createAccount.models import MyUserManager, MyUser

# Create your tests here.
class createUserTestCase(TestCase):
    def setUp(self):
        MyUserManager.objects.create_user(user__email="the@gmail.com", 
            user__first_name="jim",
            user__last_name="samson",
            user__date_of_birth="2000-10-10")

    def test_createUser(self):
        user = MyUser.objects.create_user.get(user__email="the@gmail.com")
