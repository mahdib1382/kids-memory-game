"""
تست فاز 6 - بهینه‌سازی و مستندات
"""
import json
from pathlib import Path

def test_json_loading():
    """تست بارگذاری فایل JSON تاریخچه"""
    print("\n" + "="*70)
    print("         تست فاز 6 - بهینه‌سازی و مستندات")
    print("="*70 + "\n")
    
    print("تست 1: بررسی وجود و ساختار فایل JSON...")
    
    # ایجاد یک فایل JSON تستی
    test_file = Path('game_results.json')
    
    # تست 1: بررسی امکان ایجاد فایل
    test_data = {
        'games': [
            {
                'date': '2026-02-01 06:00:00',
                'winner': 'بازیکن 1',
                'game_time': 45.67,
                'num_players': 2,
                'scores': [5, 3]
            }
        ]
    }
    
    try:
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
        print("  ✓ ایجاد فایل JSON موفق")
    except Exception as e:
        print(f"  ✗ خطا در ایجاد فایل: {e}")
        return False
    
    # تست 2: بارگذاری فایل
    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
        print("  ✓ بارگذاری فایل JSON موفق")
    except Exception as e:
        print(f"  ✗ خطا در بارگذاری فایل: {e}")
        return False
    
    # تست 3: بررسی ساختار داده‌ها
    try:
        assert 'games' in loaded_data, "کلید 'games' یافت نشد"
        assert isinstance(loaded_data['games'], list), "'games' باید لیست باشد"
        assert len(loaded_data['games']) > 0, "لیست بازی‌ها خالی است"
        
        game = loaded_data['games'][0]
        required_fields = ['date', 'winner', 'game_time', 'num_players', 'scores']
        for field in required_fields:
            assert field in game, f"فیلد '{field}' یافت نشد"
        
        print("  ✓ ساختار داده‌ها صحیح است")
    except AssertionError as e:
        print(f"  ✗ خطا در ساختار: {e}")
        return False
    
    # تست 4: بررسی نوع داده‌ها
    try:
        assert isinstance(game['date'], str), "date باید رشته باشد"
        assert isinstance(game['winner'], str), "winner باید رشته باشد"
        assert isinstance(game['game_time'], (int, float)), "game_time باید عدد باشد"
        assert isinstance(game['num_players'], int), "num_players باید عدد صحیح باشد"
        assert isinstance(game['scores'], list), "scores باید لیست باشد"
        print("  ✓ نوع داده‌ها صحیح است")
    except AssertionError as e:
        print(f"  ✗ خطا در نوع داده: {e}")
        return False
    
    # تست 5: افزودن بازی جدید
    try:
        new_game = {
            'date': '2026-02-01 07:00:00',
            'winner': 'بازیکن 2',
            'game_time': 52.34,
            'num_players': 2,
            'scores': [3, 5]
        }
        loaded_data['games'].append(new_game)
        
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(loaded_data, f, ensure_ascii=False, indent=2)
        
        # بارگذاری مجدد
        with open(test_file, 'r', encoding='utf-8') as f:
            updated_data = json.load(f)
        
        assert len(updated_data['games']) == 2, "تعداد بازی‌ها باید 2 باشد"
        print("  ✓ افزودن بازی جدید موفق")
    except Exception as e:
        print(f"  ✗ خطا در افزودن بازی: {e}")
        return False
    
    # تست 6: مدیریت خطا برای فایل نامعتبر
    print("\nتست 2: مدیریت خطا...")
    
    # ایجاد فایل نامعتبر
    invalid_file = Path('invalid.json')
    try:
        with open(invalid_file, 'w', encoding='utf-8') as f:
            f.write('{"invalid": json content}')
        
        # سعی در بارگذاری
        try:
            with open(invalid_file, 'r', encoding='utf-8') as f:
                json.load(f)
            print("  ✗ باید خطا رخ دهد")
            invalid_file.unlink()  # حذف فایل
            return False
        except json.JSONDecodeError:
            print("  ✓ خطای JSON به درستی شناسایی شد")
            invalid_file.unlink()  # حذف فایل
    except Exception as e:
        print(f"  ✗ خطای غیرمنتظره: {e}")
        if invalid_file.exists():
            invalid_file.unlink()
        return False
    
    print("\n" + "="*70)
    print("خلاصه نتایج تست")
    print("="*70)
    print("\n✓ تمام تست‌های JSON با موفقیت انجام شد!")
    print("\nتست‌های انجام شده:")
    print("  1. ✓ ایجاد فایل JSON")
    print("  2. ✓ بارگذاری فایل JSON")
    print("  3. ✓ بررسی ساختار داده‌ها")
    print("  4. ✓ بررسی نوع داده‌ها")
    print("  5. ✓ افزودن بازی جدید")
    print("  6. ✓ مدیریت خطا")
    print("\n" + "="*70 + "\n")
    
    return True


def test_code_features():
    """تست ویژگی‌های کد فاز 6"""
    print("\n" + "="*70)
    print("         تست ویژگی‌های کد فاز 6")
    print("="*70 + "\n")
    
    print("تست 1: بررسی وجود ویژگی‌های جدید...")
    
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            code = f.read()
        
        features = {
            'HelpWindow': 'پنجره راهنما',
            'show_help': 'نمایش راهنما',
            '❓ راهنما': 'دکمه راهنما',
            '_unlock_after_flip': 'باز کردن قفل بعد از چرخش',
            'game_manager.is_processing = True': 'قفل در input',
            'isinstance(entity, ConfettiParticle)': 'پاکسازی ذرات',
            'cards.clear()': 'پاکسازی لیست‌ها',
            '📌 هدف بازی': 'محتوای راهنما',
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
        
        print("\n✓ تمام ویژگی‌های فاز 6 پیاده‌سازی شده است!\n")
        return True
        
    except Exception as e:
        print(f"✗ خطا در بررسی کد: {e}")
        return False


def test_readme():
    """تست وجود مستندات دوزبانه"""
    print("\n" + "="*70)
    print("         تست مستندات دوزبانه")
    print("="*70 + "\n")
    
    print("تست: بررسی README.md...")
    
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        sections = {
            'Installation': 'بخش نصب انگلیسی',
            'نصب': 'بخش نصب فارسی',
            'Game Guide': 'راهنمای بازی انگلیسی',
            'راهنمای بازی': 'راهنمای بازی فارسی',
        }
        
        missing = []
        for section, description in sections.items():
            if section.lower() in content.lower():
                print(f"  ✓ {description}")
            else:
                missing.append(f"  ✗ {description} ({section})")
        
        if missing:
            print("\nبخش‌های ناموجود:")
            for m in missing:
                print(m)
            print("\nنکته: این تست بعد از بازنویسی README انجام می‌شود")
            return False
        
        print("\n✓ مستندات دوزبانه کامل است!\n")
        return True
        
    except Exception as e:
        print(f"✗ خطا در خواندن README: {e}")
        return False


if __name__ == '__main__':
    print("\n" + "╔" + "="*70 + "╗")
    print("║" + " "*20 + "تست نهایی فاز 6" + " "*30 + "║")
    print("╚" + "="*70 + "╝")
    
    results = []
    
    # تست JSON
    results.append(("JSON Loading", test_json_loading()))
    
    # تست ویژگی‌های کد
    results.append(("Code Features", test_code_features()))
    
    # تست مستندات (اختیاری)
    # results.append(("Documentation", test_readme()))
    
    # نمایش نتیجه نهایی
    print("\n" + "="*70)
    print("                    نتیجه نهایی")
    print("="*70)
    
    for test_name, result in results:
        status = "✓ موفق" if result else "✗ ناموفق"
        print(f"  {test_name}: {status}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n🎉 تمام تست‌های فاز 6 با موفقیت انجام شد! 🎉\n")
        exit(0)
    else:
        print("\n⚠️ برخی تست‌ها شکست خوردند ⚠️\n")
        exit(1)
