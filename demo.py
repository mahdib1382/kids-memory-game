"""
نمایش ساختار بازی بدون نیاز به GUI
این اسکریپت ساختار کارت‌ها را به صورت متنی نمایش می‌دهد
"""

def demo_game_structure():
    """نمایش ساختار Grid کارت‌ها"""
    
    print("\n" + "="*60)
    print("      نمایش ساختار بازی حافظه کودکان")
    print("="*60 + "\n")
    
    # شبیه‌سازی ایجاد کارت‌ها
    from random import shuffle
    num_pairs = 6
    numbers = list(range(1, num_pairs + 1)) * 2
    shuffle(numbers)
    
    print(f"تعداد جفت‌ها: {num_pairs}")
    print(f"تعداد کل کارت‌ها: {len(numbers)}")
    print(f"اعداد (مخلوط شده): {numbers}\n")
    
    # محاسبه Grid
    total_cards = len(numbers)
    if total_cards <= 12:
        cols = 4
    elif total_cards <= 20:
        cols = 5
    else:
        cols = 6
    
    rows = (total_cards + cols - 1) // cols
    
    print(f"ابعاد Grid: {rows} ردیف × {cols} ستون\n")
    print("چیدمان کارت‌ها روی صفحه:")
    print("-" * 40)
    
    # نمایش Grid
    idx = 0
    for row in range(rows):
        line = ""
        for col in range(cols):
            if idx < total_cards:
                line += f"[{numbers[idx]:2}] "
                idx += 1
            else:
                line += "     "
        print(f"  {line}")
    
    print("-" * 40)
    
    # آمار
    print("\nآمار:")
    for num in range(1, num_pairs + 1):
        count = numbers.count(num)
        print(f"  عدد {num}: {count} بار (✓ صحیح)" if count == 2 else f"  عدد {num}: {count} بار (✗ خطا)")
    
    print("\n" + "="*60)
    print("توضیحات:")
    print("  - هر عدد دو بار در بازی وجود دارد")
    print("  - کارت‌ها به صورت تصادفی چیده شده‌اند")
    print("  - در بازی واقعی، کارت‌ها در ابتدا پشت هستند")
    print("  - با کلیک، کارت‌ها با انیمیشن چرخش رو می‌شوند")
    print("="*60 + "\n")
    
    # نمایش فلوی انیمیشن
    print("فلوی انیمیشن کارت:")
    print("  1. کلیک روی کارت")
    print("  2. کارت به صورت افقی کوچک می‌شود (scale_x → 0)")
    print("  3. متن '?' با عدد واقعی جایگزین می‌شود")
    print("  4. کارت دوباره بزرگ می‌شود (scale_x → 1.5)")
    print("  5. مدت کل: 0.3 ثانیه (0.15 + 0.15)\n")

if __name__ == '__main__':
    demo_game_structure()
