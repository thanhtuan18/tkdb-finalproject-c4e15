from urllib.request import urlopen
from bs4 import BeautifulSoup
import mlab
from models.phone import Phone
from random import randint, choice
from faker import Faker

mlab.connect()

quote_page1 = "https://www.thegioididong.com/dtdd/samsung-galaxy-s9-plus-128gb"
quote_page2 = "https://www.phonearena.com/phones/Samsung-Galaxy-S9_id10717"

page1 = urlopen(quote_page1)
page2 = urlopen(quote_page2)

soup1 = BeautifulSoup(page1, "html.parser")
soup2 = BeautifulSoup(page2, "html.parser")

product_main_image = soup1.find('div', id='normalproduct').find('aside', class= 'picture').find('img').get('src')
product_name = soup2.find('div', id="phone").find('h1').find('span').text

# image = soup.find('table', class_ = 'infobox box colored bordered innerbordered fill-td type-character list-noicon float-right-clear')
# for img in image.findAll('img'):
#     link = img.get('src')
#     if "scale-to-width-down/300" in link:
#         image = link
#         break




phone = Phone(
    product_main_image = product_main_image # Ảnh sản phẩm
    product_size_image =product_size_image # Ảnh kích cỡ sản phẩm
    product_name = product_name # Tên sản phẩm
    #1. Màn hình
    display_technology = display_technology # Công nghệ màn hình
    display_resolution = display_resolution # Độ phân giải
    display_size = display_size # Màn hình rộng
    display_screen = display_screen # Mặt kính cảm ứng
    #2. Camera sau
    back_cam_re = back_cam_re # Độ phân giải
    back_cam_vid_rercord = back_cam_vid_rercord # Quay phim
    back_cam_flash = back_cam_flash # Đèn Flash
    back_cam_features = back_cam_features # Các tính năng chụp ảnh nâng cao
    #3. Camera trước
    front_cam_res = front_cam_res # Độ phân giải
    front_cam_vid_call = front_cam_vid_call # Videocall
    front_cam_features = front_cam_features # Các tính năng khác
    #4. Hệ điều hành-CPU
    operating_system = operating_system # Hệ điều hành
    chipset = chipset # CPU
    chipset_speed = chipset_speed # Tốc độ CPU
    chipset_gpu = chipset_gpu # Chip đồ họa(GPU)
    #5. Bộ nhớ và lưu trữ
    ram = ram # RAM
    rom = rom # Bộ nhớ trong
    rom_available = rom_available # Bộ nhớ khả dụng
    external_storage = external_storage # Bộ nhớ gắn ngoài
    #6. Kết nối
    data = data # Mạng di động
    sim = sim # Loại SIM
    wifi = wifi # Kết nối Wifi
    gps = gps # Công nghệ GPS
    bluetooth = bluetooth # bluetooth
    port = port # Cổng kết nối/sạc
    headphone_jack = headphone_jack # Jack tai nghe
    other_connection = other_connection # Kết nối khác
    #7. Thiết kế và Trọng lượng
    design = design # Thiết kế
    material = material # Chất liệu
    phone_dimension = phone_dimension # Kích thước
    weight = weight # Trọng lượng
    #8. Thông tin pin & Sạc
    battery_capacity = battery_capacity # Dung lượng pin
    battery_type = battery_type  # Loại pin
    battery_technology = battery_technology # Công nghệ pin
    #9. Tiện ích
    protection = protection # Bảo mật nâng cao
    special_features = special_features # Tính năng đặc biệt
    recording = recording  # Ghi âm
    radio = radio  # Radio
    video_player = video_player # Định dạng phim
    music_player = music_player # Định dạng nhạc
    #10. Thông tin khác
    release_date = release_date # Thời điểm ra mắt
                )
phone.save()
