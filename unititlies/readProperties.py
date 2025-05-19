import configparser

# Create a configuration parser object
config = configparser.ConfigParser()

# Read the configuration file
config.read("./Configuration/config.ini")

class ReadConfig:

    @staticmethod
    def get_application_url():
        """
        Retrieves the application base URL from the configuration file.

        Returns:
            str: The base URL of the application.
        """
        return config.get('COMMON', 'BaseURL', fallback=None)