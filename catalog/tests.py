from django.test import TestCase
from .models import Category, Tag, Item

class ModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create categories
        cls.category1 = Category.objects.create(name="Electronics")
        cls.category2 = Category.objects.create(name="Appliances")

        # Create tags
        cls.tag1 = Tag.objects.create(name="Eco Friendly")
        cls.tag2 = Tag.objects.create(name="Battery Powered")

        # Create an item
        cls.item = Item.objects.create(
            title="Eco Battery Lamp",
            description="A lamp powered by eco-friendly batteries.",
            category=cls.category1,
            price=49.99
        )
        cls.item.tags.add(cls.tag1, cls.tag2)

    def test_category_slug_auto_generated(self):
        expected_slug1 = "electronics"
        expected_slug2 = "appliances"
        self.assertEqual(self.category1.slug, expected_slug1)
        self.assertEqual(self.category2.slug, expected_slug2)

    def test_tag_slug_auto_generated(self):
        expected_slug1 = "eco-friendly"
        expected_slug2 = "battery-powered"
        self.assertEqual(self.tag1.slug, expected_slug1)
        self.assertEqual(self.tag2.slug, expected_slug2)

    def test_item_tags_relationship(self):
        # Check if tags are assigned correctly
        tags = list(self.item.tags.all())
        self.assertIn(self.tag1, tags)
        self.assertIn(self.tag2, tags)
        self.assertEqual(len(tags), 2)

    def test_item_str(self):
        self.assertEqual(str(self.item), self.item.title)

    def test_category_str(self):
        self.assertEqual(str(self.category1), self.category1.name)

    def test_tag_str(self):
        self.assertEqual(str(self.tag1), self.tag1.name)
