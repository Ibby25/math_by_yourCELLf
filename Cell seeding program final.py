#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[ ]:


# Choose plate you want seeded lol

def display_vessels(vessels):
    for vessel in vessels:
        print(f" - {vessel}")

def resuspension_and_seeding():
    print("=== Cell Seeding Calculator (Using 1M cells/mL stock) ===\n")

    vessel_areas = {"6-well": 9.6,"12-well": 3.8,"24-well": 1.9,
        "96-well": 0.32,"T25": 25,"T75": 75,"T175": 175}

    recommended_volumes = {"6-well": 2.0,"12-well": 1.0,"24-well": 0.5,
        "96-well": 0.1,"T25": 4.0,"T75": 8.0,"T175": 20.0}

    try:
        total_cells = float(input("Enter your total cell count (avg*total vol you spun down): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Resuspend to 1M cells/mL
    stock_volume = total_cells / 1e6
    print(f"\n→ Resuspend your pellet in {stock_volume:.2f} mL of media to get 1e6 cells/mL stock.")

    try:
        desired_density = float(input("\nEnter desired seeding density (cells/cm²): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print("\nSelect vessel type:")
    display_vessels(vessel_areas)
    vessel = input("Enter vessel type: ").strip()

    if vessel not in vessel_areas:
        print("Invalid vessel selected.")
        return

    try:
        number_of_wells = int(input(f"How many {vessel} wells/flasks will you seed? "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    area_per_well = vessel_areas[vessel]
    rec_vol_per_well = recommended_volumes[vessel]

    cells_per_well = desired_density * area_per_well
    volume_from_stock_per_well = cells_per_well / 1e6  # because stock is 1M cells/mL
    total_volume_from_stock = volume_from_stock_per_well * number_of_wells
    total_cells_needed = cells_per_well * number_of_wells
    total_final_volume = rec_vol_per_well * number_of_wells
    media_to_add = total_final_volume - total_volume_from_stock

    print(f"\nFor {number_of_wells} × {vessel} (each ~{area_per_well:.2f} cm², {rec_vol_per_well:.2f} mL per well):")
    print(f"- You will need {cells_per_well:.0f} cells per well")
    print(f"- Add {volume_from_stock_per_well:.3f} mL from the 1M cells/mL stock per well")
    print(f"- Total volume from stock needed: {total_volume_from_stock:.2f} mL for {number_of_wells} wells")
    print(f"- Total cells used: {total_cells_needed:.0f} cells\n")

    print(f"→ To prepare {total_final_volume:.2f} mL of cell mix for all wells:")
    print(f"   - Use {total_volume_from_stock:.2f} mL of 1M cells/mL stock")
    print(f"   - Add {media_to_add:.2f} mL of fresh media")
    print(f"\nThen pipette {rec_vol_per_well:.2f} mL into each of the {number_of_wells} wells.")

    if volume_from_stock_per_well > rec_vol_per_well:
        print("\n⚠️ WARNING: The required stock volume per well exceeds the recommended seeding volume.")
        print("You may need to increase your stock concentration or decrease seeding density.")

if __name__ == "__main__":
    resuspension_and_seeding()






# In[ ]:




