from flask import *
import mlab
from models.phone import Phone
from models.evaluate import Evaluate
from models.average import Average
from random import randint, choice
mlab.connect()

app = Flask(__name__)

app.secret_key = "tuan@123"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # phone_list = Phone.objects()
        SP_ordered = Average.objects().order_by("-averagePoint") # dau tru tuc la largest to smallest
        top4 = []
        for i in SP_ordered[0:4]:
            phone_dict = {}
            phone_dict["phone"] = Phone.objects.get(id=i.phone)
            phone_dict["averagePoint"] = round(i.averagePoint, 1)
            top4.append(phone_dict)
        return render_template('index.html', top4=top4)

    elif request.method == "POST":
        # form = request.form
        # name1 = form["name1"]
        # name2 = form["name2"]
        # regex1 = re.compile(name1)
        # regex2 = re.compile(name2)
        # phone_li1 = Phone.objects(product_name=regex1)
        # phone_li2 = Phone.objects(product_name=regex2)
        # session["phone_li1"] = phone_li1
        # session["phone_li2"] = phone_li2

        return redirect("/result")


@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "GET":
        SP_ordered = Phone.objects()
        phone_li1 = SP_ordered[0:3]
        phone_li2 = SP_ordered[4:7]
        print(phone_li1[0].product_name)
        print(phone_li2[0].product_name)
        return render_template('result.html', phone_li1=phone_li1, phone_li2=phone_li2)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        # name1 = form["name2"]
        # regex1 = re.compile(name1)
        # regex2 = re.compile(name2)
        # phone_li1 = Phone.objects(product_name=regex1)
        # phone_li2 = Phone.objects(product_name=regex2)
        return "a"




@app.route('/phone')
def phone():
    phone = Phone.objects
    return render_template('phone.html', all_phones = phone)

@app.route('/product-detail/<product_name>',methods = ['GET', 'POST'])
def detail(product_name):
    for phone in Phone.objects():
        if product_name == phone['product_name']:
            for evaluated in Average.objects():
                if evaluated.phone.id == phone.id:
                    n = round(evaluated['averagePoint'] * 2)
                    R = round((255 * (10 - n)) / 10)
                    G = round((255 * n) / 10)
                    B = 0
                    return render_template('product_detail.html', phone = phone, red = R, green = G, blue = B, score = n)


# @app.route('/service/update-service/<service_id>', methods=['GET','POST'])
# def modify(service_id):
#     service_detail = Service.objects().with_id(service_id)
#     if request.method == 'GET': # request là function của Flask, là thông tin của người dùng gửi đến server(yêu cầu,thông tin cá nhân,...)
#         return render_template('modify.html', service = service_detail)
#     elif request.method == 'POST':
#         form = request.form
#         name = form['name']
#         yob = int(form['yob'])
#         phone = form['phone']
#         gender = form['gender']
#         description = form['description']
#         address = form['address']
#         # measurements = form['measurements']
#         service_detail.update(set__name = name, yob = yob, phone = phone, gender = gender, description = description, address = address)
#         service_detail.reload()
#         # return render_template('modify.html', service = service_detail)
#         return "{0}, {1}, {2}, {3} updated".format(name, yob, phone, gender)
#     # return render_template('modify.html')
#
# @app.route('/service/<service_id>')
# def detail(service_id):
#     service_detail = Service.objects().with_id(service_id)
#     return render_template('detail.html', service = service_detail)
#
#
# @app.route('/search/<int:gender>/')
# def search(gender):
#     service = Service.objects(gender=0)
#     # service = Service.objects(yob__lte = 1998)
#     # service = Service.objects
#     return render_template('search.html', all_services = service)
#
#
# @app.route('/admin')
# def admin():
#     services = Service.objects()
#     return render_template('admin.html', services = services)
#
# @app.route('/delete/<service_id>')
# def delete(service_id):
#     service_to_delete = Service.objects().with_id(service_id)
#
#     if service_to_delete == None:
#         return "Not found"
#
#     service_to_delete.delete()
#
#     return redirect(url_for('admin'))
#
# @app.route('/new-phone', methods=['GET', 'POST'])
# def create():
#     if request.method == 'GET': # request là function của Flask, là thông tin của người dùng gửi đến server(yêu cầu,thông tin cá nhân,...)
#         return render_template('new-phone.html')
#     elif request.method == 'POST':
#         form = request.form
#         product_main_image = form['product_main_image'] # Ảnh sản phẩm
#         product_size_image = form['product_size_image'] # Ảnh kích cỡ sản phẩm
#         product_name = form['product_name'] # Tên sản phẩm
#         #1. Màn hình
#         display_technology = form['display_technology'] # Công nghệ màn hình
#         display_resolution = form['display_resolution'] # Độ phân giải
#         display_size = form['display_size'] # Màn hình rộng
#         display_screen = form['display_screen'] # Mặt kính cảm ứng
#         #2. Camera sau
#         back_cam_re = form['back_cam_re'] # Độ phân giải
#         back_cam_vid_rercord = form['back_cam_vid_rercord'] # Quay phim
#         back_cam_flash = form['back_cam_flash'] # Đèn Flash
#         back_cam_features = form['back_cam_features'] # Các tính năng chụp ảnh nâng cao
#         #3. Camera trước
#         front_cam_res = form['front_cam_res'] # Độ phân giải
#         front_cam_vid_call = form['front_cam_vid_call'] # Videocall
#         front_cam_features = form['front_cam_features'] # Các tính năng khác
#         #4. Hệ điều hành-CPU
#         operating_system = form['operating_system'] # Hệ điều hành
#         chipset = form[''] # CPU
#         chipset_speed = form[''] # Tốc độ CPU
#         chipset_gpu = form[''] # Chip đồ họa(GPU)
#         #5. Bộ nhớ và lưu trữ
#         ram = form[''] # RAM
#         rom = form[''] # Bộ nhớ trong
#         rom_available = form[''] # Bộ nhớ khả dụng
#         external_storage = form[''] # Bộ nhớ gắn ngoài
#         #6. Kết nối
#         data = form[''] # Mạng di động
#         sim = form[''] # Loại SIM
#         wifi = form[''] # Kết nối Wifi
#         gps = form[''] # Công nghệ GPS
#         bluetooth = form[''] # bluetooth
#         port = form[''] # Cổng kết nối/sạc
#         headphone_jack = form[''] # Jack tai nghe
#         other_connection = form[''] # Kết nối khác
#         #7. Thiết kế và Trọng lượng
#         design = form[''] # Thiết kế
#         material = form[''] # Chất liệu
#         phone_dimension = form[''] # Kích thước
#         weight = form[''] # Trọng lượng
#         #8. Thông tin pin & Sạc
#         battery_capacity = form[''] # Dung lượng pin
#         battery_type = form['']  # Loại pin
#         battery_technology = form[''] # Công nghệ pin
#         #9. Tiện ích
#         protection = form[''] # Bảo mật nâng cao
#         special_features = form[''] # Tính năng đặc biệt
#         recording = form['']  # Ghi âm
#         radio = form['']  # Radio
#         video_player = form[''] # Định dạng phim
#         music_player = form[''] # Định dạng nhạc
#         #10. Thông tin khác
#         release_date = form[''] # Thời điểm ra mắt
#         phone_brand_name = form[''] # Hãng sản xuất
#         new_service = Service(name = name,
#                               yob = yob,
#                               phone = phone,
#                               gender = gender,
#                               height = height,
#                               # measurements = measurements,
#                               address = address,
#                               description = description,
#                               status = choice([True, False])
#                               )
#         new_service.save()
#
#         return "{0} {1} {2} posted and saved".format(name, yob, phone)

if __name__ == '__main__':
  app.run(debug=True)
