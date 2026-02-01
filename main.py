"""
بازی حافظه کودکان (Kids Memory Game)
نسخه 1.0
یک بازی آموزشی برای کمک به یادگیری اعداد برای دانش‌آموزان کلاس سوم
"""

from ursina import *
from pathlib import Path
import os
import sys
import json
import time
from datetime import datetime

# تابع برای دریافت مسیر صحیح فایل‌ها (برای فایل اجرایی)
def get_resource_path(relative_path):
    """دریافت مسیر صحیح برای فایل‌ها (برای PyInstaller)"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# متغیر سراسری برای مدیر بازی (برای دسترسی از کارت‌ها)
game_manager = None
game_menu = None
current_settings = {'num_players': 2, 'level_start': 1, 'num_pairs': 6, 'voiceover_enabled': True}


class DataManager:
    """
    مدیر ذخیره‌سازی داده‌ها در JSON
    """
    def __init__(self, filename='game_results.json'):
        self.filename = filename
        # برای فایل JSON، از پوشه جاری استفاده می‌کنیم نه _MEIPASS
        # تا داده‌ها در کنار فایل اجرایی ذخیره شوند
        self.filepath = Path(os.path.join(os.getcwd(), filename))
    
    def save_game_result(self, winner, game_time, num_players, scores):
        """ذخیره نتیجه بازی"""
        try:
            # خواندن داده‌های قبلی
            if self.filepath.exists():
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = {'games': []}
            
            # اضافه کردن بازی جدید
            game_result = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'winner': winner,
                'game_time': round(game_time, 2),
                'num_players': num_players,
                'scores': scores
            }
            
            data['games'].append(game_result)
            
            # ذخیره در فایل
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"✅ نتیجه بازی ذخیره شد: {self.filename}")
        except Exception as e:
            print(f"⚠️ خطا در ذخیره نتیجه: {e}")
    
    def get_recent_games(self, count=10):
        """دریافت آخرین بازی‌ها"""
        try:
            if self.filepath.exists():
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data['games'][-count:]
            return []
        except:
            return []


class VoiceoverManager:
    """
    مدیر گوینده برای خواندن اعداد به فارسی
    """
    def __init__(self):
        self.voices = {}
        self.enabled = True
        self.load_voiceovers()
    
    def load_voiceovers(self):
        """بارگذاری فایل‌های صوتی اعداد"""
        voice_path = Path(get_resource_path('assets/voices'))
        if voice_path.exists():
            # بارگذاری اعداد 1 تا 20
            for i in range(1, 21):
                voice_file = voice_path / f'{i}.mp3'
                if voice_file.exists():
                    try:
                        self.voices[i] = Audio(str(voice_file), loop=False, autoplay=False)
                    except:
                        pass
    
    def speak_number(self, number):
        """پخش صدای عدد"""
        if self.enabled and number in self.voices:
            try:
                self.voices[number].play()
            except:
                pass
    
    def set_enabled(self, enabled):
        """فعال/غیرفعال کردن گوینده"""
        self.enabled = enabled


class GameMenu(Entity):
    """
    منوی اصلی بازی
    """
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.title = None
        self.create_menu()
    
    def create_menu(self):
        """ایجاد منوی اصلی"""
        # عنوان
        self.title = Text(
            text='🎮 بازی حافظه کودکان 🎮',
            position=(0, 0.35),
            origin=(0, 0),
            scale=3,
            color=color.yellow
        )
        
        # دکمه شروع بازی
        start_btn = Button(
            text='▶ شروع بازی',
            color=color.rgb(100, 200, 100),
            scale=(0.3, 0.1),
            position=(0, 0.10),
            on_click=self.start_game
        )
        start_btn.text_entity.scale = 2
        self.buttons.append(start_btn)
        
        # دکمه راهنما
        help_btn = Button(
            text='❓ راهنما',
            color=color.rgb(200, 150, 100),
            scale=(0.3, 0.1),
            position=(0, -0.05),
            on_click=self.show_help
        )
        help_btn.text_entity.scale = 2
        self.buttons.append(help_btn)
        
        # دکمه تنظیمات
        settings_btn = Button(
            text='⚙ تنظیمات',
            color=color.rgb(100, 150, 200),
            scale=(0.3, 0.1),
            position=(0, -0.20),
            on_click=self.show_settings
        )
        settings_btn.text_entity.scale = 2
        self.buttons.append(settings_btn)
        
        # دکمه خروج
        exit_btn = Button(
            text='✖ خروج',
            color=color.rgb(200, 100, 100),
            scale=(0.3, 0.1),
            position=(0, -0.35),
            on_click=application.quit
        )
        exit_btn.text_entity.scale = 2
        self.buttons.append(exit_btn)
    
    def start_game(self):
        """شروع بازی جدید"""
        global game_manager
        self.hide()
        
        # ایجاد مدیر بازی با تنظیمات فعلی
        game_manager = GameManager(
            num_pairs=current_settings['num_pairs'],
            num_players=current_settings['num_players'],
            level_start=current_settings['level_start'],
            voiceover_enabled=current_settings['voiceover_enabled']
        )
    
    def show_settings(self):
        """نمایش منوی تنظیمات"""
        self.hide()
        settings_menu = SettingsMenu()
    
    def show_help(self):
        """نمایش راهنمای بازی"""
        self.hide()
        help_window = HelpWindow()
    
    def hide(self):
        """مخفی کردن منو"""
        if self.title:
            self.title.enabled = False
        for btn in self.buttons:
            btn.enabled = False
    
    def show(self):
        """نمایش منو"""
        if self.title:
            self.title.enabled = True
        for btn in self.buttons:
            btn.enabled = True


class SettingsMenu(Entity):
    """
    منوی تنظیمات بازی
    """
    def __init__(self):
        super().__init__()
        self.ui_elements = []
        self.create_settings()
    
    def create_settings(self):
        """ایجاد منوی تنظیمات"""
        # عنوان
        title = Text(
            text='⚙ تنظیمات',
            position=(0, 0.35),
            origin=(0, 0),
            scale=2.5,
            color=color.cyan
        )
        self.ui_elements.append(title)
        
        # تنظیم تعداد بازیکنان
        players_text = Text(
            text=f'تعداد بازیکنان: {current_settings["num_players"]}',
            position=(-0.35, 0.15),
            origin=(0, 0),
            scale=1.5,
            color=color.white
        )
        self.ui_elements.append(players_text)
        
        players_minus = Button(
            text='−',
            color=color.red,
            scale=(0.08, 0.08),
            position=(-0.1, 0.15),
            on_click=Func(self.change_players, -1, players_text)
        )
        players_minus.text_entity.scale = 2
        self.ui_elements.append(players_minus)
        
        players_plus = Button(
            text='+',
            color=color.green,
            scale=(0.08, 0.08),
            position=(0, 0.15),
            on_click=Func(self.change_players, 1, players_text)
        )
        players_plus.text_entity.scale = 2
        self.ui_elements.append(players_plus)
        
        # تنظیم محدوده اعداد
        level_text = Text(
            text=f'محدوده اعداد: {current_settings["level_start"]}-{current_settings["level_start"]+current_settings["num_pairs"]-1}',
            position=(-0.35, 0.0),
            origin=(0, 0),
            scale=1.5,
            color=color.white
        )
        self.ui_elements.append(level_text)
        
        level_options = ['1-10', '11-20']
        level_btn = Button(
            text='تغییر محدوده',
            color=color.orange,
            scale=(0.2, 0.08),
            position=(0.05, 0.0),
            on_click=Func(self.cycle_level, level_text)
        )
        level_btn.text_entity.scale = 1.5
        self.ui_elements.append(level_btn)
        
        # تنظیم گوینده
        voiceover_text = Text(
            text=f'گوینده: {"فعال" if current_settings["voiceover_enabled"] else "غیرفعال"}',
            position=(-0.35, -0.15),
            origin=(0, 0),
            scale=1.5,
            color=color.white
        )
        self.ui_elements.append(voiceover_text)
        
        voiceover_btn = Button(
            text='تغییر',
            color=color.magenta,
            scale=(0.15, 0.08),
            position=(0.05, -0.15),
            on_click=Func(self.toggle_voiceover, voiceover_text)
        )
        voiceover_btn.text_entity.scale = 1.5
        self.ui_elements.append(voiceover_btn)
        
        # دکمه بازگشت
        back_btn = Button(
            text='↩ بازگشت',
            color=color.gray,
            scale=(0.2, 0.08),
            position=(0, -0.35),
            on_click=self.back_to_menu
        )
        back_btn.text_entity.scale = 1.5
        self.ui_elements.append(back_btn)
    
    def change_players(self, delta, text_obj):
        """تغییر تعداد بازیکنان"""
        current_settings['num_players'] = max(1, min(5, current_settings['num_players'] + delta))
        text_obj.text = f'تعداد بازیکنان: {current_settings["num_players"]}'
    
    def cycle_level(self, text_obj):
        """چرخش محدوده اعداد"""
        if current_settings['level_start'] == 1:
            current_settings['level_start'] = 11
            current_settings['num_pairs'] = 10
        else:
            current_settings['level_start'] = 1
            current_settings['num_pairs'] = 6
        
        text_obj.text = f'محدوده اعداد: {current_settings["level_start"]}-{current_settings["level_start"]+current_settings["num_pairs"]-1}'
    
    def toggle_voiceover(self, text_obj):
        """تغییر وضعیت گوینده"""
        current_settings['voiceover_enabled'] = not current_settings['voiceover_enabled']
        text_obj.text = f'گوینده: {"فعال" if current_settings["voiceover_enabled"] else "غیرفعال"}'
    
    def back_to_menu(self):
        """بازگشت به منوی اصلی"""
        global game_menu
        self.destroy()
        if game_menu:
            game_menu.show()
    
    def destroy(self):
        """حذف منوی تنظیمات"""
        for elem in self.ui_elements:
            destroy(elem)


class HelpWindow(Entity):
    """
    پنجره راهنمای بازی
    """
    def __init__(self):
        super().__init__()
        self.ui_elements = []
        self.create_help()
    
    def create_help(self):
        """ایجاد پنجره راهنما"""
        # عنوان
        title = Text(
            text='❓ راهنمای بازی',
            position=(0, 0.40),
            origin=(0, 0),
            scale=2.5,
            color=color.orange
        )
        self.ui_elements.append(title)
        
        # قوانین بازی به زبان ساده برای دانش‌آموزان
        rules_lines = [
            '📌 هدف بازی:',
            'پیدا کردن جفت کارت‌های یکسان',
            '',
            '🎮 نحوه بازی:',
            '۱. روی یک کارت کلیک کن تا عدد آن را ببینی',
            '۲. روی کارت دیگری کلیک کن',
            '۳. اگر دو عدد یکسان باشند، کارت‌ها می‌مانند',
            '۴. اگر متفاوت باشند، دوباره پنهان می‌شوند',
            '',
            '⭐ نکات مهم:',
            '• سعی کن جای اعداد را یادت بماند',
            '• با هر جفت درست، امتیاز می‌گیری',
            '• در بازی چند نفره، نوبت‌ها عوض می‌شود',
            '',
            '🎯 بازنده نداریم! همه یاد می‌گیرند! 🎯'
        ]
        
        y_position = 0.25
        for line in rules_lines:
            if line.startswith('📌') or line.startswith('🎮') or line.startswith('⭐'):
                # عناوین اصلی
                scale = 1.8
                text_color = color.yellow
            elif line.startswith('🎯'):
                # پیام پایانی
                scale = 1.6
                text_color = color.green
            else:
                # متن عادی
                scale = 1.3
                text_color = color.white
            
            rule_text = Text(
                text=line,
                position=(0, y_position),
                origin=(0, 0),
                scale=scale,
                color=text_color
            )
            self.ui_elements.append(rule_text)
            y_position -= 0.055  # فاصله بین خطوط
        
        # دکمه بستن
        close_btn = Button(
            text='✓ فهمیدم!',
            color=color.rgb(100, 200, 100),
            scale=(0.25, 0.08),
            position=(0, -0.42),
            on_click=self.close_help
        )
        close_btn.text_entity.scale = 1.8
        self.ui_elements.append(close_btn)
    
    def close_help(self):
        """بستن پنجره راهنما"""
        global game_menu
        self.destroy()
        if game_menu:
            game_menu.show()
    
    def destroy(self):
        """حذف پنجره راهنما"""
        for elem in self.ui_elements:
            destroy(elem)


class AudioManager:
    """
    مدیر صداها برای پخش جلوه‌های صوتی
    """
    def __init__(self):
        self.sounds = {}
        self.load_sounds()
    
    def load_sounds(self):
        """بارگذاری فایل‌های صوتی از پوشه assets/sounds"""
        sounds_path = Path(get_resource_path('assets/sounds'))
        if sounds_path.exists():
            # بارگذاری صداها
            sound_files = {
                'click': 'click.wav',
                'success': 'success.mp3',
                'wrong': 'wrong.wav'
            }
            
            for sound_name, filename in sound_files.items():
                sound_file = sounds_path / filename
                if sound_file.exists():
                    try:
                        self.sounds[sound_name] = Audio(str(sound_file), loop=False, autoplay=False)
                    except:
                        print(f"⚠️ نمی‌توان صدای {filename} را بارگذاری کرد")
    
    def play(self, sound_name):
        """پخش یک صدای خاص"""
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except:
                pass  # در صورت خطا، بی‌صدا ادامه می‌دهیم


class ConfettiParticle(Entity):
    """
    یک ذره رنگی برای جشن موفقیت
    """
    def __init__(self, position, **kwargs):
        import random
        
        # انتخاب رنگ تصادفی
        colors = [color.yellow, color.orange, color.pink, color.cyan, color.lime, color.magenta]
        particle_color = random.choice(colors)
        
        super().__init__(
            model='quad',
            color=particle_color,
            position=position,
            scale=0.15,
            **kwargs
        )
        
        # سرعت اولیه تصادفی
        self.velocity = Vec3(
            random.uniform(-3, 3),
            random.uniform(3, 6),
            random.uniform(-1, 1)
        )
        
        # شتاب گرانش
        self.gravity = -15
        
        # زمان زندگی
        self.lifetime = 1.5
        self.age = 0
    
    def update(self):
        """به‌روزرسانی موقعیت ذره"""
        dt = time.dt
        self.age += dt
        
        if self.age >= self.lifetime:
            destroy(self)
            return
        
        # اعمال گرانش
        self.velocity.y += self.gravity * dt
        
        # به‌روزرسانی موقعیت
        self.position += self.velocity * dt
        
        # چرخش
        self.rotation_z += 360 * dt
        
        # محو شدن
        self.color = color.rgba(
            self.color.r * 255,
            self.color.g * 255,
            self.color.b * 255,
            int(255 * (1 - self.age / self.lifetime))
        )


class NumberCard(Entity):
    """
    کلاس کارت با قابلیت چرخش، نمایش عدد، و تصاویر
    """
    def __init__(self, number, position=(0, 0), **kwargs):
        super().__init__(
            model='quad',
            color=color.azure,
            position=(position[0], position[1], 0),
            scale=(1.5, 2),
            collider='box',
            **kwargs
        )
        
        self.number = number
        self.is_flipped = False
        self.is_matched = False
        
        # بارگذاری تصویر اگر موجود باشد
        self.number_texture = self._load_texture(number)
        
        # اگر تصویر موجود نیست، از متن استفاده می‌کنیم
        if self.number_texture:
            # ایجاد Entity برای نمایش تصویر
            self.number_image = Entity(
                model='quad',
                texture=self.number_texture,
                parent=self,
                position=(0, 0, -0.01),
                scale=(1.2, 1.2),
                enabled=False
            )
            self.number_text = None
        else:
            # استفاده از متن با خوانایی بهتر
            self.number_image = None
            self.number_text = Text(
                text=str(number),
                parent=self,
                position=(0, 0, -0.01),
                scale=4,  # افزایش اندازه برای خوانایی بهتر
                origin=(0, 0),
                color=color.black,
                enabled=False,
                font='assets/fonts/Arial.ttf'  # فونت واضح‌تر
            )
        
        # متن پشت کارت (علامت سوال) با خوانایی بهتر
        self.back_text = Text(
            text='?',
            parent=self,
            position=(0, 0, -0.01),
            scale=4,  # افزایش اندازه
            origin=(0, 0),
            color=color.white,
            enabled=True
        )
    
    def _load_texture(self, number):
        """بارگذاری تصویر عدد از پوشه assets/textures"""
        texture_path = Path(get_resource_path(f'assets/textures/{number}.png'))
        if texture_path.exists():
            try:
                return load_texture(str(texture_path))
            except:
                return None
        return None
    
    def input(self, key):
        """مدیریت کلیک روی کارت"""
        if self.hovered and key == 'left mouse down':
            if not self.is_flipped and not self.is_matched:
                # بررسی اینکه آیا بازی قفل است (در حال پردازش)
                if game_manager and not game_manager.is_processing:
                    # قفل کردن بازی در حین انیمیشن چرخش (0.3 ثانیه)
                    game_manager.is_processing = True
                    
                    # پخش صدای کلیک
                    if game_manager.audio_manager:
                        game_manager.audio_manager.play('click')
                    
                    self.flip()
                    
                    # باز کردن قفل بعد از اتمام انیمیشن چرخش
                    invoke(lambda: self._unlock_after_flip(), delay=0.3)
                    
                    # اطلاع به مدیر بازی که کارت باز شد
                    if game_manager:
                        game_manager.on_card_flipped(self)
    
    def _unlock_after_flip(self):
        """باز کردن قفل بازی بعد از اتمام انیمیشن چرخش"""
        if game_manager:
            # فقط اگر دو کارت باز نشده باشد، قفل را باز کن
            # اگر دو کارت باز شده، check_match مسئول باز کردن قفل است
            if len(game_manager.flipped_cards) < 2:
                game_manager.is_processing = False
    
    def flip(self):
        """چرخش کارت با انیمیشن نرم"""
        if self.is_matched:
            return
            
        self.is_flipped = not self.is_flipped
        
        # انیمیشن چرخش
        if self.is_flipped:
            # چرخش برای نمایش عدد
            self.animate_scale_x(0, duration=0.15, curve=curve.in_out_expo)
            invoke(self._show_number, delay=0.15)
            invoke(lambda: self.animate_scale_x(1.5, duration=0.15, curve=curve.in_out_expo), delay=0.15)
        else:
            # چرخش برای پنهان کردن عدد
            self.animate_scale_x(0, duration=0.15, curve=curve.in_out_expo)
            invoke(self._hide_number, delay=0.15)
            invoke(lambda: self.animate_scale_x(1.5, duration=0.15, curve=curve.in_out_expo), delay=0.15)
    
    def _show_number(self):
        """نمایش عدد و مخفی کردن پشت کارت"""
        if self.number_image:
            self.number_image.enabled = True
        if self.number_text:
            self.number_text.enabled = True
        self.back_text.enabled = False
        self.color = color.white
        
        # پخش گوینده برای عدد
        if game_manager and game_manager.voiceover_manager:
            game_manager.voiceover_manager.speak_number(self.number)
    
    def _hide_number(self):
        """مخفی کردن عدد و نمایش پشت کارت"""
        if self.number_image:
            self.number_image.enabled = False
        if self.number_text:
            self.number_text.enabled = False
        self.back_text.enabled = True
        self.color = color.azure
    
    def mark_as_matched(self):
        """
        علامت‌گذاری کارت به عنوان جفت شده با انیمیشن جذاب
        """
        self.is_matched = True
        self.color = color.green
        
        # انیمیشن پرش و کوچک شدن با curve.out_back
        original_scale = self.scale
        
        # مرحله 1: بزرگ شدن کمی (bounce)
        self.animate_scale(
            original_scale * 1.3,
            duration=0.15,
            curve=curve.out_back
        )
        
        # مرحله 2: برگشت به اندازه نرمال
        invoke(
            lambda: self.animate_scale(
                original_scale,
                duration=0.15,
                curve=curve.in_out_expo
            ),
            delay=0.15
        )
        
        # مرحله 3: کوچک شدن و محو
        invoke(
            lambda: self.animate_scale(
                0,
                duration=0.4,
                curve=curve.in_out_expo
            ),
            delay=0.4
        )
        
        # غیرفعال کردن کارت
        invoke(self.disable, delay=0.8)


class GameManager:
    """
    مدیر بازی که کارت‌ها، نوبت‌ها و امتیازات را مدیریت می‌کند
    """
    def __init__(self, num_pairs=6, num_players=1, level_start=1, voiceover_enabled=True):
        self.num_pairs = num_pairs
        self.num_players = max(1, min(5, num_players))  # محدود به 1-5 بازیکن
        self.level_start = level_start  # شروع محدوده سطح (مثلاً 1 برای 1-10)
        
        # مدیریت کارت‌ها
        self.cards = []
        self.flipped_cards = []
        
        # مدیریت نوبت و امتیاز
        self.current_player = 0  # شماره بازیکن فعلی (0-based)
        self.scores = [0] * self.num_players  # امتیاز هر بازیکن
        self.total_matches = 0  # تعداد جفت‌های پیدا شده
        
        # قفل برای جلوگیری از کلیک در حین پردازش
        self.is_processing = False
        
        # زمان شروع بازی
        self.start_time = time.time()
        
        # UI elements
        self.ui_texts = []
        
        # مدیر صداها
        self.audio_manager = AudioManager()
        
        # مدیر گوینده
        self.voiceover_manager = VoiceoverManager()
        self.voiceover_manager.set_enabled(voiceover_enabled)
        
        # مدیر ذخیره‌سازی داده‌ها
        self.data_manager = DataManager()
        
        # ایجاد کارت‌ها
        self.create_cards()
        
        # ایجاد UI
        self.create_ui()
        
        # ایجاد Scoreboard
        self.create_scoreboard()
    
    def create_cards(self):
        """ایجاد و چیدمان کارت‌ها به صورت Grid"""
        # تعداد کارت‌ها (هر عدد دو بار) با استفاده از محدوده سطح
        numbers = list(range(self.level_start, self.level_start + self.num_pairs)) * 2
        
        # مخلوط کردن کارت‌ها
        from random import shuffle
        shuffle(numbers)
        
        # محاسبه تعداد ردیف و ستون بر اساس تعداد کارت‌ها
        total_cards = len(numbers)
        
        # بهینه‌سازی ابعاد Grid
        if total_cards <= 12:
            cols = 4
        elif total_cards <= 20:
            cols = 5
        else:
            cols = 6
        
        rows = (total_cards + cols - 1) // cols  # سقف تقسیم
        
        # فاصله بین کارت‌ها
        spacing_x = 2
        spacing_y = 2.5
        
        # محاسبه موقعیت شروع برای مرکزیت
        start_x = -(cols - 1) * spacing_x / 2
        start_y = (rows - 1) * spacing_y / 2
        
        # ایجاد کارت‌ها
        idx = 0
        for row in range(rows):
            for col in range(cols):
                if idx >= total_cards:
                    break
                
                x = start_x + col * spacing_x
                y = start_y - row * spacing_y
                
                card = NumberCard(
                    number=numbers[idx],
                    position=(x, y)
                )
                self.cards.append(card)
                idx += 1
    
    def create_ui(self):
        """ایجاد المان‌های رابط کاربری"""
        # نمایش امتیازات بازیکنان
        y_pos = 0.45
        for i in range(self.num_players):
            player_text = Text(
                text=f'بازیکن {i+1}: 0',
                position=(-0.85, y_pos - i * 0.08),
                scale=1.5,
                color=color.white,
                origin=(0, 0)
            )
            self.ui_texts.append(player_text)
        
        # نمایش نوبت فعلی
        self.turn_text = Text(
            text=f'نوبت: بازیکن 1',
            position=(0.6, 0.45),
            scale=2,
            color=color.yellow,
            origin=(0, 0)
        )
        
        # نمایش محدوده سطح
        level_end = self.level_start + self.num_pairs - 1
        self.level_text = Text(
            text=f'سطح: {self.level_start}-{level_end}',
            position=(0, 0.45),
            scale=2,
            color=color.cyan,
            origin=(0, 0)
        )
        
        # نمایش بازخورد (شروع مخفی)
        self.feedback_text = Text(
            text='',
            position=(0, -0.45),
            scale=2.5,
            color=color.green,
            origin=(0, 0),
            enabled=False
        )
    
    def create_scoreboard(self):
        """ایجاد پنل امتیازات لحظه‌ای"""
        # پس‌زمینه Scoreboard
        self.scoreboard_bg = Entity(
            model='quad',
            color=color.rgba(0, 0, 0, 150),
            scale=(0.35, 0.15 + 0.08 * self.num_players),
            position=(0.75, 0.35),
            z=1
        )
        
        # عنوان Scoreboard
        self.scoreboard_title = Text(
            text='🏆 امتیازات',
            position=(0.75, 0.42),
            scale=1.8,
            color=color.gold,
            origin=(0, 0),
            z=0
        )
    
    def on_card_flipped(self, card):
        """
        رویداد وقتی یک کارت باز می‌شود
        """
        # اضافه کردن به لیست کارت‌های باز شده
        self.flipped_cards.append(card)
        
        # اگر دو کارت باز شد، بررسی تطبیق
        if len(self.flipped_cards) == 2:
            # is_processing قبلاً در input تنظیم شده
            invoke(self.check_match, delay=0.5)  # کمی صبر برای نمایش کارت دوم
    
    def check_match(self):
        """
        بررسی تطبیق دو کارت باز شده
        """
        card1, card2 = self.flipped_cards
        
        if card1.number == card2.number:
            # جفت درست! 
            self.on_match_success(card1, card2)
        else:
            # جفت نادرست
            self.on_match_failure(card1, card2)
    
    def on_match_success(self, card1, card2):
        """
        رویداد موفقیت در تطبیق (جفت درست)
        """
        # پخش صدای موفقیت
        if self.audio_manager:
            self.audio_manager.play('success')
        
        # ایجاد ذرات جشن (confetti)
        self.spawn_confetti(card1.position)
        self.spawn_confetti(card2.position)
        
        # علامت‌گذاری کارت‌ها به عنوان جفت شده
        card1.mark_as_matched()
        card2.mark_as_matched()
        
        # افزایش امتیاز بازیکن فعلی
        self.scores[self.current_player] += 1
        self.total_matches += 1
        
        # به‌روزرسانی UI
        self.update_ui()
        
        # نمایش بازخورد مثبت
        self.show_feedback('عالی! ✓', color.green, 1.0)
        
        # پاک کردن لیست کارت‌های باز
        self.flipped_cards = []
        
        # باز کردن قفل
        self.is_processing = False
        
        # بررسی پایان بازی
        if self.total_matches == self.num_pairs:
            invoke(self.game_over, delay=1.0)
    
    def spawn_confetti(self, position):
        """
        ایجاد ذرات جشن در موقعیت مشخص
        """
        import random
        # ایجاد 8-12 ذره
        num_particles = random.randint(8, 12)
        for _ in range(num_particles):
            ConfettiParticle(position=position)
    
    def on_match_failure(self, card1, card2):
        """
        رویداد شکست در تطبیق (جفت نادرست)
        """
        # پخش صدای اشتباه
        if self.audio_manager:
            self.audio_manager.play('wrong')
        
        # نمایش بازخورد منفی
        self.show_feedback('تلاش دوباره! ✗', color.red, 1.5)
        
        # صبر 1.5 ثانیه تا کودک یاد بگیرد
        invoke(lambda: self.hide_cards(card1, card2), delay=1.5)
        
        # تغییر نوبت به بازیکن بعدی
        self.next_turn()
    
    def hide_cards(self, card1, card2):
        """
        پنهان کردن دو کارت نامطابق
        """
        card1.flip()
        card2.flip()
        
        # پاک کردن لیست کارت‌های باز
        self.flipped_cards = []
        
        # باز کردن قفل
        self.is_processing = False
    
    def next_turn(self):
        """
        رفتن به نوبت بازیکن بعدی
        """
        self.current_player = (self.current_player + 1) % self.num_players
        self.update_ui()
    
    def update_ui(self):
        """
        به‌روزرسانی رابط کاربری
        """
        # به‌روزرسانی امتیازات
        for i in range(self.num_players):
            highlight = ' ←' if i == self.current_player else ''
            self.ui_texts[i].text = f'بازیکن {i+1}: {self.scores[i]}{highlight}'
            
            # رنگ‌آمیزی بازیکن فعلی
            if i == self.current_player:
                self.ui_texts[i].color = color.yellow
            else:
                self.ui_texts[i].color = color.white
        
        # به‌روزرسانی نوبت
        self.turn_text.text = f'نوبت: بازیکن {self.current_player + 1}'
    
    def show_feedback(self, message, feedback_color, duration):
        """
        نمایش پیام بازخورد به کاربر
        """
        self.feedback_text.text = message
        self.feedback_text.color = feedback_color
        self.feedback_text.enabled = True
        
        # مخفی کردن پس از مدت زمان مشخص
        invoke(self.hide_feedback, delay=duration)
    
    def hide_feedback(self):
        """
        مخفی کردن پیام بازخورد
        """
        self.feedback_text.enabled = False
    
    def game_over(self):
        """
        پایان بازی و نمایش برنده
        """
        # محاسبه زمان بازی
        game_time = time.time() - self.start_time
        
        # پیدا کردن برنده (بیشترین امتیاز)
        max_score = max(self.scores)
        winners = [i+1 for i, score in enumerate(self.scores) if score == max_score]
        
        if len(winners) == 1:
            message = f'🎉 بازیکن {winners[0]} برنده شد! 🎉'
            winner_str = f'بازیکن {winners[0]}'
        else:
            winners_str = ', '.join(str(w) for w in winners)
            message = f'🎉 مساوی! بازیکنان {winners_str} 🎉'
            winner_str = f'مساوی ({winners_str})'
        
        # ذخیره نتیجه در JSON
        self.data_manager.save_game_result(
            winner=winner_str,
            game_time=game_time,
            num_players=self.num_players,
            scores=self.scores
        )
        
        # نمایش پیام و دکمه بازگشت
        self.show_feedback(message, color.gold, 10.0)
        
        # دکمه بازگشت به منو
        invoke(self.show_back_button, delay=2.0)
    
    def show_back_button(self):
        """نمایش دکمه بازگشت به منو"""
        self.back_btn = Button(
            text='🏠 بازگشت به منو',
            color=color.rgb(100, 150, 200),
            scale=(0.3, 0.1),
            position=(0, -0.3),
            on_click=self.return_to_menu
        )
        self.back_btn.text_entity.scale = 2
    
    def return_to_menu(self):
        """بازگشت به منوی اصلی"""
        global game_manager, game_menu
        
        # حذف تمام ذرات confetti که ممکن است باقی مانده باشند
        # جستجو و حذف تمام اشیاء ConfettiParticle
        for entity in scene.entities[:]:  # کپی لیست برای جلوگیری از تغییر در حین حلقه
            if isinstance(entity, ConfettiParticle):
                destroy(entity)
        
        # حذف تمام کارت‌ها
        for card in self.cards:
            # حذف تصاویر و متن‌های مرتبط با کارت
            if hasattr(card, 'number_image') and card.number_image:
                destroy(card.number_image)
            if hasattr(card, 'number_text') and card.number_text:
                destroy(card.number_text)
            if hasattr(card, 'back_text') and card.back_text:
                destroy(card.back_text)
            destroy(card)
        
        # حذف UI elements
        for ui_text in self.ui_texts:
            destroy(ui_text)
        
        destroy(self.turn_text)
        destroy(self.level_text)
        destroy(self.feedback_text)
        destroy(self.scoreboard_bg)
        destroy(self.scoreboard_title)
        
        if hasattr(self, 'back_btn'):
            destroy(self.back_btn)
        
        # پاکسازی لیست‌ها
        self.cards.clear()
        self.ui_texts.clear()
        self.flipped_cards.clear()
        
        # بازگشت به منو
        game_manager = None
        if game_menu:
            game_menu.show()
    
    def update(self):
        """
        به‌روزرسانی وضعیت بازی در هر فریم
        """
        pass


def setup_window():
    """تنظیمات پنجره و محیط بازی"""
    window.title = 'بازی حافظه کودکان'
    window.borderless = False
    window.fullscreen = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False
    
    # تنظیمات دوربین
    camera.orthographic = True
    camera.fov = 20


def main():
    """تابع اصلی اجرای برنامه"""
    global game_manager, game_menu
    
    # راه‌اندازی موتور Ursina
    app = Ursina()
    
    # تنظیمات پنجره و دوربین
    setup_window()
    
    # تنظیم رنگ پس‌زمینه
    window.color = color.rgb(40, 40, 60)
    
    # ایجاد منوی اصلی
    game_menu = GameMenu()
    
    # اجرای برنامه
    app.run()


if __name__ == '__main__':
    main()
