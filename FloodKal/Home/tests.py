import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Map
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_map(**kwargs):
    defaults = {}
    defaults["LocName"] = "LocName"
    defaults.update(**kwargs)
    return Map.objects.create(**defaults)


class MapViewTest(unittest.TestCase):
    '''
    Tests for Map
    '''
    def setUp(self):
        self.client = Client()

    def test_list_map(self):
        url = reverse('Home_map_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_map(self):
        url = reverse('Home_map_create')
        data = {
            "LocName": "LocName",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_map(self):
        map = create_map()
        url = reverse('Home_map_detail', args=[map.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_map(self):
        map = create_map()
        data = {
            "LocName": "LocName",
        }
        url = reverse('Home_map_update', args=[map.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


