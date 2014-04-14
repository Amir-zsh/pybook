#!/usr/bin/python
# Filename: mail_validity.py
def valid_mail(mail):
    a='@%^()+=<>?:;"`~[]{}/,'
    b='@%^()+=<>?:;".!#$&*0987654321`~[]{}/'
    t=True
    while True:
        if mail.find('@')==-1 or mail.find('@')==0:
            t=False
            break
        elif mail.find('.')==-1 or mail.find('.')==0:
            t=False
            break
        elif mail.find('@'):
            if mail[mail.find('@')-1]=='.' or mail[mail.find('@')+1]=='.':
                t=False
                break
            if (mail[:mail.find('@')]).count(".")>1:
                t=False
                break
            for i in range(mail.find('@')):
                if mail[i] in a:
                    t=False
                    break
            if (mail[mail.find('@')+1:]).count(".")>2:
                t=False
                break
            for i in range(mail.find('@')+1,mail.find('.',mail.find('@')+1)):
                if mail[i] in b:
                    t=False
                    break
            if mail.find('@',mail.find('@')+1)!=-1:
                t=False
                break
            j=mail[mail.rfind('.')+1:]
            if len(j)<2 or len(j)>4:
                t=False
                break
            for i in j:
                if i in b:
                    t=False
                    break
        break
    return t
# End of mail_validity.py
