#!/usr/bin/env python3
"""
LG Home Solutions - Image Cleanup Script
Removes unused and duplicate images from the repository
Frees approximately 208 MB of storage
"""

import os
import sys
from pathlib import Path

# Color codes for output
class Colors:
    YELLOW = '\033[1;33m'
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    NC = '\033[0m'  # No Color

def print_header(text):
    print(f"{Colors.YELLOW}{'='*40}{Colors.NC}")
    print(f"{Colors.YELLOW}{text}{Colors.NC}")
    print(f"{Colors.YELLOW}{'='*40}{Colors.NC}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.NC}")

def print_info(text):
    print(f"{Colors.YELLOW}{text}{Colors.NC}")

def remove_files(file_list, category_name):
    """Remove a list of files and print progress"""
    print_info(f"Removing {category_name}...")
    count = 0
    for file_path in file_list:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print_success(f"Removed: {file_path}")
                count += 1
            except Exception as e:
                print(f"{Colors.RED}✗ Failed to remove {file_path}: {e}{Colors.NC}")
        else:
            print(f"  ⊘ File not found: {file_path}")
    print(f"  → Removed {count} files\n")
    return count

def main():
    print_header("Image Cleanup Script - LG Home Solutions")
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    total_removed = 0
    
    # Category 1: Duplicate PNG files
    duplicates = [
        "images/16LDualInvertorDehumidifier.png",
        "images/AeroBooster.png",
        "images/AeroFuniture.png",
        "images/AeroHitAirPurifier.png",
        "images/DishwasherQuadWash (2).png",
        "images/DualCoolWithPurifier1.5HP.png",
        "images/HitAirPurifier.png",
        "images/WashMachine AIDD20KW.png",
        "images/WashingMachineDual20KG.png",
    ]
    total_removed += remove_files(duplicates, "Category 1: Duplicate PNG files (15 MB)")
    
    # Category 2: Large flyer images
    flyers = [
        "images/flyer_page1.png",
        "images/flyer_page2.png",
        "images/flyer_page3.png",
        "images/flyer_page4.png",
        "images/flyer_page5.png",
        "images/flyer_page6.png",
        "images/flyer_page7.png",
        "images/flyer_page8.png",
        "images/flyer_page9.png",
        "images/flyer_page11.png",
        "images/flyer_page16.png",
        "images/flyer_page21.png",
        "images/flyer_page26.png",
        "images/flyer_page31.png",
        "images/flyer_page36.png",
    ]
    total_removed += remove_files(flyers, "Category 2: Large flyer images (33 MB)")
    
    # Category 3: AC numbered sequences
    ac_files = [
        "images/ac1.jpg", "images/ac2.jpg", "images/ac3.jpg", "images/ac4.jpg",
        "images/ac5.jpg", "images/ac6.jpg", "images/ac7.jpg", "images/ac8.jpg",
        "images/ac9.jpg", "images/ac_scene_1.jpg", "images/ac_scene_2.jpg",
        "images/aca1.jpg", "images/aca2.jpg", "images/aca3.jpg", "images/aca4.jpg",
        "images/acav1.mp4", "images/acav2.mp4", "images/acav3.mp4", "images/acav4.mp4",
        "images/acv1.mp4", "images/acv2.webm", "images/acv3.mp4", "images/acv4.mp4",
    ]
    total_removed += remove_files(ac_files, "Category 3: AC numbered sequences (8.8 MB)")
    
    # Category 4: Water purifier numbered sequences
    water_files = [
        "images/wpa1.jpg", "images/wpa2.jpg", "images/wpa3.jpg", "images/wpa4.jpg",
        "images/wpa5.jpg", "images/wpa6.png", "images/wpa7.jpg", "images/wpa8.jpg",
        "images/wpa9.jpg", "images/wpa10.jpg", "images/wpa11.jpg", "images/wpa12.jpg",
        "images/wpa13.jpg", "images/wpa14.jpg", "images/wpa15.jpg", "images/wpa16.jpg",
        "images/wpa17.jpg", "images/wpa18.jpg", "images/wpav2.mp4", "images/wpav3.mp4",
        "images/wpb1.mp4", "images/wpb2.webm", "images/wpb3.webm", "images/wpb4.webm",
        "images/wpb5.webm", "images/wpb6.jpg", "images/wpb7.jpg", "images/wpb8.jpg",
        "images/wpb9.jpg", "images/wpc1.jpg", "images/wpc2.jpg", "images/wpc3.jpg",
        "images/wpc4.jpg", "images/wpc5.jpg", "images/wpc6.jpg", "images/wpc7.jpg",
        "images/wpcv1.mp4", "images/wpcv2.mp4", "images/wpcv3.webm", "images/wpcv4.webm",
        "images/wpcv5.webm", "images/wpcv6.webm",
    ]
    total_removed += remove_files(water_files, "Category 4: Water purifier sequences (35 MB)")
    
    # Category 5: Dishwasher numbered sequences
    dishwasher_files = [
        "images/quadwash-1.jpg", "images/quadwash-2.jpg", "images/quadwash-3.jpg",
        "images/quadwash-4.jpg", "images/quadwash-5.jpg", "images/quadwash-6.jpg",
        "images/quadwash-7.jpg", "images/quadwash-8.jpg", "images/quadwash-9.jpg",
        "images/quadwash-10.jpg", "images/quadwash-11.jpg",
        "images/dishwasher-silver-1.jpg", "images/dishwasher-silver-2.jpg",
        "images/dishwasher-silver-3.jpg", "images/dishwasher-silver-4.jpg",
        "images/dishwasher-silver-5.jpg", "images/dishwasher-silver-6.jpg",
        "images/dishwasher-silver-7.jpg", "images/dishwasher-silver-8.jpg",
        "images/dishwasher-silver-9.jpg", "images/dishwasher-silver-10.jpg",
        "images/dishwasher-silver-11.jpg",
    ]
    total_removed += remove_files(dishwasher_files, "Category 5: Dishwasher sequences (2.5 MB)")
    
    # Category 6: Washing machine numbered sequences
    washer_files = [
        "images/washt1.jpg", "images/washt3.jpg", "images/washt4.jpg", "images/washt5.webm",
        "images/washt6.jpg", "images/washt7.jpg", "images/washt8.png", "images/washt9.mp4",
        "images/washt10.png", "images/washt11.webm", "images/washt12.webm", "images/washt13.webm",
        "images/washt14.webm", "images/washt15.webm", "images/washt16.jpg", "images/washt17.jpg",
        "images/washt18.jpg",
    ]
    total_removed += remove_files(washer_files, "Category 6: Washing machine sequences (20 MB)")
    
    # Category 7: Washing tower sequences
    washtower_files = [
        "images/washtower-1.jpg", "images/washtower-2.jpg", "images/washtower-3.jpg",
        "images/washtower2520-1.jpg",
    ]
    total_removed += remove_files(washtower_files, "Category 7: Washing tower sequences (0.1 MB)")
    
    # Category 8: Duplicate detail images
    detail_files = [
        "images/aidd-1.jpg", "images/aidd-2.jpg", "images/aidd-3.jpg",
        "images/aidd10kg-1.jpg", "images/aidd10kg-2.jpg", "images/aidd10kg-3.jpg",
        "images/aidd10kg-4.jpg", "images/aidd15kg-1.jpg", "images/aidd15kg-2.jpg",
        "images/aidd15kg-3.jpg", "images/aidd15kg-4.jpg", "images/aidd20kg-1.jpg",
        "images/aidd20kg-2.jpg", "images/aidd20kg-3.jpg", "images/aidd20kg-4.jpg",
        "images/aidd105kg-1.jpg", "images/aidd105kg-2.jpg", "images/aidd105kg-3.jpg",
        "images/aerobooster-1.jpg", "images/aerobooster-2.jpg", "images/aerofurniture-white-detail.jpg",
        "images/aerofurniture-white.jpg", "images/aerofurniture-1.jpg", "images/aerofurniture-2.jpg",
        "images/alphapet-double-1.jpg", "images/alphapet-double-2.jpg", "images/alphapet-double-3.jpg",
        "images/alphapet-single-1.jpg", "images/alphapet-single-2.jpg", "images/cattower-1.jpg",
        "images/cattower-2.jpg", "images/cordzero-1.jpg", "images/cordzero-2.jpg",
        "images/cordzero-3.jpg", "images/cordzero-4.jpg", "images/cordzero-5.jpg",
        "images/dd16gm-1.jpg", "images/dd16gm-2.jpg", "images/dryer9kg-1.jpg",
        "images/dryer9kg-2.jpg", "images/dryer9kg-3.jpg", "images/dryer9kg-4.jpg",
        "images/hit-as60-beige-top.jpg", "images/hit-as60-white-top.jpg", "images/hit-as60-1.jpg",
        "images/hit-as60-2.jpg", "images/hit-as65-1.jpg", "images/hit-as65-2.jpg",
        "images/hit-as65-3.jpg", "images/hit-detail-1.jpg", "images/hit-detail-2.jpg",
        "images/hit-detail-3.jpg", "images/hit-detail-4.jpg",
    ]
    total_removed += remove_files(detail_files, "Category 8: Duplicate detail images (4 MB)")
    
    # Category 9: Scene/lifestyle images
    scene_files = [
        "images/air_scene_1.jpg", "images/air_scene_2.jpg", "images/fridge_scene_1.jpg",
        "images/fridge_scene_2.jpg", "images/others_scene_1.jpg", "images/others_scene_2.jpg",
        "images/tv_scene_1.jpg", "images/tv_scene_2.jpg", "images/washer_scene_1.jpg",
        "images/washer_scene_2.jpg", "images/water_scene_1.jpg", "images/water_scene_2.jpg",
    ]
    total_removed += remove_files(scene_files, "Category 9: Scene/lifestyle images (1.1 MB)")
    
    # Category 10: Miscellaneous unused files
    misc_files = [
        "images/3water1.jpg", "images/3water2.jpg", "images/3water3.jpg", "images/3water4.jpg",
        "images/3water5.jpg", "images/3water6.jpg", "images/3water7.jpg", "images/3water8.jpg",
        "images/3water9.jpg", "images/3water10.jpg", "images/3water11.jpg", "images/2water2.jpg",
        "images/2water4.jpg", "images/2water5.png", "images/2water6.jpg", "images/2water7.jpg",
        "images/2water8.jpg", "images/3waterv1.webm", "images/3waterv2.webm", "images/3waterv3.webm",
        "images/3waterv4.webm", "images/3waterv5.webm", "images/3waterv6.webm", "images/3waterv7.webm",
        "images/3waterv8.webm", "images/heropage.MOV", "images/0509.mp4",
        "images/10f16817-9cec-4582-8741-7f86f2c42dcc.jpeg", "images/765d0c67-2a64-455d-8832-dc8fc831bfc8.jpeg",
        "images/8652b39d-2c00-4164-bb45-04c125e731e6.jpeg", "images/aefe7d95-8cfe-40a1-a63f-2577c1e1b673.jpeg",
        "images/b3d694f5-c24e-480c-b3a9-ad04a92c695e.jpeg", "images/IMG_0914.webp",
    ]
    total_removed += remove_files(misc_files, "Category 10: Miscellaneous files (61 MB)")
    
    print_header(f"Cleanup Complete! - {total_removed} files removed (~208 MB freed)")
    
    print_info("Next steps:")
    print("1. Review the deleted files above")
    print("2. Run: git add -A")
    print("3. Run: git commit -m 'Remove unused and duplicate images - Free 208 MB storage'")
    print("4. Run: git push origin main")
    print("")
    print_info("To restore from backup if needed:")
    print("   git checkout image-cleanup-backup")

if __name__ == "__main__":
    main()
