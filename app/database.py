import data_tool as o

user = o.s("user")
SchoolListDATA = o.s("SchoolList")


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
