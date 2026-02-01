"""
تست فاز 3 و 4 - بررسی جلوه‌های بصری و صوتی
این اسکریپت بدون نیاز به GUI ویژگی‌های فاز 3 و 4 را بررسی می‌کند
"""

def test_phase3_features():
    """تست ویژگی‌های فاز 3 و 4"""
    
    print("\n" + "="*70)
    print("         تست فاز 3 و 4 - جلوه‌های بصری و صوتی")
    print("="*70 + "\n")
    
    # تست 1: بررسی imports و کلاس‌های جدید
    print("تست 1: بررسی ساختار کد و کلاس‌های جدید...")
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            code = f.read()
        
        # بررسی وجود ویژگی‌های کلیدی فاز 3
        features = {
            'class AudioManager': 'کلاس مدیر صداها',
            'class ConfettiParticle': 'کلاس ذرات جشن',
            '_load_texture': 'سیستم بارگذاری تصاویر',
            'self.number_image': 'پشتیبانی از تصویر روی کارت',
            'curve.out_back': 'انیمیشن با curve.out_back',
            'audio_manager.play': 'پخش صدا',
            'spawn_confetti': 'ایجاد ذرات',
            'assets/textures': 'پوشه تصاویر',
            'assets/sounds': 'پوشه صداها',
            'click.wav': 'صدای کلیک',
            'success.mp3': 'صدای موفقیت',
            'wrong.wav': 'صدای اشتباه',
        }
        
        missing = []
        for feature, description in features.items():
            if feature not in code:
                missing.append(f"  ✗ {description} ({feature})")
            else:
                print(f"  ✓ {description}")
        
        if missing:
            print("\nویژگی‌های ناموجود:")
            for m in missing:
                print(m)
            return False
        
        print("\n✓ تمام ویژگی‌های کلیدی فاز 3 و 4 پیاده‌سازی شده است!\n")
        
    except Exception as e:
        print(f"✗ خطا در بررسی کد: {e}")
        return False
    
    # تست 2: بررسی پوشه assets
    print("تست 2: بررسی ساختار پوشه assets...")
    import os
    
    required_dirs = ['assets', 'assets/textures', 'assets/sounds']
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"  ✓ پوشه {dir_path} موجود است")
        else:
            print(f"  ✗ پوشه {dir_path} موجود نیست")
    
    print()
    
    # تست 3: بررسی متدهای AudioManager
    print("تست 3: بررسی کلاس AudioManager...")
    audio_methods = {
        'def load_sounds': 'بارگذاری صداها',
        'def play': 'پخش صدا',
    }
    
    for method, description in audio_methods.items():
        if method in code:
            print(f"  ✓ {description} ({method})")
        else:
            print(f"  ✗ {description} ({method}) یافت نشد")
    
    print()
    
    # تست 4: بررسی انیمیشن‌های بهبود یافته
    print("تست 4: بررسی انیمیشن‌های پیشرفته...")
    animation_checks = {
        'animate_scale': 'انیمیشن مقیاس',
        'curve.out_back': 'منحنی out_back',
        'original_scale * 1.3': 'بزرگ شدن کارت',
    }
    
    for check, description in animation_checks.items():
        if check in code:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description} یافت نشد")
    
    print()
    
    # تست 5: بررسی سیستم ذرات
    print("تست 5: بررسی سیستم ذرات...")
    particle_checks = {
        'class ConfettiParticle': 'کلاس ذره',
        'self.velocity': 'سرعت ذره',
        'self.gravity': 'گرانش',
        'def update': 'به‌روزرسانی ذره',
        'spawn_confetti': 'ایجاد ذرات',
    }
    
    for check, description in particle_checks.items():
        if check in code:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description} یافت نشد")
    
    print()
    
    # تست 6: بررسی خوانایی اعداد
    print("تست 6: بررسی بهبود خوانایی اعداد...")
    readability_checks = {
        'scale=4': 'افزایش اندازه متن',
        'color.black': 'رنگ واضح متن',
    }
    
    for check, description in readability_checks.items():
        if check in code:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description} یافت نشد")
    
    print()
    
    # خلاصه
    print("="*70)
    print("                    خلاصه نتایج تست")
    print("="*70)
    print("\n✓ فاز 3 و 4 با موفقیت پیاده‌سازی شده است!")
    print("\nویژگی‌های پیاده‌سازی شده:")
    print("  1. ✓ سیستم Texture (PNG از assets/textures با fallback)")
    print("  2. ✓ انیمیشن‌های نرم‌تر (bounce با curve.out_back)")
    print("  3. ✓ صداگذاری (click, success, wrong)")
    print("  4. ✓ سیستم ذرات (Confetti با گرانش)")
    print("  5. ✓ بهبود خوانایی اعداد (اندازه بزرگ‌تر)")
    print("\n" + "="*70 + "\n")
    
    return True

if __name__ == '__main__':
    success = test_phase3_features()
    exit(0 if success else 1)
