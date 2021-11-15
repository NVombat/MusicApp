from dotenv import load_dotenv
import os

load_dotenv()

class Base:
    def __init__(self) -> None:
        self.test_data = {
            "Date": "15/10/2021, 16:30:00",
            "Name": "Nikhill Vombatkere",
            "Email": "nv9824@srmist.edu.in",
            "Filename": "test.wav",
            "CloudFilename": "tests/nv9824/test.wav",
            "ObjectURL": os.getenv("TEST_AWS_S3_OBJECT_URL_PREFIX") + "tests/nv9824/test.wav",
            "File": "/home/nvombat/Desktop/Nikhill/Rap/Catatonic/Final Songs/No Oxygen/Recordings/Ricochet Rec8 Chorus.wav",
        }

        self.wrong_data = {"wrong_file": "wrong.txt", "wrong_email": "wrong@test.com"}
