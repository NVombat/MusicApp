from dotenv import load_dotenv

load_dotenv()


class Base:
    def __init__(self) -> None:
        self.test_data = {
            "Name": "testuser",
            "Email": "test@gmail.com",
            "Filename": "test.wav",
            "File": "/home/nvombat/Desktop/Nikhill/Rap/Catatonic/Final Songs/No Oxygen/Recordings/Ricochet Rec8 Chorus.wav",
        }

        self.incomplete_data = {
            "Name": "testuser",
            "Filename": "test.wav",
        }

        self.contact_us_data = {
            "Name": "testuser",
            "Email": "test@gmail.com",
            "Message": "testmessage",
        }

        self.wrong_contact_us_data = {
            "Name": "wronguser",
            "Email": "wrong@gmail.com",
            "Message": "testmessage",
        }
