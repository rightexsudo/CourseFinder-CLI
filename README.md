# CourseFinder-CLI

أداة لاستخراج ودعم البحث عن الدورات التدريبية المجانية عبر سطر الأوامر (CLI) من منصات متعددة.

---

## الميزات
- البحث المتزامن في المنصات التالية: Great Learning، إدراك، معارف.
- دعم المتصفحات: Brave (افتراضي)، Chrome، Edge.
- طباعة مخرجات ملونة لحالة العمل والنتائج.
- حفظ النتائج في ملفات نصية (.txt) لكل منصة على حدة.


## المتطلبات والتثبيت
تثبيت المكتبات المطلوبة عبر سطر الأوامر:

bash```
pip install beautifulsoup4 selenium colorama```

طريقة الاستخدام
bash``
python CourseFinder-cli.py -t <search_topic> -b <browser_name>```
المعاملات (Arguments)
bash```
-t, --topic (مطلوب): موضوع البحث (مثل: python, sql, excel).

-b, --browser (اختياري): المتصفح المستهدف. الخيارات المتاحة: brave (افتراضي)، chrome، edge.```

أمثلة التشغيل
البحث عن موضوع بايثون باستخدام متصفح كروم:

bash```
python CourseFinder-cli.py -t python -b chrome```
البحث عن موضوع SQL بالمتصفح الافتراضي (Brave):
bash```
python CourseFinder-cli.py -t sql```
البحث عن موضوع Excel باستخدام متصفح Edge:
bash```
python CourseFinder-cli.py -t excel -b edge```
المخرجات

يتم إنشاء ملف نصي باسم المنصة والموضوع (مثل courses_edraak_python.txt) يحتوي على عناوين الدورات المكتشفة وروابطها.
