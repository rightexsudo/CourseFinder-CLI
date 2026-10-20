# CourseFinder-CLI

أداة لاستخراج ودعم البحث عن الدورات التدريبية المجانية عبر سطر الأوامر (CLI) من منصات متعددة.



## الميزات
* البحث المتزامن في المنصات التالية: Great Learning، إدراك، معارف.
* دعم المتصفحات: Brave (افتراضي)، Chrome، Edge.
* طباعة مخرجات ملونة لحالة العمل والنتائج.
* حفظ النتائج في ملفات نصية (.txt) لكل منصة على حدة.



## المتطلبات والتثبيت

تثبيت المكتبات المطلوبة عبر سطر الأوامر:

pip install beautifulsoup4 selenium colorama



## طريقة الاستخدام

python CourseFinder-cli.py -t <search_topic> -b <browser_name>
