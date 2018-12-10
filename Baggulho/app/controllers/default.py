from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import app, db, login_manager

from app.models.tables import User, Product, Image, Sale
from app.models.forms import LoginForm, RegisterForm, SaleForm

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    r = Image.query.filter_by().all()
    return render_template('index.html', images=r)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Invalid login")
    return render_template('login.html',
                           form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect( url_for("login") )

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        i = User(username=form.username.data, name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(i)
        db.session.commit()
        flash("Olá %s Faça Login" % (form.name.data) )
        return redirect( url_for("login") )

    return render_template("register.html", form = form)

@app.route("/index/main/")
def main():
    r = Product.query.filter_by().all()
    return render_template('main.html', produtos=r)

@app.route("/index/main/", defaults={'name': None})
@app.route("/index/main/<name>")
def view_types(name):
    bands = Product.query.filter_by(types=name).all()
    return render_template('main.html', bands=bands)

@app.route("/index/main/products", defaults={'id': None})
@app.route("/index/main/products/<id>")
def view_product(id):
    product = Product.query.filter_by(id=int(id)).first()
    if product != None:
        return render_template('appliance.html', product=product)
    else:
        return render_template('main.html', product=product)

@app.route("/index/main/products/sale", defaults={'id': None}, methods=["GET", "POST"])
@app.route("/index/main/products/sale/<id>")
def purchase_item(id):
    item = Product.query.filter_by(id=int(id)).first()
    form = SaleForm()
    print (item)
    if current_user.is_authenticated and item.unit > 0:
        return render_template('purchase.html', item=item, form=form)
    elif current_user.is_authenticated and item.unit <= 0:
        flash("Infelizmente este Produto está fora de estoque temporariamente")
        return redirect( url_for("index") )
    else:
        flash("Faça login para comprar")
        return redirect( url_for("login") )

@app.route("/index/main/products/sale/end/")
def sale_end():
    return render_template("finalize.html")


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info: None"})
def teste(info):
    '''
    i = User("test3", "1234", "Matheus Cavalcante", "test3@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "Ok"

    i = Smartphone("Mi 8 EE", "Xiaomi", "8Gb+128Gb", 2350)
    db.session.add(i)
    db.session.commit()

     r = Smartphone.query.filter_by(name="Mi 8 EE").first()
    print (r)
    print (r.brand, r.description)
    return "Ok"

    u = Smartphone.query.filter_by(name="Mi 8 EE").first()
    u.name = "POCOPHONE"
    db.session.add(u)
    db.session.commit()

    d = Smartphone.query.filter_by(name="Mi 8 EE").first()
    d.name = "POCOPHONE"
    db.session.delete(u)
    db.session.commit()

    return "Ok"

    u = Smartphone.query.filter_by(name="Mi 8 EE").first()
    u.img = "img/smartphones/xiaomi/mi8ee.jpg"
    db.session.add(u)
    db.session.commit()

    a = Smartphone.query.filter_by(name="Mi 8 Lite").all()
    a.img = "img/smartphones/xiaomi/mi8lite.jpg"
    db.session.add(a)
    db.session.commit()

    b = Smartphone.query.filter_by(name="Mi A2").all()
    b.img = "img/smartphones/xiaomi/mia2.jpg"
    db.session.add(b)
    db.session.commit()

    c = Smartphone.query.filter_by(name="Redmi Note 6 Pro").all()
    c.img = "img/smartphones/xiaomi/redminote6.jpg"
    db.session.add(c)
    db.session.commit()
    
    d = Smartphone.query.filter_by(name="POCOPHONE").all()
    d.img = "img/smartphones/xiaomi/pocophone.jpg"
    db.session.add(d)
    db.session.commit()
    
    e = Smartphone.query.filter_by(name="P20 Pro").all()
    e.img = "img/smartphones/huawei/p20.jpg"
    db.session.add(e)
    db.session.commit()
    

    u = Smartphone.query.filter_by(name="Redmi Note 6 Pro", description="4Gb+64Gb").first()
    u.img = "img/smartphones/xiaomi/redminote6.jpg"
    db.session.add(u)
    db.session.commit()
    
    u = Product.query.filter_by(name="Mi 8 EE").first()
    u.name = "Mi 8 Pro"
    u.description = "8Gb+128Gb"
    u.price = 2355.39
    u.img = "img/smartphones/xiaomi/mi8pro.jpg"
    db.session.add(u)
    db.session.commit()

    
    i = Product("POCOPHONE","Smartphone", "Xiaomi","6Gb+128", "a", "img/smartphones/xiaomi/redminote6.jpg", 1528.99)
    db.session.add(i)
    db.session.commit()

    i = Product("Galaxy S9","Smartphone", "Samsung","4Gb+128", "a","img/smartphones/s9.png", 2999)
    db.session.add(i)
    db.session.commit()

    a = Product("Galaxy Note 9","Smartphone", "Samsung","6Gb+128", "a","img/smartphones/note9.png", 3999)
    db.session.add(a)
    db.session.commit()

    b = Product("Iphone XS Max","Smartphone", "Apple","2Gb+256Gb", "a", "img/smartphones/iphone.jpg", 8799)
    db.session.add(b)
    db.session.commit()
    
    i = Product("Mi Band 4","SmartBands", "Xiaomi","a", "a", "img/smart_wathcs_bands/band/miband2.jpg", 67.12)
    db.session.add(i)
    db.session.commit()

    i = Product("Mi Band 3","SmartBand", "Xiaomi","a", "a", "img/smart_wathcs_bands/band/miband3.jpg", 93.19)
    db.session.add(i)
    db.session.commit()

    i = Product("AMAZFIT Cor MiDong","SmartBands", " Xiaomi","a", "a", "img/smart_wathcs_bands/band/amazfit.jpg", 157.97)
    db.session.add(i)
    db.session.commit()
    
    i = Product("POCOPHONE","SmartPhones", "Xiaomi","6Gb+128", "a", "img/smartphones/xiaomi/redminote6.jpg", 1528.99)
    db.session.add(i)
    db.session.commit()
    
    i = Product("POCOPHONE","SmartPhones", "Xiaomi","6Gb+128", "a", "img/smartphones/xiaomi/pocophone.jpg", 1528.99, 50)
    db.session.add(i)
    db.session.commit()
    '''

    u = Product.query.filter_by(name="Galaxy Note 9").first()
    u.description ="6Gb Ram + 128Gb Rom"   
    db.session.add(u)
    db.session.commit()

    
    return "ok"
