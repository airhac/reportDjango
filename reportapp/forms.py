from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.friends['username'].disabled = True
        #초기화 할때 username칸을 비활성화 해준다.
        #비밀번호만 바꿀수 있도록 해준다.
        #브라우저에서 고칠수 있지만 이런식으로 해놓으면 변경되지 않는다.
