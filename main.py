"""
بازی حافظه کودکان (Kids Memory Game)
فاز اول: پایه‌گذاری - راه‌اندازی موتور Ursina و کلاس‌های اولیه
"""

from ursina import *


class NumberCard(Entity):
    """
    کلاس کارت با قابلیت چرخش و نمایش عدد
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
        
        # متن عدد روی کارت (در ابتدا مخفی است)
        self.number_text = Text(
            text=str(number),
            parent=self,
            position=(0, 0, -0.01),
            scale=3,
            origin=(0, 0),
            color=color.black,
            enabled=False
        )
        
        # متن پشت کارت (علامت سوال)
        self.back_text = Text(
            text='?',
            parent=self,
            position=(0, 0, -0.01),
            scale=3,
            origin=(0, 0),
            color=color.white,
            enabled=True
        )
    
    def input(self, key):
        """مدیریت کلیک روی کارت"""
        if self.hovered and key == 'left mouse down':
            if not self.is_flipped and not self.is_matched:
                self.flip()
    
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
        self.number_text.enabled = True
        self.back_text.enabled = False
        self.color = color.white
    
    def _hide_number(self):
        """مخفی کردن عدد و نمایش پشت کارت"""
        self.number_text.enabled = False
        self.back_text.enabled = True
        self.color = color.azure
    
    def mark_as_matched(self):
        """علامت‌گذاری کارت به عنوان جفت شده"""
        self.is_matched = True
        self.color = color.green
        self.animate_scale(0, duration=0.3, curve=curve.in_out_expo)
        invoke(self.disable, delay=0.3)


class GameManager:
    """
    مدیر بازی که کارت‌ها را مدیریت می‌کند
    """
    def __init__(self, num_pairs=6):
        self.num_pairs = num_pairs
        self.cards = []
        self.flipped_cards = []
        self.create_cards()
    
    def create_cards(self):
        """ایجاد و چیدمان کارت‌ها به صورت Grid"""
        # تعداد کارت‌ها (هر عدد دو بار)
        numbers = list(range(1, self.num_pairs + 1)) * 2
        
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
    
    def update(self):
        """
        به‌روزرسانی وضعیت بازی
        در فاز 2 برای بررسی جفت‌ها و مدیریت نوبت استفاده خواهد شد
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
    # راه‌اندازی موتور Ursina
    app = Ursina()
    
    # تنظیمات پنجره و دوربین
    setup_window()
    
    # تنظیم رنگ پس‌زمینه
    window.color = color.rgb(40, 40, 60)
    
    # ایجاد مدیر بازی
    game_manager = GameManager(num_pairs=6)  # شروع با 6 جفت (12 کارت)
    
    # اجرای برنامه
    app.run()


if __name__ == '__main__':
    main()
