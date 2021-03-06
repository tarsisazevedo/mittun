from django.db import models

from mittun.tests.utils import ModelTestCase
from mittun.sponsors.models import Sponsor, Category


class SponsorModelTestCase(ModelTestCase):

    def setUp(self):
        self.category = Category.objects.create(name_en_us='test')
        self.sponsor = Sponsor.objects.create(
            name='sponsor name',
            description_en_us='sponsor description',
            url='sponsorurl.com',
            category=self.category,
        )

    def tearDown(self):
        self.category.delete()
        self.sponsor.delete()

    def test_model_should_have_a_name_field(self):
        self.assertIsFieldPresent('name', Sponsor)

    def test_model_should_have_a_en_us_description(self):
        self.assertIsFieldPresent('description_en_us', Sponsor)

    def test_model_should_have_a_pt_br_description(self):
        self.assertIsFieldPresent('description_pt_br', Sponsor)

    def test_description_should_be_a_text_field(self):
        self.assertIsInstance(self.sponsor._meta._name_map['description_en_us'][0], models.TextField)

    def test_model_should_have_a_logo(self):
        self.assertIsFieldPresent('logo', Sponsor)

    def test_model_should_have_a_url(self):
        self.assertIsFieldPresent('url', Sponsor)

    def test_model_should_have_a_category(self):
        self.assertIsFieldPresent('category', Sponsor)

    def test_should_return_sponsor_name_when_called_by_unicode(self):
        self.assertEqual('sponsor name', unicode(self.sponsor))
