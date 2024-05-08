from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inisialisasi WebDriver (di sini menggunakan Chrome)
driver = webdriver.Chrome("D:\pythonselenium\belajarselenium\driver")

# Buka halaman registrasi
driver.get("https://candymapper.com/")

# Isi formulir registrasi
username_input = driver.find_element_by_id("username")
username_input.send_keys("marjuniatiputri")

email_input = driver.find_element_by_id("email")
email_input.send_keys("marjuniatiputri@email.com")

password_input = driver.find_element_by_id("password")
password_input.send_keys("Niacantik123_")

# Simulasi klik tombol submit
submit_button = driver.find_element_by_id("submit")
submit_button.click()

# Tunggu beberapa detik untuk memungkinkan proses registrasi selesai
time.sleep(3)

# Verifikasi hasil registrasi
success_message = driver.find_element_by_class_name("success-message").text
assert "Selamat datang" in success_message, "Registrasi gagal"

# Tutup WebDriver
driver.quit()
