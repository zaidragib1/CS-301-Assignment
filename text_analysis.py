# Import necessary libraries
import unittest
from cultural_destination import CulturalDestination, EmergingTalent

# Define a class for Text Analysis testing
class TestCulturalDestinationTextAnalysis(unittest.TestCase):
    def test_destination_description(self):
        destination = CulturalDestination("Indian Heritage Hub", "New Delhi, India", "A celebration of India's rich cultural heritage and a platform for emerging talents.")
        description = destination.get_description()
        self.assertIsInstance(description, str)
        self.assertGreater(len(description), 0)
        
    def test_talent_description(self):
        talent = EmergingTalent("Sitar Player", "A talented musician specializing in classical Indian music.")
        description = talent.get_description()
        self.assertIsInstance(description, str)
        self.assertGreater(len(description), 0)
        
# Run the tests
if __name__ == '__main__':
    unittest.main()
