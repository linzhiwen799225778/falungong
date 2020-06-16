import MySQLdb
import random,string
conn=MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    db='test'
)
cursor=conn.cursor()
class Card:
    def __init__(self,password,state='1',money='0'):
        self.cardid1 = '622848356' + ''.join(random.sample(str(string.digits) * 10, 10))
        self.password =password
        self.state =state
        self.money =money
class Person:
    def __init__(self,name,phone,passport):
        self.name=name
        self.phone=phone
        self.passport=passport
class Option:
        # input("""
        # 欢迎来到ATM：(1)注册(2)查询(3)存钱(4)取钱(5)转账
        # (6)改密(7)锁卡(8)解卡(9)补卡(0)退出
        # """)
    #创造卡
    def creatcard(self,password,passport):
        self.card=Card(password)
        self.sql='insert into card(password,state,card,money) values(%s,%s,%s,%s)'
        cursor.execute(self.sql,(self.card.password,self.card.state,self.card.cardid1,'0'))
        conn.commit()
        self.sql2 = 'select id from card where card=%s'
        cursor.execute(self.sql2,(self.card.cardid1,))
        self.id=cursor.fetchone()[0]
        self.sqlp = 'update person set carid=%s where userid=%s'
        cursor.execute(self.sqlp,(self.id,passport))
        conn.commit()
    # 查询卡号
    def searchcard(self,userid):
        self.sqlsearch='select carid from person where userid=%s'
        cursor.execute(self.sqlsearch,(userid,))
        self.cardid=cursor.fetchone()[0]
        self.sqlcard = 'select card from card where id=%s'
        cursor.execute(self.sqlcard, (self.cardid,))
        return cursor.fetchone()[0]
    # 创造用户
    def creatperson(self,name,phone,passport):
        self.sql='insert into person(name,phone,userid) value(%s,%s,%s)'
        cursor.execute(self.sql,(name,phone,passport))
        conn.commit()
    # 注册
    def register(self,name,passport,phone,password):
        self.creatperson(name,phone,passport)
        self.creatcard(password,passport)
    # 检验用户密码是否正确
    def checkuser(self,passport,password):
        self.sqllog0='select carid from person where userid=%s'
        if cursor.execute(self.sqllog0,(passport,)):
            self.card_id=cursor.fetchone()[0]
            self.sqllog1 = 'select password from card where id=%s'
            if cursor.execute(self.sqllog1,(self.card_id,)):
                if cursor.fetchone()[0]==password:
                    return 1
        return 0
    # 查询
    def chaxun(self,passport):
        self.sqlcarid='select carid from person where userid=%s'
        cursor.execute(self.sqlcarid,(passport,))
        self.id=cursor.fetchone()[0]
        self.sqlmoney='select money from card where id=%s'
        cursor.execute(self.sqlmoney,(self.id,))
        return cursor.fetchone()[0]
    # 存钱
    def savemoney(self, money,passport):
        self.sqlscarid='select carid from person where userid=%s'
        cursor.execute(self.sqlscarid,(passport,))
        self.id=cursor.fetchone()[0]
        self.sqlsmoney='select money from card where id=%s'
        cursor.execute(self.sqlsmoney,(self.id,))
        newmoney=int(cursor.fetchone()[0])+int(money)
        updata_money = 'update card set money=%s where id=%s'
        cursor.execute(updata_money, (str(newmoney),self.id,))
        conn.commit()
    # 取钱 转钱
    def getmoney(self, money,passport,card=None):
        sqlscarid='select carid from person where userid=%s'
        cursor.execute(sqlscarid,(passport,))
        id=cursor.fetchone()[0]
        sqlsmoney='select money from card where id=%s'
        cursor.execute(sqlsmoney,(id,))
        getmoney=int(cursor.fetchone()[0])
        if getmoney >= int(money):
            newmoney=getmoney-int(money)
            updata_money = 'update card set money=%s where id=%s'
            cursor.execute(updata_money, (str(newmoney),id))
            if card:
                sqlsothermoney = 'select money from card where card=%s'
                if cursor.execute(sqlsothermoney, (card,)):
                    updata_othermoney = 'update card set money=%s where card=%s'
                    cursor.execute(updata_othermoney,(money,card))
                else:
                    return 2
            conn.commit()
            return 1
        return 0
#     改密码
    def changepassword(self,passport,newpassword):
        sqllog0 = 'select carid from person where userid=%s'
        cursor.execute(sqllog0, (passport,))
        card_id = cursor.fetchone()[0]
        changesql='update card set password = %s where id=%s'
        cursor.execute(changesql,(newpassword,card_id))
        conn.commit()
    # 改卡（补卡）
    def changecard(self,passport):
        sqllog0 = 'select carid from person where userid=%s'
        cursor.execute(sqllog0, (passport,))
        card_id = cursor.fetchone()[0]
        changesql='update card set card = %s where id=%s'
        newcard='622848356' + ''.join(random.sample(str(string.digits) * 10, 10))
        cursor.execute(changesql,(newcard,card_id))
        conn.commit()
    #锁卡
    def suoka(self,passport):
        sqllog0 = 'select carid from person where userid=%s'
        cursor.execute(sqllog0, (passport,))
        card_id = cursor.fetchone()[0]
        change_statesql='update card set state = %s where id=%s'
        cursor.execute(change_statesql,('0',card_id))
        conn.commit()
    def checkstate(self,passport):
        sqllog0 = 'select carid from person where userid=%s'
        cursor.execute(sqllog0, (passport,))
        card_id = cursor.fetchone()[0]
        statesql='select state from card where id=%s'
        cursor.execute(statesql,(card_id,))
        conn.commit()
        return cursor.fetchone()[0]
if __name__ == '__main__':
    Options=Option()
    while 1:
        option=input("欢迎来到ATM：(1)注册(2)查询(3)存钱(4)取钱(5)转账(6)改密(7)解卡(8)补卡(其他退出)")
        # 注册
        if option=='1':
            name=input('请输入注册名字:\n')
            phone=input('请输入注册电话:\n')
            passport=input('请输入注册身份证:\n')
            password=input('请输入注册密码：\n')
            Options.register(name=name,passport=passport,phone=phone,password=password)
            card=Options.searchcard(passport)
            print("注册成功,您的卡号为%s"%card)
        # 查询
        elif option == '2':
            num=0
            passport = input('请输入身份证:\n')
            while num<3:
                password = input('请输入密码：\n')
                if Options.checkuser(passport,password):
                    if Options.checkstate(passport)=='1':
                        print('您的账户余额为%s'%Options.chaxun(passport))
                    else:
                        print('您的账号被冻结')
                    break
                else:
                    num+=1
                    print('密码错误！')
            if num>=3:
                Options.suoka(passport)
        # 存钱
        elif option == '3':
            num=0
            passport = input('请输入身份证:\n')
            while num<3:
                password = input('请输入密码：\n')
                if Options.checkuser(passport, password):
                    if Options.checkstate(passport) == '1':
                        money=input('请输入存的钱')
                        Options.savemoney(money,passport)
                        print('已存入')
                    else:
                        print('您的账号被冻结')
                    break
                else:
                    print('账号或密码错误！')
            if num >= 3:
                Options.suoka(passport)
        # 取钱
        elif option == '4':
            num=0
            passport = input('请输入身份证:\n')
            while num<3:
                password = input('请输入密码：\n')
                if Options.checkuser(passport, password):
                    if Options.checkstate(passport) == '1':
                        money=input('请输入要取出的钱')
                        if Options.getmoney(money,passport)==1:
                            print('已取出')
                        else:print('没那么多钱取')
                    else:
                        print('您的账号被冻结')
                    break
                else:
                    print('账号或密码错误！')
            if num >= 3:
                Options.suoka(passport)
        #转账
        elif option == '5':
            num=0
            passport = input('请输入身份证:\n')
            while num<3:
                password = input('请输入密码：\n')
                if Options.checkuser(passport, password):
                    if Options.checkstate(passport) == '1':
                        money=input('请输入要转出的钱')
                        card=input('请输入要转入的账号')
                        if Options.getmoney(money,passport,card)==1:
                            print('已转入到对方账号')
                        elif Options.getmoney(money,passport,card)==2:
                            print('无此账号，无法转入')
                        else:print('没那么多钱转')
                    else:
                        print('您的账号被冻结')
                    break
                else:
                    print('账号或密码错误！')
            if num >= 3:
                Options.suoka(passport)
        # 改密码
        elif option == '6':
            num=0
            passport = input('请输入身份证:\n')
            while num<3:
                password = input('请输入原密码：\n')
                if Options.checkuser(passport, password):
                    if Options.checkstate(passport) == '1':
                        newpassword=input('请输入新密码')
                        Options.changepassword(passport,newpassword)
                        print('密码已修改')
                    else:
                        print('您的账号被冻结')
                    break
                else:
                    print('账号或原密码错误！')
            if num>=3:
                Options.suoka(passport)
        elif option == '7':
            pass
        # 补卡
        elif option == '8':
            num=0
            passport = input('请输入丢失银行卡绑定的身份证:\n')
            while num<3:
                password = input('请输入丢银行卡的密码：\n')
                if Options.checkuser(passport, password):
                    if Options.checkstate(passport) == '1':
                        Options.changecard(passport)
                        card = Options.searchcard(passport)
                        print("补卡成功,您的新卡号为%s"%card)
                    else:
                        print('您的账号被冻结')
                    break
                else:
                    print('账号或原密码错误，不可补卡！')
            if num>=3:
                Options.suoka(passport)
        # 退出
        else:
            break



