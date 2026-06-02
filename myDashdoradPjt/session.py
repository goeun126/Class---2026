signInedMemberId = ''

# 보내는 기능(set)
def setsignInedMemberId(mId=''):
    global signInedMemberId
    signInedMemberId = mId

# 가지고 오는 기능(get)
def getsignInedMemberId():
    return signInedMemberId