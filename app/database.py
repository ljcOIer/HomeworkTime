# database.py - 导入数据
import data_tool as o


SUBJECT = {
    "chinese":"语文",
    "maths":"数学",
    "english":"英语",
    "physics":"物理",
    "history":"历史",
    "chemistry":"化学",
    "biology":"生物",
    "politics":"政治",
    "geography":"地理",
    "other":"其他",
}


user = o.s("user")
SchoolList = o.s("SchoolList")
classwork = o.s("classWork")

def verify_cookies(cookies):
    username = cookies.get('username')
    pass_str = cookies.get('pass_str')
    identity = cookies.get('identity')
    school = cookies.get('school')
    # return user.value
    if not username or not pass_str or not identity or not school:
        return False
    if school not in user.value:
        return False
    if identity not in user.value[school]:
        return False
    if username not in user.value[school][identity]:
        return False
    if o.encrypt(user.value[school][identity][username]['password']) != pass_str:
        return False
    return True

def get_identity(cookies):
    if cookies.get('identity')=='teacher':
        return 1
    if cookies.get('identity')=='principal':
        return 2
    return 0