from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import desc
from flask import jsonify
from flask import request
import copy
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:123456@localhost:3306/test1?charset=utf8'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SECRET_KEY"]="xxx"
db=SQLAlchemy(app)
# 评价数据库
class Comment1(db.Model):
    __tablename__="Comments"
    id=db.Column(db.Integer,primary_key=True)
    userid=db.Column(db.Integer,foreign_key=True)
    productid=db.Column(db.Integer,foreign_key=True)
    pingfen=db.Column(db.Float,nullable=False)
    pingjia=db.Column(db.String(200))
    shijian=db.Column(db.String(64))
    image=db.Column(db.String(500))
    
    def __init__(self,userid,productid,pingfen,pingjia,shijian,image):
        # self.commentid=commentid
        self.userid=userid
        self.productid=productid
        self.pingfen=pingfen
        self.pingjia=pingjia
        self.shijian=shijian
        self.image=image
    def __repr__(self):
        return "<User %s>" %self.userid
@app.route('/c')
def index():
    dic={}
    dic1={}
    pinglun=[]
    zuihou={}
    content = '<h1>Comments</h1><hr><ul>'
    Comments = Comment1.query.all()  # 查询所有数据
    if not Comments:
        return "<p>No users exist! <a href='/addcomment'>Add comments first.</a></p>"#无数据时
    for Comment in Comments:            #调出所有数据，并将数据调入键值对
        # dic["id"]=Comment.commentid
        dic["grade"]=Comment.pingfen
        dic["content"]=Comment.pingjia
        dic["productid"]=Comment.productid
        dic["shijian"]=Comment.shijian
        dic["image"]=Comment.image

        dic1=copy.deepcopy(dic)         #锁定键值
        pinglun.append(dic1)            #将键值放入列表
        
    zuihou["neirong"]=pinglun          #将列表放入键值对输出
    return zuihou
        

    content += '</ul>'
    content += "<p><a href='/filter'>filter</a>"
    content += " | <a href='/sort'>sort</a> "
    content += " | <a href='/update'>update</a>"
    content += " | <a href='/pagination'>pagination</a></p>"

  #以字符串形式输出数组

      #理想的改造是将users在模板里循环开来
@app.route('/addcomment')
def add_user():
    #手工添加几行记录，思考：如何用页面输入来添加？
    feedback1 = Comment1(1,100001, 8.0,"圣诞节送给朋友的礼物，他很感激我并且说下辈子愿意做牛做马报答我的猪肉铺之恩，我觉得很赚","2020/05/19 20:00:00")
    feedback2 = Comment1(1,100002, 8.0,"母亲牛肉棒，你值得拥有","2020/05/19 20:00:00")
    feedback3 = Comment1(1,100003, 8.0,"盐焗鸡蛋，你值得拥有","2020/05/19 20:00:00")
    feedback4 = Comment1(1,200001, 8.0,"卫龙辣条，你值得拥有","2020/05/19 20:00:00")
    feedback5 = Comment1(1,200002, 8.0,"乐事薯片，你值得拥有","2020/05/19 20:00:00")
    feedback6 = Comment1(1,200003, 8.0,"上好佳虾片，你值得拥有","2020/05/19 20:00:00")
    feedback7 = Comment1(1,300001, 8.0,"溜溜梅，你值得拥有","2020/05/19 20:00:00")
    feedback8 = Comment1(1,300002, 8.0,"三只松鼠，你值得拥有","2020/05/19 20:00:00")
    feedback9 = Comment1(1,300003, 8.0,"焦糖瓜子，你值得拥有","2020/05/19 20:00:00")
    feedback10 = Comment1(1,400001, 8.0,"皇冠丹麦，你值得拥有","2020/05/19 20:00:00")
    feedback11 = Comment1(1,400002, 8.0,"奥利奥，你值得拥有","2020/05/19 20:00:00")
    feedback12 = Comment1(1,400003, 8.0,"百醇，你值得拥有","2020/05/19 20:00:00")
    feedback13 = Comment1(1,500001, 8.0,"费列罗，你值得拥有","2020/05/19 20:00:00")
    feedback14 = Comment1(1,500002, 8.0,"大白兔，你值得拥有","2020/05/19 20:00:00")
    feedback15 = Comment1(1,500003, 8.0,"不二家棒棒糖，你值得拥有","2020/05/19 20:00:00")
    feedback16 = Comment1(1,600001, 8.0,"旺仔牛奶，你值得拥有","2020/05/19 20:00:00")
    feedback17 = Comment1(1,600002, 8.0,"RIO，你值得拥有","2020/05/19 20:00:00")
    feedback18 = Comment1(1,600003, 8.0,"可口可乐，你值得拥有","2020/05/19 20:00:00")
    feedback19 = Comment1(1,700001, 8.0,"光明白熊雪糕，你值得拥有","2020/05/19 20:00:00")
    feedback20 = Comment1(1,800001, 8.0,"喜之郎果冻，你值得拥有","2020/05/19 20:00:00")


    db.session.add(feedback1)
    db.session.add(feedback2)
    db.session.add(feedback3)
    db.session.add(feedback4)
    db.session.add(feedback5)
    db.session.add(feedback6)
    db.session.add(feedback7)
    db.session.add(feedback8)
    db.session.add(feedback9)
    db.session.add(feedback10)
    db.session.add(feedback11)
    db.session.add(feedback12)
    db.session.add(feedback13)
    db.session.add(feedback14)
    db.session.add(feedback15)
    db.session.add(feedback16)
    db.session.add(feedback17)
    db.session.add(feedback18)
    db.session.add(feedback19)
    db.session.add(feedback20)


    db.session.commit()

    return "<p>add succssfully! <a href='/c'>Home</a></p>"


@app.route('/ajax_post', methods=["POST","GET"]) #与上例类似

def ajax_post():
    json_data = request.get_json()  #注：这个方法不管GET|POST
    pingfen1 = json_data["pingfena"]
    pingjia1 = json_data["pingjiaa"]
    userid1 = json_data["userid"]
    productid1 = json_data["productid"]
    shijian=json_data["shijian"]
    image=json_data["image"]


    feedback=Comment1(userid1,productid1,pingfen1,pingjia1,shijian,image)
    db.session.add(feedback)

    Comments = Comment1.query.filter(Comment1.productid==productid1)
    x=1
    n=0
    for comment in Comments:
        n=n+float(comment.pingfen)
        print(n)
        f=float(n/x)
        x=x+1
        print(f)

    Product.query.filter_by(productid=productid1).update(dict(rate=f))

    db.session.commit()
    # x+=1
    return jsonify(grade=pingfen1,content=pingjia1,date=shijian,tupian=image)


    #return jsonify(pinfen='6', comments = '非常棒')   #ajax特色：接收/返回json

# 商品数据库
class Product(db.Model):
    __tablename__ = 'products'
    productid = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(80), unique=True)
    rate = db.Column(db.Float, unique=False)
    category = db.Column(db.String(80), unique=False)
    pop = db.Column(db.String(80), unique=False)
    quantity = db.Column(db.String(80), unique=False)
    ingredient = db.Column(db.String(200), unique=False)
    ed = db.Column(db.String(80), unique=False)
    price = db.Column(db.String(80), unique=False)
    image = db.Column(db.String(500), unique=True)
    shoppath = db.Column(db.String(500),unique=True)
    

    def __init__(self,productid,productname,rate,category,pop,quantity,ingredient,ed,price,image,shoppath):
        self.productid = productid
        self.productname = productname
        self.rate = rate
        self.category = category
        self.pop = pop
        self.quantity = quantity
        self.ingredient = ingredient
        self.ed = ed
        self.price = price
        self.image = image
        self.shoppath = shoppath

    def __repr__(self):
        return '<Product %r>' % self.productname

@app.route('/products')
def index2():
    content = '<h1>products</h1><hr><ul>'
    products = Product.query.all()  # 查询所有数据
    if not products:
        return "<p>No products exist! <a href='/addproduct'>Add products first.</a></p>"

    for product in products:
        content += '<li>' + str(product.productid) + ', '+ product.productname + ', ' +str(product.rate) + ', ' + product.category + ', '+ product.pop + ', ' +product.quantity + ', ' +product.ingredient + ', ' +product.ed + ', ' +product.price + ', ' + product.image +'</li>'

    content += '</ul>'
    # content += "<p><a href='/filter'>filter</a>"
    # content += " | <a href='/sort'>sort</a> "
    # content += " | <a href='/update'>update</a>"
    # content += " | <a href='/pagination'>pagination</a></p>"

    return content

@app.route('/p')
def index4():
    dic={}
    dic1={}
    thumbnail=[]
    result={}
    content = '<h1>products</h1><hr><ul>'
    products = Product.query.all()  # 查询所有数据
    if not products:
        return "<p>No products exist! <a href='/addproduct'>Add products first.</a></p>"#无数据时
    for product in products:            #调出所有数据，并将数据调入键值对
        dic["productid"]=product.productid
        dic["productname"]=product.productname
        dic["rate"]=product.rate
        dic["category"]=product.category
        dic["pop"]=product.pop
        dic["quantity"]=product.quantity
        dic["ingredient"]=product.ingredient
        dic["ed"]=product.ed
        dic["price"]=product.price
        dic["image"]=product.image
        dic["shoppath"]=product.shoppath
        dic1=copy.deepcopy(dic)         #锁定键值
        thumbnail.append(dic1)            #将键值放入列表
        
    result["neirong"]=thumbnail          #将列表放入键值对输出
    return result

@app.route('/addproduct')
def add_product():
    product1 = Product('100001','厨师猪肉脯','8.5','肉类制品','中国','18g','猪肉，白砂糖，鱼露，食用盐，食品添加剂（丙三醇、谷氨酸钠、5‘-呈味核苷酸二钠、脱氢乙酸钠、葡萄糖酸内酯、乳酸链球菌素、D-异抗坏血酸钠、乙基麦芽酚、红曲红），食品用香精，香辛料','12个月','2.90','https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D1863126065,4073624891%26fm%3D15%26gp%3D0.jpg',"package_c/goods/goods?goods_id=3255398955%26image_id=45228426833%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2019-08-07%252F8d60ce70-f6e8-4634-98d3-4061c9e98238.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product2 = Product('100002','母亲牛肉棒（原味）','8.8','肉类制品','中国','22g','精选牛肉，麦芽糖，白砂糖，海藻糖，海藻提取物，食品添加剂（乳酸钾、D-异抗坏血酸钠、亚硝酸钠）食用盐，味精，香辛料，食品用香精','12个月','8.50','https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u%3D1087216320,1725897980%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=96094751096%26image_id=289352019782%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fopenapi%252Fimages%252F2020-03-20%252F2cd530f9fe4b33585d7e5be04955cfe5.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product3 = Product('100003','无穷盐焗鸡蛋','7.9','肉类制品','中国','100g','鲜鸡蛋，白砂糖，食用盐，，味精，酿造酱油，香辛料，氧化羟丙基淀粉，红曲黄色素，D-异抗坏血酸钠，呈味核苷酸二钠，食品用香精香料','12个月','9.80','https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u%3D1516671960,3532014954%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=119326246376%26image_id=330901899427%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-05-13%252F89ae8083-c63a-4207-acf6-ddd7cccb96ad.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product4 = Product('200001','卫龙大面筋','6.7','休闲膨化','中国','106g','小麦粉，植物油，生活饮用水，丙三醇，食用盐，大豆膳食纤维粉，白砂糖，味精，辣椒，香辛料，单硬脂酸甘油酯，呈味核苷酸二钠，辣椒红油，环己基氨基磺酸钠，三氯蔗糖，特丁基对苯二酚，纽甜，食用香精香料','120天','8.90','https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u%3D3114071085,1832295694%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=89010707018%26image_id=%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-02-28%252F75eddd1a-f865-40c1-a27f-34b2dfc65bbb.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product5 = Product('200002','乐事薯片（原味）','7.3','休闲膨化','中国','70g','马铃薯，植物油，美国经典原味调味料（食用盐、味精、5‘-呈味核苷酸二钠、二氧化硅）','9个月','7.50', 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u%3D3886675226,2488600569%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=2736649439%26image_id=36764680219%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2019-11-29%252F7975d57d-dbb4-4eb7-9d62-dc68d3b92c04.jpeg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product6 = Product('200003', '上好佳鲜虾片','8.5','休闲膨化','中国','40g','小麦粉，植物油，淀粉，虾（7.0%），复合调味料（白砂糖、食用盐、麦芽糊精、味精、食用香精、酵母抽取物、酱油粉、5‘-呈味核苷酸二钠、琥珀酸二钠），单硬脂酸甘油酯，胭脂虫红，栀子黄','9个月','3.50','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D1266340287,3089588609%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=97454771585%26image_id=%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-03-23%252F928b08b8-25aa-4485-8551-3838911c1e6e.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product7 = Product('300001','溜溜梅清梅','8.3','坚果蜜饯','中国','60g','鲜李梅（嫁接），白砂糖，青梅汁，食用盐，蜂蜜，蔗糖素，食用香料','12个月','8.90','https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D1338506,1963611478%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=95753400495%26image_id=288823661430%26page_from=23%26preloadImgUrl=http%253A%252F%252Ft00img.yangkeduo.com%252Fopenapi%252Fimages%252F2020-03-19%252Ff08e0255482a0b4178192cd7f67386ad.jpeg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product8 = Product('300002','三只松鼠开口松子','8.3','坚果蜜饯','中国','185g','松子，植物油，酸度调节剂（330），抗氧化剂（319）','8个月','29.90','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u%3D4203466726,4286923813%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=6734264053%26image_id=104974889760%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2019-05-23%252F8f9a29f4-924a-4f45-8ef1-b218e8f02126.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product9 = Product('300003','恰恰焦糖瓜子','6.7','坚果蜜饯','中国','108g','精选葵花籽，白砂糖，食用盐，赤砂糖，食品添加剂（甜蜜素，安赛蜜，糖精钠，三氯蔗糖，食用香精，特丁基对苯二酚）','8个月','6.90','https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D3552648643,2399165751%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=2577959744%26image_id=%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-04-29%252Fe195712b-e641-4488-a557-bbd705906484.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product10 = Product('400001','皇冠丹麦曲奇','7.8','糕点饼干','中国 原产国（印度尼西亚)','90g','小麦粉，白砂糖，黄油，腰果仁10%，植物油（含维生素E），可可粉，脱脂乳粉，食用盐，碳酸氢铵','24个月','9.90','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D3090522393,3739928051%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=80007750951%26image_id=%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-04-27%252Fa427aa98-6b21-426c-81c1-0a0d3e33be64.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product11 = Product('400002','奥利奥（双莓味）','6.6','糕点饼干','中国','318g','小麦粉，白砂糖，食用植物油，可可粉，淀粉，食用葡萄糖，食品添加剂（碳酸氢钠、碳酸氢氨、柠檬酸、大豆磷脂、胭脂虫红、栀子蓝），食用盐，蓝莓粉，树莓粉，食用香精香料','12个月','21.90','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u%3D550006728,3861498723%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=90298048506%26image_id=279823566455%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-03-04%252F9c59b543-b41e-4e69-893e-00c6e35cf380.jpeg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product12 = Product('400003','百醇（抹茶慕斯味）','8.7','糕点饼干','中国','48g','小麦粉，白砂糖，食用氢化油，乳糖，全脂乳粉，起酥油，液体麦精，抹茶粉，食品添加剂（碳酸氢钠、磷脂、蔗糖脂肪酸酯），食用盐，食用香精香料','12个月','6.80','https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u%3D3023074076,2837828542%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=88651458166%26image_id=277083230667%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-02-26%252F5aaaa980-38d3-45a0-8573-a9a26e480874.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product13 = Product('500001','费列罗Rocher','9.0','糖果','中国','260g','牛奶巧克力30%（白砂糖、可可脂、可可浆、脱脂乳粉、无水奶油），榛子28.5%，白砂糖，植物油，小麦面粉，乳清粉，低脂可可粉，黑巧克力33.5%，木薯淀粉，食盐，植物油，食品添加剂（磷脂、膨松剂、香兰素）','9个月','114.00','https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u%3D2669568969,1560354480%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=90406821470%26_oc_trace_mark=1%26_oc_trace_mark_extra=321%26page_from=0%26_pdd_fs=1%26refer_page_name=brand_station%26refer_page_id=21269_1590375891444_kt28o8h663%26refer_page_sn=21269%26xcx_trace_id=kbTUPBNeQJcxMV0qCnyKsmLWrkmoX0Fx")
    product14 = Product('500002','大白兔奶糖','8.8','糖果','中国','114g','麦芽糖，白砂糖，全脂乳粉，奶油，食品添加剂（明胶），香兰素，食用糯米纸（食用淀粉、水、单双硬脂酸甘油酯）','18个月','6.90','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u%3D477266516,2724604049%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=8830766703%26image_id=%26page_from=23%26preloadImgUrl=http%253A%252F%252Ft00img.yangkeduo.com%252Fopenapi%252Fimages%252F2019-05-16%252Fa97a55f931a14d8ef5317b592ecbe29b.jpeg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product15 = Product('500003','不二家棒棒糖','8.5','糖果','中国','125g','白砂糖，麦芽糖浆，食品添加剂（柠檬酸、红曲红、红花黄），食用盐，食品用香精','12个月','14.90','https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u%3D4067732800,1431314834%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=118160621582%26image_id=328851807774%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-05-07%252F11fa7c58-707e-4a56-8301-81ddc2cc414d.jpeg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product16 = Product('600001','旺仔牛奶','8.9','饮品','中国','245ml','复原乳（80%），水，白砂糖，食品添加剂（蔗糖脂肪酸酯、单双甘油脂肪酸酯），食品用香精','15个月','8.50','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D3810509426,4095828696%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=33223714387%26image_id=%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-05-19%252F6bec3195-f343-4ee5-93e1-06dbca08c7e2.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product17 = Product('600002','RIO（蓝玫瑰味）','0.0','饮品','中国','275ml','水，白砂糖，果葡糖浆，伏特加，重瓣红玫瑰低温提取液（0.1%），浓缩百香果汁，威士忌，结晶果糖，食品添加剂（二氧化碳、柠檬酸、亮蓝），食用香精','18个月','12.80','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D3697771356,846557372%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=90820085641%26image_id=%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-03-06%252Fac88a7c3-13ee-4856-a2f3-6dc10182dbd2.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product18 = Product('600003','可口可乐','8.8','饮品','中国','330ml','水，果葡糖浆，白砂糖，食品添加剂（二氧化碳、焦糖色、磷酸、咖啡因），食用香精','9个月','3.00','https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D1138369626,1900417086%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=87992521786%26image_id=%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-03-06%252F03613ec4-5725-4ca7-b009-dae587ae8f62.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product19 = Product('700001','光明白熊雪糕','8.9','雪糕','中国','100g','牛奶，稀奶油，白砂糖，水，全脂乳粉，奶油，全蛋粉，食品添加剂（食用香精、瓜尔胶、单双甘油脂肪酸酯、吐温80、卡拉胶、海藻酸胺、槐豆胶）','24个月','8.00','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u%3D2210407426,4151806073%26fm%3D15%26gp%3D0.jpg',"package_c/goods/goods?goods_id=108475958648%26image_id=311644358029%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-04-16%252Faefa363f-2eb6-4884-911c-aeffcfc1e0a7.png%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
    product20 = Product('800001','喜之郎蜜桔果冻','7.6','其它','中国','200g','水，白砂糖，蜜桔果肉（>15%）,椰果，魔芋粉，食品添加剂（卡拉胶、乳酸钙、柠檬酸、柠檬酸钠、氯化钾、山梨酸钾、胡萝卜素、柠檬黄、日落黄），食用香精','9个月','8.5','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u%3D476544408,4005364484%26fm%3D26%26gp%3D0.jpg',"package_c/goods/goods?goods_id=2731886995%26image_id=%26page_from=23%26preloadImgUrl=https%253A%252F%252Ft00img.yangkeduo.com%252Fgoods%252Fimages%252F2020-04-29%252F141ee63c-ec3c-456a-a3ae-f6aeea566aa0.jpg%253FimageView2%252F2%252Fq%252F50%252Fw%252F400%252Fformat%252Fwebp")
      

    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.add(product6)
    db.session.add(product7)
    db.session.add(product8)
    db.session.add(product9)
    db.session.add(product10)
    db.session.add(product11)
    db.session.add(product12)
    db.session.add(product13)
    db.session.add(product14)
    db.session.add(product15)
    db.session.add(product16)
    db.session.add(product17)
    db.session.add(product18)
    db.session.add(product19)
    db.session.add(product20)

    db.session.commit()

    return "<p>add succssfully! <a href='/p'>Home</a></p>"

if __name__ == "__main__":
    db.create_all()
    app.run(host="192.168.0.105",port=5002,debug=True)
    





