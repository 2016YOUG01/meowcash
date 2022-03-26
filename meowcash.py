import os, time, shutil, logging
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            print(d)
            listdirs(d)
        
def send():
    clear()
    t = input('<username> ')
    path = 'meowbase/' + t
    #print(path) # debug
    if os.path.exists(path):
        spath = path
        ipwd = input('<password> ')
        mpwd = open(path+'/password.txt', 'r').read()
        #print(path+'/password.txt') #debug
        if ipwd == mpwd:
            t = input('<recipient> ')
            path = 'meowbase/' + t
            #print(path) #debug
            if os.path.exists(path):
                rpath = path
                a = int(input('<amount> '))
                clear()
                print('meowcash comfirmation\n')
                print('sender: ' + spath)
                print('recipient: ' + rpath)
                sba = int(int(open(spath+'/balance.txt', 'r').read()) - int(a))
                sba = str(sba)
                rba = int(int(open(rpath+'/balance.txt', 'r').read()) + int(a))
                rba = str(rba)
                print('your balance after transaction: ' + sba + 'meowcash')
                print('recipient balance before transaction: ' + rba + 'meowcash')
                t = input('\ncontinue? <N/y>')
                if t == 'y':
                    sb = int(int(open(spath+'/balance.txt', 'r').read()) - int(a))
                    print(int(open(spath+'/balance.txt', 'r').read()) - int(a))
                    if sb < 0:
                        print('Insufficient funds.')
                        input()
                        menu()
                    else:
                        rb = int(open(rpath+'/balance.txt', 'r').read()) + int(a)
                        open(rpath+'/balance.txt', 'w').write(str(rb))
                        open(spath+'/balance.txt', 'w').write(str(sb))
                        print('Funds sent.\n')
                        t = input('<MENU/send>')
                        if t == 'menu':
                            menu()
                        else:
                            send()    
                else:
                    print('\ntranscation cancelled.')
                    t = input('<SEND/menu>')
                    if t == 'menu':
                        menu()
                    else:
                        send()
            else:
                print('cant find user [' + t + '].\n')
                t = input('<SEND/menu>')
                if t == 'menu':
                    menu()
                else:
                    send()
        else:
            print('ar yu a haxor?\n')
            t = input('<SEND/menu>')
            if t == 'menu':
                menu()
            else:
                send()
    else:
        print('cant find user [' + t + '].\n')
        t = input('<SEND/menu>')
        if t == 'menu':
            menu()
        else:
            send()
        
def balance():
    clear()
    t = input('<username> ')
    path = 'meowbase/' + t
    #print(path) # debug
    if os.path.exists(path):
        b = open(path+'/balance.txt', 'r').read()
        print('balance: ' + b + 'meowcash')
        input()
        menu()
    else:
        print('cant find user [' + t + '].')
        t = input('<BALANCE/menu>')
        if t == 'menu':
            menu()
        else:
            balance()
        
def userlist():
    clear()
    print('meowcash userlist\n\n')
    rootdir = 'meowbase'
    listdirs(rootdir)
    input('\n')
    menu()
    
def useradd():
    clear()
    u = input('<username> ')
    shutil.copytree('meowbase/.template', 'meowbase/'+u)
    ipwd = input('<password> ')
    open('meowbase/'+u+'/password.txt', 'w').write(ipwd)
    print('user created.')
    input()
    menu()
    
def userdel():
    clear()
    iusr = input('<username> ')
    path = 'meowbase/' + iusr
    ipwd = input('<password> ')
    mpwd = open(path+'/password.txt', 'r').read()
    #print(path+'/password.txt') #debug
    if ipwd == mpwd:
        shutil.rmtree(path)
        print('user deleted.')
        input()
        menu()
    else:
        print('why are you trying to delete other people\'s accounts?')
        input()
        menu()

def menu():
    clear()
    print('meowteor\n\n[send] [balance] [userlist] [useradd] [userdel] [exit]')
    i = input('> ')
    if i == 'send':
        send()
    elif i == 'balance':
        balance()
    elif i == 'userlist':
        userlist()
    elif i == 'useradd':
        useradd()
    elif i == 'userdel':
        userdel()
    elif i == 'exit':
        exit()
    else:
        menu()    
    
menu()