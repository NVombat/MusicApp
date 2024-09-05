from core.pagination import CustomPagination
from userprofile.models import UserData
from .issue_jwt import AdminTokenAuth
from mainapp.models import MusicData, Comments
from .models import AdminAuth

Admin_Token_Auth = AdminTokenAuth()
Paginate = CustomPagination()
Music_Data = MusicData()
Admin_Auth = AdminAuth()
User_Data = UserData()
Comments = Comments()
