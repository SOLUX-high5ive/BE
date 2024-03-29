from django.contrib import admin
from .models import CustomUser


#admin 페이지에 User를 등록한다는 뜻
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
	#리스트에 보여지는 것
    list_display=(
        'user_id',
        'user_pw',
        'user_register_dttm'
    )
    
    
#+ 추가로 작성 후 DB에 반영하기 위해서는 아래 2줄 필수
#python3 manage.py makemigrations
#python3 manage.py migrate
