class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 765
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
