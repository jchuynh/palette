import server
import unittest
import doctest


class TestFlaskRoutes(unittest.TestCase):
    """Test Flask Routes"""

    def test_gallery(self):
        """Make sure gallery page returns correct HTML."""

        client = server.app.test_client()  # Create a test client

        # Use the test client to make requests
        result = client.get('/gallery')

        # Compare result.data with assert method
        self.assertIn(b'<h1>Welcome to Palette!</h1>', result.data)



    def test_search_form(self):
        """Make sure search-form page returns correct HTML."""

        # Create a test client
        client = server.app.test_client()

        # Use the test client to make requests
        result = client.get('/search-form')

        # Compare result.data with assert method
        self.assertIn(b'<h1>Search for Artworks</h1>', result.data)


    def test_upload(self):
        """Make sure upload page returns correct HTML."""

        # Create a test client
        client = server.app.test_client()

        # Use the test client to make requests
        result = client.get('/uplaod')

        # Compare result.data with assert method
        self.assertIn(b'<h1>Create your own color palette!</h1>', result.data)


if __name__ == '__main__':
    # If called like a script, run tests
    unittest.main() 












