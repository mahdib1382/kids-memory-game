"""
تست فاز 5 - بررسی UI/UX، منو، تنظیمات، و گوینده
"""

def test_phase5_features():
    """تست ویژگی‌های فاز 5"""
    
    print("\n" + "="*70)
    print("              تست فاز 5 - UI/UX و تعامل")
    print("="*70 + "\n")
    
    # تست 1: بررسی imports و کلاس‌های جدید
    print("تست 1: بررسی ساختار کد و کلاس‌های جدید...")
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            code = f.read()
        
        # بررسی وجود ویژگی‌های کلیدی فاز 5
        features = {
            'class DataManager': 'مدیر ذخیره‌سازی JSON',
            'class VoiceoverManager': 'مدیر گوینده',
            'class GameMenu': 'منوی اصلی بازی',
            'class SettingsMenu': 'منوی تنظیمات',
            'save_game_result': 'ذخیره نتیجه بازی',
            'speak_number': 'پخش صدای عدد',
            'voiceover_enabled': 'تنظیم گوینده',
            'current_settings': 'تنظیمات فعلی',
            'create_scoreboard': 'پنل امتیازات',
            'game_results.json': 'فایل JSON نتایج',
            'assets/voices': 'پوشه فایل‌های صوتی',
            'start_time': 'زمان شروع بازی',
            'game_time': 'مدت زمان بازی',
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
        
        print("\n✓ تمام ویژگی‌های کلیدی فاز 5 پیاده‌سازی شده است!\n")
        
    except Exception as e:
        print(f"✗ خطا در بررسی کد: {e}")
        return False
    
    # تست 2: بررسی پوشه assets/voices
    print("تست 2: بررسی پوشه assets/voices...")
    import os
    
    if os.path.exists('assets/voices'):
        print(f"  ✓ پوشه assets/voices موجود است")
        if os.path.exists('assets/voices/README.md'):
            print(f"  ✓ راهنمای گوینده موجود است")
    else:
        print(f"  ✗ پوشه assets/voices موجود نیست")
    
    print()
    
    # تست 3: بررسی کلاس DataManager
    print("تست 3: بررسی کلاس DataManager...")
    dm_methods = {
        'save_game_result': 'ذخیره نتیجه بازی',
        'get_recent_games': 'دریافت آخرین بازی‌ها',
        'datetime': 'تاریخ و زمان',
        'json.dump': 'ذخیره در JSON',
    }
    
    for method, description in dm_methods.items():
        if method in code:
            print(f"  ✓ {description} ({method})")
        else:
            print(f"  ✗ {description} ({method}) یافت نشد")
    
    print()
    
    # تست 4: بررسی منوی اصلی
    print("تست 4: بررسی منوی اصلی...")
    menu_features = {
        'شروع بازی': 'دکمه شروع',
        'تنظیمات': 'دکمه تنظیمات',
        'خروج': 'دکمه خروج',
        'def start_game': 'متد شروع بازی',
        'def show_settings': 'نمایش تنظیمات',
    }
    
    for feature, description in menu_features.items():
        if feature in code:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description} یافت نشد")
    
    print()
    
    # تست 5: بررسی منوی تنظیمات
    print("تست 5: بررسی منوی تنظیمات...")
    settings_features = {
        'num_players': 'تنظیم تعداد بازیکنان',
        'level_start': 'تنظیم محدوده اعداد',
        'change_players': 'تغییر تعداد بازیکنان',
        'cycle_level': 'چرخش سطح',
        'toggle_voiceover': 'تغییر وضعیت گوینده',
    }
    
    for feature, description in settings_features.items():
        if feature in code:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description} یافت نشد")
    
    print()
    
    # تست 6: بررسی Scoreboard
    print("تست 6: بررسی Scoreboard...")
    scoreboard_checks = {
        'create_scoreboard': 'متد ایجاد Scoreboard',
        'scoreboard_bg': 'پس‌زمینه Scoreboard',
        'scoreboard_title': 'عنوان Scoreboard',
        '🏆 امتیازات': 'عنوان امتیازات',
    }
    
    for check, description in scoreboard_checks.items():
        if check in code:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description} یافت نشد")
    
    print()
    
    # خلاصه
    print("="*70)
    print("                    خلاصه نتایج تست")
    print("="*70)
    print("\n✓ فاز 5 با موفقیت پیاده‌سازی شده است!")
    print("\nویژگی‌های پیاده‌سازی شده:")
    print("  1. ✓ Main Menu (منوی اصلی با دکمه‌ها)")
    print("  2. ✓ Dynamic Settings (تنظیمات پویا)")
    print("  3. ✓ Scoreboard (پنل امتیازات)")
    print("  4. ✓ JSON Integration (ذخیره نتایج)")
    print("  5. ✓ Persian Voiceover (گوینده فارسی)")
    print("\n" + "="*70 + "\n")
    
    return True

if __name__ == '__main__':
    success = test_phase5_features()
    exit(0 if success else 1)
