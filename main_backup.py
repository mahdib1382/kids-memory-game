"""
بازی حافظه کودکان (Kids Memory Game)
فاز سوم و چهارم: جلوه‌های بصری، صداگذاری، و ذرات
"""

from ursina import *
from pathlib import Path
import os

# متغیر سراسری برای مدیر بازی (برای دسترسی از کارت‌ها)
game_manager = None


class AudioManager:
    """
    مدیر صداها برای پخش جلوه‌های صوتی
    """
    def __init__(self):
        self.sounds = {}
        self.load_sounds()
    
    def load_sounds(self):
        """بارگذاری فایل‌های صوتی از پوشه assets/sounds"""
        sounds_path = Path('assets/sounds')
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
        texture_path = Path(f'assets/textures/{number}.png')
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
                    # پخش صدای کلیک
                    if game_manager.audio_manager:
                        game_manager.audio_manager.play('click')
                    
                    self.flip()
                    # اطلاع به مدیر بازی که کارت باز شد
                    if game_manager:
                        game_manager.on_card_flipped(self)
    
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
    def __init__(self, num_pairs=6, num_players=1, level_start=1):
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
        
        # UI elements
        self.ui_texts = []
        
        # مدیر صداها
        self.audio_manager = AudioManager()
        
        # ایجاد کارت‌ها
        self.create_cards()
        
        # ایجاد UI
        self.create_ui()
    
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
    
    def on_card_flipped(self, card):
        """
        رویداد وقتی یک کارت باز می‌شود
        """
        # اضافه کردن به لیست کارت‌های باز شده
        self.flipped_cards.append(card)
        
        # اگر دو کارت باز شد، بررسی تطبیق
        if len(self.flipped_cards) == 2:
            self.is_processing = True  # قفل کردن بازی
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
        # پیدا کردن برنده (بیشترین امتیاز)
        max_score = max(self.scores)
        winners = [i+1 for i, score in enumerate(self.scores) if score == max_score]
        
        if len(winners) == 1:
            message = f'🎉 بازیکن {winners[0]} برنده شد! 🎉'
        else:
            winners_str = ', '.join(str(w) for w in winners)
            message = f'🎉 مساوی! بازیکنان {winners_str} 🎉'
        
        self.show_feedback(message, color.gold, 5.0)
    
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
    global game_manager
    
    # راه‌اندازی موتور Ursina
    app = Ursina()
    
    # تنظیمات پنجره و دوربین
    setup_window()
    
    # تنظیم رنگ پس‌زمینه
    window.color = color.rgb(40, 40, 60)
    
    # ایجاد مدیر بازی
    # num_pairs: تعداد جفت کارت‌ها
    # num_players: تعداد بازیکنان (1 تا 5)
    # level_start: شماره شروع محدوده (مثلاً 1 برای 1-10، 11 برای 11-20)
    game_manager = GameManager(num_pairs=6, num_players=2, level_start=1)
    
    # اجرای برنامه
    app.run()


if __name__ == '__main__':
    main()
