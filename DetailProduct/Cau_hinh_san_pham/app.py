from flask import *
import mlab
from models.phone import Phone
from random import randint, choice
mlab.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phone')
def phone():
    phone = Phone.objects
    return render_template('phone.html', all_phones = phone)

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
