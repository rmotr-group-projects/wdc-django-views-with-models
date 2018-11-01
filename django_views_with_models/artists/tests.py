from django.test import TestCase


class TasksTestCase(TestCase):

    def test_task_1(self):
        """Should return proper template while GETing to /artists URL"""
        response = self.client.get('/artists/')
        assert response.status_code == 200
        assert "Here's a list of artists" in str(response.content)
