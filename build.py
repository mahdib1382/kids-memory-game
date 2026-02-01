"""
اسکریپت ساخت فایل اجرایی بازی حافظه کودکان
Build Script for Kids Memory Game
نسخه 1.0
"""

import os
import sys
import shutil
from pathlib import Path
import subprocess

# تنظیمات ساخت
APP_NAME = "KidsMemoryGame"
VERSION = "1.0"
AUTHOR = "mahdib1382"
DESCRIPTION = "بازی حافظه آموزشی برای کودکان"

# مسیرهای پروژه
PROJECT_DIR = Path(__file__).parent
DIST_DIR = PROJECT_DIR / "dist"
BUILD_DIR = PROJECT_DIR / "build"
FINAL_DIR = PROJECT_DIR / "KidsMemoryGame_Final"

def clean_previous_builds():
    """پاکسازی ساخت‌های قبلی"""
    print("🧹 پاکسازی ساخت‌های قبلی...")
    
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
        print("   ✓ پوشه dist پاک شد")
    
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
        print("   ✓ پوشه build پاک شد")
    
    if FINAL_DIR.exists():
        shutil.rmtree(FINAL_DIR)
        print("   ✓ پوشه KidsMemoryGame_Final پاک شد")

def check_pyinstaller():
    """بررسی نصب PyInstaller"""
    try:
        import PyInstaller
        print("✓ PyInstaller نصب شده است")
        return True
    except ImportError:
        print("❌ PyInstaller نصب نیست!")
        print("لطفاً با دستور زیر نصب کنید:")
        print("pip install pyinstaller")
        return False

def create_icon():
    """ایجاد یک آیکون ساده (اگر وجود نداشت)"""
    icon_path = PROJECT_DIR / "icon.ico"
    
    if icon_path.exists():
        print("✓ فایل آیکون موجود است")
        return str(icon_path)
    
    print("⚠ فایل آیکون یافت نشد - از آیکون پیش‌فرض استفاده می‌شود")
    return None

def build_executable():
    """ساخت فایل اجرایی با PyInstaller"""
    print("\n🔨 شروع ساخت فایل اجرایی...")
    
    # پارامترهای PyInstaller
    pyinstaller_args = [
        'main.py',
        '--name=' + APP_NAME,
        '--onefile',  # یک فایل اجرایی
        '--windowed',  # بدون پنجره کنسول
        '--clean',
        '--noconfirm',
    ]
    
    # اضافه کردن آیکون (اگر موجود بود)
    icon_path = create_icon()
    if icon_path:
        pyinstaller_args.append(f'--icon={icon_path}')
    
    # اضافه کردن پوشه assets
    pyinstaller_args.extend([
        '--add-data=assets;assets',  # برای ویندوز از ; استفاده می‌شود
    ])
    
    # متادیتا برای فایل ویندوز
    pyinstaller_args.extend([
        f'--version-file=version_info.txt' if Path('version_info.txt').exists() else '--noupx',
    ])
    
    # اجرای PyInstaller
    try:
        result = subprocess.run(
            ['pyinstaller'] + pyinstaller_args,
            check=True,
            capture_output=True,
            text=True
        )
        print("✓ فایل اجرایی با موفقیت ساخته شد")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ خطا در ساخت: {e}")
        print(e.output)
        return False

def create_distribution_folder():
    """ایجاد پوشه توزیع نهایی"""
    print("\n📦 ایجاد پوشه توزیع نهایی...")
    
    # ایجاد پوشه اصلی
    FINAL_DIR.mkdir(exist_ok=True)
    
    # کپی فایل اجرایی
    exe_source = DIST_DIR / f"{APP_NAME}.exe"
    exe_dest = FINAL_DIR / f"{APP_NAME}.exe"
    
    if exe_source.exists():
        shutil.copy2(exe_source, exe_dest)
        print(f"   ✓ {APP_NAME}.exe کپی شد")
    else:
        print(f"   ❌ فایل اجرایی یافت نشد!")
        return False
    
    # کپی پوشه assets
    assets_source = PROJECT_DIR / "assets"
    assets_dest = FINAL_DIR / "assets"
    
    if assets_source.exists():
        shutil.copytree(assets_source, assets_dest, dirs_exist_ok=True)
        print("   ✓ پوشه assets کپی شد")
    
    # ایجاد پوشه data
    data_dest = FINAL_DIR / "data"
    data_dest.mkdir(exist_ok=True)
    print("   ✓ پوشه data ایجاد شد")
    
    # ایجاد راهنمای فارسی
    create_manual(FINAL_DIR)
    
    print(f"\n✅ پوشه توزیع در {FINAL_DIR} ایجاد شد")
    return True

def create_manual(output_dir):
    """ایجاد فایل راهنمای فارسی"""
    manual_path = output_dir / "Manual.txt"
    
    manual_content = """
╔═══════════════════════════════════════════════════════════════════╗
║                   بازی حافظه کودکان - نسخه 1.0                   ║
║                    Kids Memory Game - Version 1.0                 ║
╚═══════════════════════════════════════════════════════════════════╝

🎮 راهنمای نصب و اجرا
═══════════════════════════════════════════════════════════

📥 نصب:
1. کل پوشه KidsMemoryGame_Final را در جایی مناسب کپی کنید
2. مطمئن شوید پوشه‌های assets و data در کنار فایل اجرایی هستند
3. روی فایل KidsMemoryGame.exe دوبار کلیک کنید

🎯 نحوه بازی:
═══════════════════════════════════════════════════════════

1️⃣ منوی اصلی:
   - شروع بازی: برای شروع بازی جدید
   - تنظیمات: برای تنظیم تعداد بازیکنان و سطح
   - راهنما: برای مشاهده قوانین بازی
   - خروج: برای بستن بازی

2️⃣ تنظیمات:
   - تعداد بازیکنان: 1 تا 5 نفر
   - سطح (محدوده اعداد): 1-10 یا 11-20
   - گوینده: فعال/غیرفعال کردن خواندن اعداد

3️⃣ قوانین بازی:
   - هدف: پیدا کردن جفت کارت‌های یکسان
   - روی کارت‌ها کلیک کنید تا عدد پشت آن‌ها نمایش داده شود
   - اگر دو کارت یکسان بودند، آن‌ها باز می‌مانند
   - اگر متفاوت بودند، دوباره برمی‌گردند
   - بازیکنی که بیشترین جفت را پیدا کند، برنده است!

🔊 ویژگی‌های خاص:
═══════════════════════════════════════════════════════════

✨ گوینده فارسی: وقتی کارتی باز می‌شود، عدد آن خوانده می‌شود
🎨 انیمیشن‌های جذاب: افکت‌های بصری برای کودکان
🎵 صداهای مناسب: جلوه‌های صوتی مثبت و تشویقی
📊 ثبت امتیاز: ذخیره نتایج بازی‌ها

💾 فایل‌های مهم:
═══════════════════════════════════════════════════════════

📂 assets/
   ├── textures/     (تصاویر اعداد - اختیاری)
   ├── sounds/       (صداهای بازی - اختیاری)
   └── voices/       (صدای گوینده - اختیاری)

📂 data/
   └── game_results.json  (نتایج بازی‌ها)

⚙️ نیازمندی‌های سیستم:
═══════════════════════════════════════════════════════════

💻 سیستم عامل: Windows 10 یا 11
🖥️ پردازنده: Intel Core i3 یا بالاتر
💾 حافظه رم: 2 گیگابایت یا بیشتر
📀 فضای خالی: 200 مگابایت

🔧 رفع مشکلات:
═══════════════════════════════════════════════════════════

❓ اگر بازی اجرا نشد:
   - مطمئن شوید Windows Defender بازی را بلاک نکرده
   - پوشه‌های assets و data باید در کنار exe باشند
   - از قابلیت Run as Administrator استفاده کنید

❓ اگر صدا پخش نشد:
   - فایل‌های صوتی در پوشه assets/sounds هستند؟
   - بلندگوی سیستم روشن است؟

❓ اگر تصاویر نمایش داده نشد:
   - فایل‌های PNG در assets/textures هستند؟
   - در صورت نبود تصاویر، متن نمایش داده می‌شود

📞 پشتیبانی:
═══════════════════════════════════════════════════════════

GitHub: https://github.com/mahdib1382/kids-memory-game
نسخه: 1.0
توسعه‌دهنده: mahdib1382

═══════════════════════════════════════════════════════════
          با آرزوی یادگیری شاد برای دانش‌آموزان! 📚✨
═══════════════════════════════════════════════════════════
"""
    
    with open(manual_path, 'w', encoding='utf-8') as f:
        f.write(manual_content)
    
    print("   ✓ فایل Manual.txt ایجاد شد")

def create_deployment_checklist():
    """ایجاد چک‌لیست استقرار"""
    checklist_path = FINAL_DIR / "DEPLOYMENT_CHECKLIST.txt"
    
    checklist_content = r"""
╔═══════════════════════════════════════════════════════════════════╗
║              چک‌لیست استقرار بازی در مدرسه                       ║
║            Deployment Checklist for School                        ║
╚═══════════════════════════════════════════════════════════════════╝

📋 فایل‌های ضروری برای کپی در فلش‌مموری:
═══════════════════════════════════════════════════════════

✅ پوشه کامل: KidsMemoryGame_Final/
   ├── ✅ KidsMemoryGame.exe (فایل اجرایی اصلی)
   ├── ✅ Manual.txt (راهنمای فارسی)
   ├── ✅ DEPLOYMENT_CHECKLIST.txt (این فایل)
   │
   ├── 📁 assets/ (پوشه دارایی‌ها)
   │   ├── 📁 textures/ (تصاویر اعداد - اختیاری)
   │   ├── 📁 sounds/ (جلوه‌های صوتی - اختیاری)
   │   ├── 📁 voices/ (گوینده فارسی - اختیاری)
   │   └── 📄 README.md
   │
   └── 📁 data/ (پوشه داده‌ها - خودکار ایجاد می‌شود)

💾 حجم کل: حدود 50-200 مگابایت (بسته به فایل‌های صوتی)

🔍 بررسی نهایی قبل از استقرار:
═══════════════════════════════════════════════════════════

1. ☐ فایل KidsMemoryGame.exe در پوشه اصلی وجود دارد
2. ☐ پوشه assets در کنار فایل exe قرار دارد
3. ☐ پوشه data ایجاد شده است
4. ☐ فایل Manual.txt قابل خواندن است
5. ☐ بازی بدون خطا اجرا می‌شود
6. ☐ منوی اصلی به درستی نمایش داده می‌شود
7. ☐ دکمه‌های منو کار می‌کنند
8. ☐ تنظیمات قابل تغییر است
9. ☐ بازی به درستی اجرا می‌شود
10. ☐ امتیازات ذخیره می‌شوند (فایل game_results.json)

✨ ویژگی‌های اختیاری:
═══════════════════════════════════════════════════════════

📸 تصاویر (assets/textures/):
   ☐ فایل‌های 1.png تا 20.png برای نمایش تصویری اعداد
   ⚠ در صورت نبود، متن نمایش داده می‌شود

🔊 صداها (assets/sounds/):
   ☐ click.wav - صدای کلیک
   ☐ success.mp3 - صدای موفقیت
   ☐ wrong.wav - صدای اشتباه
   ⚠ در صورت نبود، بازی بدون صدا اجرا می‌شود

🎙️ گوینده (assets/voices/):
   ☐ فایل‌های 1.mp3 تا 20.mp3 برای خواندن اعداد
   ⚠ در صورت نبود، فقط کارت‌ها نمایش داده می‌شوند

📝 مراحل نصب در کامپیوتر مدرسه:
═══════════════════════════════════════════════════════════

1. فلش‌مموری را به کامپیوتر متصل کنید
2. پوشه KidsMemoryGame_Final را کپی کنید در:
   📂 C:\Games\KidsMemoryGame\
   یا
   📂 Desktop\KidsMemoryGame\

3. روی KidsMemoryGame.exe راست کلیک کنید
4. "Create shortcut" را انتخاب کنید
5. میانبر را روی دسکتاپ قرار دهید
6. نام میانبر را تغییر دهید به: "بازی حافظه"

7. برای اجرا، روی میانبر دوبار کلیک کنید

⚠️ نکات مهم:
═══════════════════════════════════════════════════════════

🛡️ امنیت:
   - ممکن است Windows Defender هشدار دهد
   - روی "More info" کلیک کنید
   - سپس "Run anyway" را انتخاب کنید
   - این طبیعی است چون برنامه امضای دیجیتال ندارد

💻 سازگاری:
   ✅ Windows 10 (64-bit)
   ✅ Windows 11
   ⚠ Windows 7/8: ممکن است نیاز به آپدیت داشته باشد

🔧 مشکلات رایج:
═══════════════════════════════════════════════════════════

❌ "Windows protected your PC":
   ➡️ کلیک روی "More info" → "Run anyway"

❌ فایل باز نمی‌شود:
   ➡️ روی فایل راست کلیک → Properties
   ➡️ "Unblock" را انتخاب کنید → OK

❌ بازی خیلی کند است:
   ➡️ سایر برنامه‌ها را ببندید
   ➡️ از گوینده غیرفعال کنید (در تنظیمات)

❌ صدا پخش نمی‌شود:
   ➡️ بلندگوی سیستم را چک کنید
   ➡️ فایل‌های صوتی را بررسی کنید

📊 پیگیری پیشرفت دانش‌آموزان:
═══════════════════════════════════════════════════════════

📁 فایل game_results.json شامل:
   - تاریخ و زمان هر بازی
   - برنده هر بازی
   - مدت زمان بازی
   - امتیاز هر بازیکن

💡 برای مشاهده:
   فایل را با Notepad باز کنید
   یا از ابزارهای JSON Viewer استفاده کنید

🎓 پیشنهادات آموزشی:
═══════════════════════════════════════════════════════════

1. ابتدا با سطح 1-6 (6 جفت) شروع کنید
2. تدریجاً به 1-10 (10 جفت) برسید
3. برای دانش‌آموزان پیشرفته: 11-20
4. از حالت چند نفره برای کار گروهی استفاده کنید
5. گوینده را برای یادگیری تلفظ فعال کنید

✅ آماده استقرار:
═══════════════════════════════════════════════════════════

تاریخ ساخت: [AUTO]
نسخه: 1.0
توسعه‌دهنده: mahdib1382

═══════════════════════════════════════════════════════════
         بازی آموزشی حافظه برای دانش‌آموزان پایه سوم 🎓
═══════════════════════════════════════════════════════════
"""
    
    with open(checklist_path, 'w', encoding='utf-8') as f:
        f.write(checklist_content)
    
    print("   ✓ فایل DEPLOYMENT_CHECKLIST.txt ایجاد شد")

def create_version_info():
    """ایجاد فایل اطلاعات نسخه برای ویندوز"""
    version_info_path = PROJECT_DIR / "version_info.txt"
    
    version_content = f"""# UTF-8
#
# For more details about fixed file info:
# https://msdn.microsoft.com/en-us/library/ms646997.aspx

VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'{AUTHOR}'),
        StringStruct(u'FileDescription', u'{DESCRIPTION}'),
        StringStruct(u'FileVersion', u'{VERSION}'),
        StringStruct(u'InternalName', u'{APP_NAME}'),
        StringStruct(u'LegalCopyright', u'Copyright (c) 2026 {AUTHOR}'),
        StringStruct(u'OriginalFilename', u'{APP_NAME}.exe'),
        StringStruct(u'ProductName', u'Kids Memory Game'),
        StringStruct(u'ProductVersion', u'{VERSION}')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""
    
    with open(version_info_path, 'w', encoding='utf-8') as f:
        f.write(version_content)
    
    print("✓ فایل version_info.txt ایجاد شد")

def main():
    """تابع اصلی ساخت"""
    print("╔═══════════════════════════════════════════════════════════════════╗")
    print("║         اسکریپت ساخت بازی حافظه کودکان - نسخه 1.0            ║")
    print("╚═══════════════════════════════════════════════════════════════════╝\n")
    
    # بررسی نصب PyInstaller
    if not check_pyinstaller():
        return
    
    # پاکسازی ساخت‌های قبلی
    clean_previous_builds()
    
    # ایجاد فایل version info
    create_version_info()
    
    # ساخت فایل اجرایی
    if not build_executable():
        print("\n❌ خطا در ساخت فایل اجرایی!")
        return
    
    # ایجاد پوشه توزیع
    if not create_distribution_folder():
        print("\n❌ خطا در ایجاد پوشه توزیع!")
        return
    
    # ایجاد چک‌لیست استقرار
    create_deployment_checklist()
    
    print("\n" + "="*70)
    print("✅ ساخت با موفقیت انجام شد!")
    print("="*70)
    print(f"\n📁 پوشه نهایی: {FINAL_DIR}")
    print("\n📋 فایل‌های موجود:")
    print(f"   • {APP_NAME}.exe")
    print("   • Manual.txt")
    print("   • DEPLOYMENT_CHECKLIST.txt")
    print("   • assets/ (پوشه دارایی‌ها)")
    print("   • data/ (پوشه داده‌ها)")
    
    print("\n🎯 مراحل بعدی:")
    print("   1. محتویات پوشه KidsMemoryGame_Final را تست کنید")
    print("   2. فایل Manual.txt را مطالعه کنید")
    print("   3. DEPLOYMENT_CHECKLIST.txt را برای استقرار دنبال کنید")
    print("   4. پوشه را در فلش‌مموری کپی کنید")
    
    print("\n" + "="*70)
    print("موفق باشید! 🎉")
    print("="*70)

if __name__ == "__main__":
    main()
