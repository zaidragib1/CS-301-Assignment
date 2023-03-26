# Import necessary libraries
import unittest
from io import StringIO
from unittest.mock import patch

# Import the previous Python program
from cultural_destination import CulturalDestination, EmergingTalent

# Define a class for integration testing
class TestCulturalDestinationIntegration(unittest.TestCase):
    def setUp(self):
        self.destination = CulturalDestination("Indian Heritage Hub", "New Delhi, India", "A celebration of India's rich cultural heritage and a platform for emerging talents.")
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_talent_and_showcase_talents(self, mock_stdout):
        talent = EmergingTalent("Sitar Player", "A talented musician specializing in classical Indian music.")
        self.destination.add_talent(talent)
        self.destination.showcase_talents()
        self.assertEqual(mock_stdout.getvalue(), "Sitar Player: A talented musician specializing in classical Indian music.\n")
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_digital_platform_and_showcase_platforms(self, mock_stdout):
        talent = EmergingTalent("Sitar Player", "A talented musician specializing in classical Indian music.")
        talent.add_digital_platform("YouTube")
        talent.showcase_platforms()
        self.assertEqual(mock_stdout.getvalue(), "YouTube\n")
        
# Run the tests
if __name__ == '__main__':
    unittest.main()
