from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTest(SimpleTestCase):
    """Test the home Page"""
    def test_url_exists_at_correct_location(self):
        """test url exists at correct location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """test url available by name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test template name is correct"""
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        """Test template content"""
        response=self.client.get(reverse("home"))
        self.assertContains(response, "<h1 class=\"mt-5\">Home</h1>")

class ProjectpageTest(SimpleTestCase):
    """Test the Project Page"""
    def test_url_exists_at_correct_location(self):
        """test url exists at correct location"""
        response = self.client.get("/project/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """test url available by name"""
        response = self.client.get(reverse("project"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test template name is correct"""
        response=self.client.get(reverse("project"))
        self.assertTemplateUsed(response, "project.html")

    def test_template_content(self):
        """Test template content"""
        response=self.client.get(reverse("project"))
        self.assertContains(response, "<h1 class=\"mt-5\">Projects I Have Worked On</h1>")

class ContactpageTest(SimpleTestCase):
    """Test the contact Page"""
    def test_url_exists_at_correct_location(self):
        """test url exists at correct location"""
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """test url available by name"""
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test template name is correct"""
        response=self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")

    def test_template_content(self):
        """Test template content"""
        response=self.client.get(reverse("contact"))
        self.assertContains(response, "<h1 class=\"mt-5\">Contact Me</h1>")