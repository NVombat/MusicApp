from core.pagination import CustomPagination
from .aws import AWSFunctionsS3
from .models import MusicData

S3_Functions = AWSFunctionsS3()
Paginate = CustomPagination()
Music_Data = MusicData()
