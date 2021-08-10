import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def create_user(db):
    user = User.objects.create_user(username='testuser2', email='test@mail.com', password='Test1234')
    return user


@pytest.fixture()
def create_user_db(db):
    return User.objects.create_user('testuser')


@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user

@pytest.fixture()
def new_user(db, new_user_factory):
    return new_user_factory(username='test_new_user', password='new1234Pass')

@pytest.fixture()
def new_user_staff(db, new_user_factory):
    return new_user_factory(username='test_staff_user', password='$taff1234Pass', is_staff=True)