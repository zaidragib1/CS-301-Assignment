# Import necessary libraries
import random

# Define a class for the cultural destination
class CulturalDestination:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description
        self.talents = []
    
    def add_talent(self, talent):
        self.talents.append(talent)
    
    def showcase_talents(self):
        for talent in self.talents:
            print(talent.name + ": " + talent.description)

# Define a class for emerging talents
class EmergingTalent:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.digital_platforms = []
    
    def add_digital_platform(self, platform):
        self.digital_platforms.append(platform)
    
    def showcase_platforms(self):
        for platform in self.digital_platforms:
            print(platform)

# Create a new cultural destination
destination = CulturalDestination("Indian Heritage Hub", "New Delhi, India", "A celebration of India's rich cultural heritage and a platform for emerging talents.")

# Create some emerging talents
talent1 = EmergingTalent("Sitar Player", "A talented musician specializing in classical Indian music.")
talent1.add_digital_platform("YouTube")
talent1.add_digital_platform("Spotify")

talent2 = EmergingTalent("Kathak Dancer", "A skilled performer of the traditional Indian dance form.")
talent2.add_digital_platform("Instagram")
talent2.add_digital_platform("TikTok")

talent3 = EmergingTalent("Block Printer", "A master of the traditional Indian art of block printing.")
talent3.add_digital_platform("Etsy")
talent3.add_digital_platform("Amazon Handmade")

# Add the emerging talents to the cultural destination
destination.add_talent(talent1)
destination.add_talent(talent2)
destination.add_talent(talent3)

# Showcase the talents and digital platforms
destination.showcase_talents()
talent1.showcase_platforms()
talent2.showcase_platforms()
talent3.showcase_platforms()
