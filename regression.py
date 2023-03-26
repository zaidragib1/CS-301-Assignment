# Import necessary libraries
import unittest
from unittest.mock import MagicMock, patch

# Import the previous Python program
from cultural_destination import CulturalDestination, EmergingTalent

# Define a class for regression testing
class TestCulturalDestinationRegression(unittest.TestCase):
    def test_add_talent(self):
        destination = CulturalDestination("Indian Heritage Hub", "New Delhi, India", "A celebration of India's rich cultural heritage and a platform for emerging talents.")
        talent = EmergingTalent("Sitar Player", "A talented musician specializing in classical Indian music.")
        destination.add_talent(talent)
        self.assertIn(talent, destination.talents)
        
    def test_add_digital_platform(self):
        talent = EmergingTalent("Sitar Player", "A talented musician specializing in classical Indian music.")
        talent.add_digital_platform("YouTube")
        self.assertIn("YouTube", talent.platforms)
        
    @patch('builtins.input', MagicMock(return_value='1'))
    @patch('sys.stdout', new_callable=MagicMock)
    def test_show_menu_and_quit(self, mock_stdout):
        destination = CulturalDestination("Indian Heritage Hub", "New Delhi, India", "A celebration of India's rich cultural heritage and a platform for emerging talents.")
        destination.show_menu()
        self.assertTrue(mock_stdout.called)
        destination.show_menu()
        self.assertTrue(mock_stdout.called)
        
# Run the tests
if __name__ == '__main__':
    unittest.main()
