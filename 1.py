"""
تمرین 2
فرض کنید ، کدهایی نوشته ایم و بعد اجرای آن ، اینکه کدها بدون ایراد اجرا شده اند یا اجرای نامناسب و غلط داشته ایم را در متغیر x ذخیره می کنیم
برنامه ی اعلام خروجی(print) برای حالت بدون ایراد اجرا شدن کد یا حالت ایراد دار بودن آن را به شکل زیر بنویسید

code is executed with some errors
code is executed with no errors

الف)ساده ترین شکل تنها با print و استفاده از placeholder (جا نگهدار)
 ب) با دستور if

 ج) اصلاح نام متغیر x برای سازگاری با convention پایتون

 و) تغییر متغیر x به عدد و چاپ تعداد خطاها
x= 1 برای حالت با خطا
x = 0 برای حالت بدون خطا

 مرحله دوم) اضافه کردن بخش خطا (ماژول) در صورت خطا دادن. مثلا بگوییم ماژول numpy خطا داده است

مرحله سوم: اضافه کردن شماره خط خطا
شماره ی خط خطا هم در متغیر دیگر ذخیره می شود
 از دو روش مختلف جانگدار مختلف استفاده بکنید
"""

"""ps4 al azif print"""
# آموزش خلاصه نوشتن کد، یعنی مقایسه حالت الف و ب

error_num = 5
package = "numpy"
int_ = 20
if_ = 2232
print(f'code executed with {error_num} errors, in module {package}')
