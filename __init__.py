import login
import topu

if __name__ == '__main__':
    schoolid = input('学校id:')
    number = input('学号:')
    password = input('密码:')
    puid = input("活动id:")
    login.login(schoolid=schoolid, number=number, password=password)  # choolid=学校id, number=学号, password=密码
    topu.topu(puid=puid)  # puid=活动id
