# _*_ coding: utf-8 _*_
from panew.model.User import User
from panew import db


#查询示例：
# User_list = User.query.all()
#
# u = User.query.filter_by(User_name='rice').first()
#
# user_list = User.query.filter(User.User_name.endswith('e')).all()
#
# print User_list
# print(type(User_list))
# print u.User_name
# print(type(u))
# print user_list
# print(type(user_list))

#返回数据的样子：
# [<[User] User_id:`1`, User_name:`rice`, User_num:`20151002239`, User_password:`15626010384`, User_nickname:`user1`]
# <type 'list'>
# rice
# <class 'blog2.model.User.User'>
# [<[User] User_id:`1`, User_name:`rice`, User_num:`20151002239`, User_password:`15626010384`, User_nickname:`user1`]
# <type 'list'>

#添加数据(完整属性)：
# user = User(User_id=2,User_name='kingkun',User_num='20151002239',User_password=511450130,User_nickname='user2')
# db.session.add(user)
# db.session.commit()
#添加数据(不完整属性)：

# user = User(User_name='kidgsgsngkun')
# db.session.add(user)
# db.session.commit()

#删除数据
# tmpuser=User.query.filter_by(User_name='kidgsgsngkun').first()
# db.session.delete(tmpuser)
# db.session.commit()

#更新数据

# User.query.filter_by(User_name='kidgsgsngkun').update({'User_name': 'exaid', 'User_password': '515759012','User_num':'20151002222','User_nickname':'kamianrider'})
# db.session.commit()