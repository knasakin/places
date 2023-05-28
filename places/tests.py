from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Place


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('Konstantin')
        self.client.force_login(user=self.user)

        self.list_url = reverse('places')
        self.add_url = reverse('add')
        self.place1 = Place.objects.create(
            name='SOCHI',
            location='SRID=4326;POINT (0.5806387423688333 -0.2772090313821412)',
            comment='ADLER',
            user=self.user
        )

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/places.html')

    def test_project_create_POST(self):
        data = {'name': 'MSK',
                'location': 'SRID=4326;POINT (0.5806387423688333 -0.2772090313821412)',
                'comment': 'CAP OF RUSSIA',
                'user': self.user}
        response = self.client.post(self.add_url, data)
        place1 = Place.objects.get(id=2)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(place1.name, 'MSK')
        self.assertEquals(place1.user, self.user)
