print(1)
St2udent_count = "سجادافضلی هستم", "hi"
print(St2udent_count)
# "text" , 'text'  متن رو میشه تو یکی از اینا برای متغیر تعریف کرد
print(2)
tell = """hello sajad 
welcome to 
univercity"""
print(tell)
# """ text""" برای وقتی که متن ما چن خط باشد و بخواهیم با یک پرینت نشونش بدیم
print(3)
x1x = "hello sajad"
print(len(x1x))
print(len("hello sajad"))
# len  فانکشنی برای نشان دادن طول متن و تعداد حروف و اسپیس ها
print(4)
print(x1x[0])
print(x1x[-3])
print("hello sajad"[4])
print(x1x[0:3])
print(x1x[1:8])
print(x1x[1:])
print(x1x[:-2])
# اعداد داخل کد ایندکس حروف هستندوبرای حرف اول متن صفر و به همین ترتیب افزایش می یابند)استخراج قسمتی از یک استرینگ)
print(5)
#  از هشتگ #برای ساخت کامنت استفاده میشه و به عنوان یه  یادداشت از کدنویس می باشد
print(6)
x2x = 'hello " wanted'
print(x2x)
print('hello " wanted')  # گذاشتن "
print("hello ' wanted")  # گذاشتن '
print("hello \\ wanted")  # (گذاشتن \ (بک اسلش
print("hello \t wanted")  # تب
print("hello \nwanted")  # لاین بعد
# \' , \" , \\ ,\n ,\t  های مهم scape notation
print(7)
print("aa" + "bb")  # دو عبارت را پشت سرهم چاپ می کند
first = "coding"
last = "is cool"
full = f"{first}    {last} .neon"  # میتوان بین کروشه ها هر مقدار معتبری را قرار داد
print(full)
# برای تلفیق چند متغیر -فرمت استرینگ
print(8)
course = "   PYThon programming  "
print(course)
print(course.upper())  # همه حروف استرینگ را حروف بزرگ میکند
print(course.lower())  # همه حروف را کوچک می کند
print(course.title())  # حرف اول هر کلمه را بزرگ میکند
print(course.strip())  # اسپیس های دو طرف متن استرینگ را حذف میکند
print(course.rstrip())  # اسپیس های سمت راست استرینگ رو حذف وبا سمت چپ کاری نداره
print(course.lstrip())  # اسپیس های سمت چپ استرینگ رو حذف وبا سمت راست کاری نداره
course = "PYThon programming"
print(course.find("h"))  # مشخص کردن ایندکس یک حرف یا حروف در استرینگ
print(course.find("Tho"))  # حرف کوچک یابزرگ دراینجا مهم است
print(course.find("o"))
# اگر یک حرف در استرینگ چند بار تکرار شداولین ایندکس نمایش داده می شود
print(course.replace("o", "Z"))
# جابجایی حرف یا حروف  سمت چپ پرانتز با حرف یا حروف سمت راست
print(course.replace("Tho", "Z"))
print("h" in course)  # مشخص کردن وجود حرف یا حروف در استرینگ
print("q" in course)
print("q" not in course)  # in , not in کاربرد
# متود های مخصوص استرینگ (میتوان کل این متود هارا با یک نقطه بعد نام متغیر مشاهده و استفاده کرد)
print(9)
# x = 14       اعداد صحیح در پایتون
# x = 1.4      اعداد اعشاری در پایتون
# x = a + bj   اعداد مختلط در پایتون
# برای هر کدوم از اعداد بالا عملگر های زیر صادق است
print(10 + 21)  # جمع در پایتون
print(25 - 5)  # تفریق در پایتون
print(25 * 5)  # ضرب در پایتون
print(10 / 3)  # تقسیم با اعشار
print(10 // 3)  # تقسیم صحیح -خارج قسمت تقسیم
print(10 % 4)  # باقی مانده تقسیم چپی بر راستی
print(10**3)  # چپی به توان راستی
# اهمیت عملگر ها ابتدا () بعد ** بعد * و/ و %و// و در اخر جمع و تفریق
x = 10
x = x + 5  # پایتون از سمت راست معادله را طبق معادله  بالا حل می کند
print(x)
x = 10
x += 5  # عبارت معادل عبارت 78 به صورت روبرو است و میتوان به جای جمع از سایر عملگر ها نیز استفاده کرد
print(x)
x **= 2
print(x)
print(round(2.51))  # رند کردن اعداد
print(round(2.49))  # رند کردن اعداد
print(abs(-84))  # قدر مطلق گیری از اعداد
# فانکشن های کمی برای اعداد روی پایتون قرار دارد و برای استفاده از محاسبات پیچیده تر باید از ماژول مث استفاده کنیم
import math

# math.pi مقدار دقیق عدد پی هست
print(math.ceil(2.4))  # سقف یک عدد را نشان میدهد.برعکس براکت است
print(math.cos(0))
# کلی متود دیگر در مث قرار دارد و میتوان ازآنهااستفاده کرد
print(10)
# int(x)  فانکشنی برای تبدیل متن  به عدد صحیح
# float(x)   فانکشنی بررای تبدیل متن به عدد اعشاری
# bool(x)  این فانکشن فقط در سه حالت جواب فالس می دهد و بقیه حالات مینویسد درست
# str(x)    فانکشنی برای تبدیل عدد بع استرینگ
# type()    فانکشنی که نوع متغیر را مشخص میکند
# input()  برای دریافت ورودی از کاربر استفاده می شود
# x = input("x:")  دریافت ورودی فقط از طریق ترمینال میشه نه اوت پوت و اوت پوت بعد از اینپوت کد هارو نشون نمیده
print(type(x))
x = float(x)
print(type(x))
x += 5
print(x)
print(bool(""))  # اگر خالی هم بود جواب فالس میشد
print(bool(0))
print(bool(None))
print(bool(555.44))
print(bool("adj"))
print(11)
# x==y   برابری
# x!=y   نابرابری
# x>=y ,x<=y , x>y ,x<y   مقایسه بزرگتری و برابری
print(10 >= 5)
print(3 == 3)
print(3 != 4)
print("ali" > "mohammad")
# عملگر ها فقط وابسته به اعداد نیستند و می توان استرینگ هارا باهم مقایسه کرد
# ord("x")   نمایش عددی کاراکتر ایکس را نشان می دهد
print(ord("a"))
print(ord("m"))
# چون حرف ام از ای نمایش عددی بیشتری دارد و هردو حرف اول  می باشند پس عبارت 119 فالس میشه
# عملگر های مقایسه ای
print(12)
x = 29  # مقدار ایکس رو تغییر بده و دستور زیر رو ران کن
if x > 30:  # از ایف برای ایجاد عبارت شرطی استفاده میشود.حواست به دو نقطه بعد شرط باشه
    print("its warm\ndrink water")
    # حکم شرط اینجا و لاین های بعدی با حفظ فاصله نوشته میشه
elif x > 20:  # از الیف برای اضافه کردن شرط متناسب با شروط قبل استفاده میشود
    print("its nice")
else:  # این عبارت اخر شروط آمده و به معنی در غیر اینصورت می باشد
    print("its cool")
# خلاصه نویسی کردن عبارت شرطی
x = 19  # این مقدار رو تغییر بده و دستور زیر رو اجرا کن
if x >= 18:
    text = "yes"
else:
    text = "not"
print(text)
# روش دوم خلاصه نویسی کاربردی
x = 17
text = "yes" if x >= 18 else "not"  # این خیلی کاربردیه
print(text)
print(13)
# and  - or  - not عملگر های منطقی
# این  سه عبارت یک عبارت درست یا غلط هستند و آن را تغییر بده وکد را ران کن
high_income = True
good_cradit = False
student = True

if high_income:  # high_income==True  عبارت معادل
    print("eligible")
else:
    print("not eligible ")
if high_income and good_cradit:
    # and با استفاده از این عملگر هر دو متغیر ما باید درست باشند تا شرط برقرار شود
    print("eligible")
else:
    print("not eligible")
if high_income or good_cradit:
    # یعنی حداقل یکی از دو متغیر درست باشه  or عملگر
    print("eligible")
else:
    print("not eligible")
if not student:  # عبارت را منفی میکند یعنی باید استیودنت نباشد تا شزط برقرار شود
    print("eligible")
else:
    print("not eligible")
# ترکیب های پیچیده تری نیز میتوان نوشت
if not student and (high_income or good_cradit):
    # پرانتز جدا کننده دستورات است و اول عبارت داخل پرانتز و به ترتیب از چپ برنامه اجرا میشه
    print("eligible")
# این عبارت میگویددانش آموز نباشد و حداقل یکی از متغیر های داخل پرانتز درست باشد
print(14)
# age should be between 18 and 65
age = 19  # سن رو تغییر بده و برنامه رواجرا کن
if age >= 18 and age < 65:  # برنامه نوبا
    print("okey")
else:
    print("not")
if 18 <= age < 65:  # برنامه لجندا
    print("okey")
else:
    print("not")
# اگر متغیر بین دو مقدار باشد
# print()=print("")  این دو عبارت یه لاین خالی در خروجی به ما میدن
print(15)
print()
print("*" * 10)  # تکرار یک متن 10 بار
print(16)
