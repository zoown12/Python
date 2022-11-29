class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if len(self.old_passwords)>0:
            return self.old_passwords[-1]
        else:
            return None

    def set_password(self, password):
        if password in self.old_passwords:
            print( "예전에 사용한 비밀번호")
        else:
            self.old_passwords.append(password)
            print( "잘 처리 되었습니다.")

    def is_correct(self, password):
        if self.old_passwords[-1] == password:
            return True
        else:
            return False

my = Password_manager()
my.set_password('123')
my.set_password('123')
my.set_password('242')
print(my.old_passwords)
print(my.get_password())
print(my.is_correct('123'))
if __name__ == '__main__' :
    password_manager = Password_manager()
