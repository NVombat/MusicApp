from dotenv import load_dotenv

load_dotenv()


class Base:
    def __init__(self) -> None:
        self.test_data = {
            "Date": "12-10-2020",
            "Name": "testuser",
            "Email": "test@gmail.com",
            "Filename": "test.wav",
            "File": "/home/nvombat/Desktop/Nikhill/Rap/Catatonic/Final Songs/No Oxygen/Recordings/Ricochet Rec8 Chorus.wav",
            "CloudFilename": "/tests/test/filename",
            "ObjectURL": "url_of_object.aws"
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
            "Message": "testmessage",
        }

        self.wrong_data = {
            "wrong_email": "wrong@gmail.com",
            "wrong_file": "wrong.csv",
        }
