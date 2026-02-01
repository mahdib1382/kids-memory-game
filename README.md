# بازی حافظه کودکان | Kids Memory Game

<div dir="rtl">

یک بازی حافظه‌ای جذاب و آموزشی برای دانش‌آموزان کلاس سوم که با موتور Ursina ساخته شده است.

An engaging educational memory game for 3rd-grade students built with the Ursina engine.

</div>

---

## 🎮 درباره بازی | About the Game

<div dir="rtl">

### فارسی

این بازی برای کمک به یادگیری و تقویت حافظه کودکان طراحی شده است. دانش‌آموزان با پیدا کردن جفت اعداد یکسان، مهارت‌های حافظه بصری و شناخت اعداد خود را بهبود می‌بخشند.

**ویژگی‌های کلیدی:**
- 🎨 رابط کاربری رنگی و جذاب برای کودکان
- 🔊 گوینده فارسی برای کمک به یادگیری اعداد
- 👥 پشتیبانی از 1 تا 5 بازیکن
- 📊 سیستم امتیازدهی و ذخیره نتایج
- 🎯 محدوده‌های مختلف اعداد (1-10، 11-20)
- ⚙️ تنظیمات قابل تنظیم توسط معلم
- ❓ راهنمای داخل بازی

</div>

### English

This game is designed to help improve children's memory and learning. Students enhance their visual memory and number recognition skills by finding matching number pairs.

**Key Features:**
- 🎨 Colorful and engaging UI for children
- 🔊 Persian voiceover to help learn numbers
- 👥 Support for 1-5 players
- 📊 Scoring system with result storage
- 🎯 Different number ranges (1-10, 11-20)
- ⚙️ Teacher-configurable settings
- ❓ In-game help guide

---

## 📥 نصب و راه‌اندازی | Installation

<div dir="rtl">

### فارسی

#### پیش‌نیازها
- Python 3.8 یا بالاتر
- سیستم‌عامل: Windows, macOS, یا Linux

#### مراحل نصب

1. **نصب Python**
   ```bash
   # بررسی نسخه Python
   python --version
   # یا
   python3 --version
   ```

2. **دانلود بازی**
   ```bash
   git clone https://github.com/mahdib1382/kids-memory-game.git
   cd kids-memory-game
   ```

3. **نصب وابستگی‌ها**
   ```bash
   pip install -r requirements.txt
   # یا
   pip3 install -r requirements.txt
   ```

4. **اجرای بازی**
   ```bash
   python main.py
   # یا
   python3 main.py
   ```

#### نکات مهم
- اگر خطای "Module not found" دریافت کردید، مطمئن شوید که وابستگی‌ها را نصب کرده‌اید
- برای فعال‌سازی گوینده فارسی، فایل‌های صوتی را در `assets/voices/` قرار دهید

</div>

### English

#### Prerequisites
- Python 3.8 or higher
- Operating System: Windows, macOS, or Linux

#### Installation Steps

1. **Install Python**
   ```bash
   # Check Python version
   python --version
   # or
   python3 --version
   ```

2. **Download the game**
   ```bash
   git clone https://github.com/mahdib1382/kids-memory-game.git
   cd kids-memory-game
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or
   pip3 install -r requirements.txt
   ```

4. **Run the game**
   ```bash
   python main.py
   # or
   python3 main.py
   ```

#### Important Notes
- If you get "Module not found" error, make sure you installed dependencies
- To enable Persian voiceover, place audio files in `assets/voices/`

---

## 🎯 راهنمای بازی | Game Guide

<div dir="rtl">

### فارسی

#### چگونه بازی کنیم؟

1. **شروع بازی**
   - بازی را اجرا کنید
   - روی دکمه "شروع بازی" کلیک کنید
   - یا ابتدا از "تنظیمات" برای تنظیم بازی استفاده کنید

2. **قوانین بازی**
   - روی یک کارت کلیک کنید تا عدد آن نمایش داده شود
   - روی کارت دیگری کلیک کنید
   - اگر دو عدد یکسان باشند، کارت‌ها باز می‌مانند و امتیاز می‌گیرید
   - اگر متفاوت باشند، کارت‌ها بسته می‌شوند و نوبت بعدی است

3. **تنظیمات**
   - **تعداد بازیکنان**: 1 تا 5 نفر
   - **محدوده اعداد**: اعداد 1-10 یا 11-20
   - **گوینده**: فعال/غیرفعال کردن خواندن اعداد

4. **راهنما**
   - روی دکمه "❓ راهنما" در منوی اصلی کلیک کنید
   - قوانین بازی را به زبان ساده بخوانید

5. **پایان بازی**
   - وقتی تمام جفت‌ها پیدا شدند، برنده اعلام می‌شود
   - نتایج به صورت خودکار ذخیره می‌شوند
   - می‌توانید به منوی اصلی برگردید

#### نکات برای معلمان

- از تنظیمات برای انتخاب سطح مناسب دانش‌آموزان استفاده کنید
- برای کلاس‌های بزرگتر، حالت چند نفره را امتحان کنید
- گوینده را برای دانش‌آموزان ضعیف‌تر فعال کنید
- نتایج ذخیره شده در `game_results.json` را برای پیگیری پیشرفت بررسی کنید

</div>

### English

#### How to Play?

1. **Start the Game**
   - Run the game
   - Click "Start Game" button
   - Or use "Settings" first to configure the game

2. **Game Rules**
   - Click on a card to reveal its number
   - Click on another card
   - If the two numbers match, cards stay open and you score
   - If different, cards close and it's the next turn

3. **Settings**
   - **Number of Players**: 1 to 5 people
   - **Number Range**: Numbers 1-10 or 11-20
   - **Voiceover**: Enable/disable number pronunciation

4. **Help**
   - Click "❓ Help" button in the main menu
   - Read game rules in simple language

5. **End Game**
   - When all pairs are found, winner is announced
   - Results are automatically saved
   - You can return to main menu

#### Tips for Teachers

- Use settings to choose appropriate level for students
- For larger classes, try multiplayer mode
- Enable voiceover for struggling students
- Check saved results in `game_results.json` to track progress

---

## 📁 ساختار پروژه | Project Structure

```
kids-memory-game/
├── main.py                 # فایل اصلی بازی | Main game file
├── PLAN.md                 # برنامه توسعه | Development plan
├── README.md               # این فایل | This file
├── requirements.txt        # وابستگی‌ها | Dependencies
├── game_results.json       # نتایج بازی‌ها | Game results
├── test_phase*.py          # فایل‌های تست | Test files
├── PHASE*_GUIDE.md         # راهنماهای فازها | Phase guides
└── assets/                 # دارایی‌های بازی | Game assets
    ├── textures/           # تصاویر اعداد | Number images
    ├── sounds/             # صداها | Sound effects
    └── voices/             # گوینده فارسی | Persian voiceover
```

---

## 🎨 دارایی‌های بازی | Game Assets

<div dir="rtl">

### فارسی

#### تصاویر (اختیاری)
- مسیر: `assets/textures/`
- فرمت: `{number}.png` (مثلاً `1.png`, `2.png`)
- اندازه توصیه‌شده: 256×256 پیکسل
- پس‌زمینه: شفاف

#### صداها (اختیاری)
- مسیر: `assets/sounds/`
- فایل‌ها:
  - `click.wav` - صدای کلیک کارت
  - `success.mp3` - صدای موفقیت
  - `wrong.wav` - صدای اشتباه

#### گوینده فارسی (اختیاری)
- مسیر: `assets/voices/`
- فرمت: `{number}.mp3` (مثلاً `1.mp3`, `2.mp3`)
- محدوده: اعداد 1 تا 20
- محتوا: "یک"، "دو"، "سه"، ... "بیست"
- صدا: مردانه (ترجیحی)

**توجه:** بازی بدون دارایی‌ها هم کار می‌کند (با متن ساده و بدون صدا)

</div>

### English

#### Images (Optional)
- Path: `assets/textures/`
- Format: `{number}.png` (e.g., `1.png`, `2.png`)
- Recommended size: 256×256 pixels
- Background: Transparent

#### Sounds (Optional)
- Path: `assets/sounds/`
- Files:
  - `click.wav` - Card click sound
  - `success.mp3` - Success sound
  - `wrong.wav` - Wrong sound

#### Persian Voiceover (Optional)
- Path: `assets/voices/`
- Format: `{number}.mp3` (e.g., `1.mp3`, `2.mp3`)
- Range: Numbers 1 to 20
- Content: "یک", "دو", "سه", ... "بیست"
- Voice: Male (preferred)

**Note:** Game works without assets (with plain text and no sound)

---

## 🧪 تست | Testing

<div dir="rtl">

### فارسی

```bash
# تست فاز 2 - منطق بازی
python test_phase2.py

# تست فاز 3 - جلوه‌های بصری و صوتی
python test_phase3.py

# تست فاز 5 - UI/UX
python test_phase5.py

# تست فاز 6 - بهینه‌سازی
python test_phase6.py
```

</div>

### English

```bash
# Test Phase 2 - Game logic
python test_phase2.py

# Test Phase 3 - Visual and audio effects
python test_phase3.py

# Test Phase 5 - UI/UX
python test_phase5.py

# Test Phase 6 - Optimization
python test_phase6.py
```

---

## 📚 مستندات | Documentation

<div dir="rtl">

### فارسی

- **PLAN.md**: برنامه کامل توسعه بازی
- **PHASE2_GUIDE.md**: راهنمای فاز 2 (منطق بازی)
- **PHASE3_GUIDE.md**: راهنمای فاز 3 و 4 (جلوه‌ها)
- **PHASE5_GUIDE.md**: راهنمای فاز 5 (UI/UX)
- **TECHNICAL.md**: مستندات فنی
- **assets/README.md**: راهنمای دارایی‌ها
- **assets/voices/README.md**: راهنمای گوینده

</div>

### English

- **PLAN.md**: Complete game development plan
- **PHASE2_GUIDE.md**: Phase 2 guide (game logic)
- **PHASE3_GUIDE.md**: Phase 3 & 4 guide (effects)
- **PHASE5_GUIDE.md**: Phase 5 guide (UI/UX)
- **TECHNICAL.md**: Technical documentation
- **assets/README.md**: Assets guide
- **assets/voices/README.md**: Voiceover guide

---

## ✨ ویژگی‌ها | Features

<div dir="rtl">

### فارسی

✅ **پایه قوی** - موتور Ursina با تنظیمات بهینه  
✅ **منطق کامل** - تطبیق، نوبت، امتیازدهی  
✅ **جلوه‌های بصری** - انیمیشن‌ها، ذرات، تصاویر  
✅ **جلوه‌های صوتی** - صداهای تعاملی  
✅ **منوی اصلی** - رابط کاربری جذاب  
✅ **تنظیمات پویا** - قابل تنظیم توسط معلم  
✅ **پنل امتیازات** - نمایش لحظه‌ای  
✅ **ذخیره‌سازی** - ثبت نتایج در JSON  
✅ **گوینده فارسی** - خواندن اعداد برای یادگیری  
✅ **راهنمای داخلی** - توضیح قوانین در بازی  
✅ **بهینه‌سازی** - مدیریت حافظه و جلوگیری از اسپم  
✅ **آموزشی** - طراحی شده برای کلاس سوم  
✅ **انعطاف‌پذیر** - 1-5 بازیکن، محدوده‌های مختلف  

</div>

### English

✅ **Strong Foundation** - Ursina engine with optimized settings  
✅ **Complete Logic** - Matching, turns, scoring  
✅ **Visual Effects** - Animations, particles, images  
✅ **Audio Effects** - Interactive sounds  
✅ **Main Menu** - Engaging UI  
✅ **Dynamic Settings** - Teacher-configurable  
✅ **Scoreboard** - Real-time display  
✅ **Storage** - JSON result tracking  
✅ **Persian Voiceover** - Number pronunciation for learning  
✅ **In-game Help** - Rule explanation  
✅ **Optimization** - Memory management and anti-spam  
✅ **Educational** - Designed for 3rd grade  
✅ **Flexible** - 1-5 players, different ranges  

---

## 🔧 سیستم مورد نیاز | System Requirements

<div dir="rtl">

### فارسی

**حداقل:**
- CPU: Intel Core i3 یا معادل
- RAM: 2 GB
- GPU: پشتیبانی از OpenGL 2.1
- فضای دیسک: 100 MB

**توصیه‌شده:**
- CPU: Intel Core i5 یا بالاتر
- RAM: 4 GB یا بیشتر
- GPU: پشتیبانی از OpenGL 3.0+
- فضای دیسک: 200 MB (با دارایی‌ها)

**تست شده روی:**
- Intel Core i7-1165G7
- 8GB RAM
- Windows 10/11

</div>

### English

**Minimum:**
- CPU: Intel Core i3 or equivalent
- RAM: 2 GB
- GPU: OpenGL 2.1 support
- Disk space: 100 MB

**Recommended:**
- CPU: Intel Core i5 or higher
- RAM: 4 GB or more
- GPU: OpenGL 3.0+ support
- Disk space: 200 MB (with assets)

**Tested on:**
- Intel Core i7-1165G7
- 8GB RAM
- Windows 10/11

---

## 🐛 رفع مشکلات | Troubleshooting

<div dir="rtl">

### فارسی

**مشکل: بازی اجرا نمی‌شود**
- بررسی کنید Python نصب است: `python --version`
- وابستگی‌ها را نصب کنید: `pip install -r requirements.txt`

**مشکل: گوینده کار نمی‌کند**
- فایل‌های صوتی را در `assets/voices/` قرار دهید
- از تنظیمات، گوینده را فعال کنید
- فرمت فایل‌ها MP3 باشد

**مشکل: تصاویر نمایش داده نمی‌شوند**
- تصاویر را در `assets/textures/` قرار دهید
- فرمت PNG با نام‌گذاری `{number}.png` باشد
- بازی با متن ساده هم کار می‌کند

**مشکل: خطای "Module not found"**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

</div>

### English

**Problem: Game doesn't run**
- Check Python is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`

**Problem: Voiceover doesn't work**
- Place audio files in `assets/voices/`
- Enable voiceover in settings
- Files must be MP3 format

**Problem: Images don't show**
- Place images in `assets/textures/`
- Format: PNG with naming `{number}.png`
- Game works with plain text too

**Problem: "Module not found" error**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🤝 مشارکت | Contributing

<div dir="rtl">

این پروژه برای اهداف آموزشی ساخته شده است. برای گزارش مشکلات یا پیشنهادات، لطفاً یک Issue در GitHub ایجاد کنید.

</div>

This project is created for educational purposes. To report issues or suggestions, please create an Issue on GitHub.

---

## 📄 مجوز | License

<div dir="rtl">

این پروژه برای استفاده آموزشی آزاد است.

</div>

This project is free for educational use.

---

## 👨‍💻 سازنده | Author

**Mahdi B.**  
GitHub: [@mahdib1382](https://github.com/mahdib1382)

---

## 🎓 استفاده در کلاس | Classroom Use

<div dir="rtl">

### فارسی

این بازی به طور خاص برای استفاده در کلاس‌های دوره ابتدایی (کلاس سوم) طراحی شده است:

- **یادگیری اعداد**: گوینده فارسی به دانش‌آموزان کمک می‌کند اعداد را یاد بگیرند
- **تقویت حافظه**: بازی به تقویت حافظه بصری کمک می‌کند
- **کار گروهی**: حالت چند نفره، همکاری را تشویق می‌کند
- **تنظیمات معلم**: معلم می‌تواند سطح بازی را متناسب با دانش‌آموزان تنظیم کند
- **پیگیری پیشرفت**: نتایج ذخیره شده برای ارزیابی مفید است

**پیشنهاد برای معلمان:**
1. ابتدا با محدوده 1-10 و تک‌نفره شروع کنید
2. پس از تسلط، به محدوده 11-20 بروید
3. برای انگیزه بیشتر، حالت چند نفره را امتحان کنید
4. گوینده را برای دانش‌آموزان ضعیف‌تر فعال کنید

</div>

### English

This game is specifically designed for elementary classroom use (3rd grade):

- **Number Learning**: Persian voiceover helps students learn numbers
- **Memory Enhancement**: Game helps improve visual memory
- **Teamwork**: Multiplayer mode encourages cooperation
- **Teacher Settings**: Teachers can adjust game level for students
- **Progress Tracking**: Saved results useful for assessment

**Suggestions for Teachers:**
1. Start with range 1-10 and single player
2. After mastery, move to range 11-20
3. Try multiplayer mode for more motivation
4. Enable voiceover for struggling students

---

<div align="center" dir="rtl">

### 🎉 بازی آماده برای استفاده در کلاس است! | Game Ready for Classroom Use! 🎉

**نسخه | Version: 1.0**  
**تاریخ | Date: 2026-02-01**

</div>
