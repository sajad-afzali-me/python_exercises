import os
from datetime import datetime

# ۱. پیدا کردن ریدمی که دقیقا کنار همین فایل است و تغییر دادن آن
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("README.md", "a") as file:
    file.write(f"\n<!-- Last auto commit: {now} -->")

# ۲. اجرای دستورات گیت برای فرستادن تغییرات به سایت
print("Sending changes to GitHub...")
os.system("git add .")
os.system('git commit -m "auto: daily green patch"')
os.system("git push origin main")
print("Done! Check your GitHub profile for the green square! 🟢")
