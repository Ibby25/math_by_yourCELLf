import streamlit as st
import numpy as np

def resuspension_and_seeding():
    st.title("🧫 Cell Seeding Calculator")
    st.subheader("Using 1 million cells/mL stock")

    vessel_areas = {
        "6-well": 9.6,
        "12-well": 3.8,
        "24-well": 1.9,
        "96-well": 0.32,
        "T25": 25,
        "T75": 75,
        "T175": 175
    }

    recommended_volumes = {
        "6-well": 2.0,
        "12-well": 1.0,
        "24-well": 0.5,
        "96-well": 0.1,
        "T25": 4.0,
        "T75": 8.0,
        "T175": 20.0
    }

    total_cells = st.number_input(
        "🔢 Enter your total cell count (avg × total vol spun down):",
        min_value=0.0, format="%.2f"
    )

    desired_density = st.number_input(
        "📈 Enter desired seeding density (cells/cm²):",
        min_value=0.0, format="%.2f"
    )

    vessel = st.selectbox("🧪 Select vessel type:", list(vessel_areas.keys()))
    number_of_wells = st.number_input(
        f"🔢 How many {vessel} wells/flasks will you seed?",
        min_value=1, step=1
    )

    if total_cells > 0 and desired_density > 0 and number_of_wells > 0:
        area_per_well = vessel_areas[vessel]
        rec_vol_per_well = recommended_volumes[vessel]

        stock_volume = total_cells / 1e6
        cells_per_well = desired_density * area_per_well
        volume_from_stock_per_well = cells_per_well / 1e6
        total_volume_from_stock = volume_from_stock_per_well * number_of_wells
        total_cells_needed = cells_per_well * number_of_wells
        total_final_volume = rec_vol_per_well * number_of_wells
        media_to_add = total_final_volume - total_volume_from_stock

        st.markdown("### 📋 Results")
        st.success(f"→ Resuspend your pellet in **{stock_volume:.2f} mL** media to get 1M cells/mL stock.")

        st.markdown(f"""
        **For {number_of_wells} × {vessel} (each ~{area_per_well:.2f} cm², {rec_vol_per_well:.2f} mL per well):**
        - You need **{cells_per_well:.0f} cells/well**
        - Add **{volume_from_stock_per_well:.3f} mL** from stock per well
        - **{total_volume_from_stock:.2f} mL** total from stock for {number_of_wells} wells
        - **{total_cells_needed:.0f} total cells used**

        **To prepare {total_final_volume:.2f} mL of cell mix:**
        - Use **{total_volume_from_stock:.2f} mL** of stock
        - Add **{media_to_add:.2f} mL** of fresh media
        - Then pipette **{rec_vol_per_well:.2f} mL** into each well
        """)

        if volume_from_stock_per_well > rec_vol_per_well:
            st.warning("⚠️ Required stock volume per well exceeds the recommended seeding volume. You may need to increase the stock concentration or lower the seeding density.")

# Run the app
if __name__ == "__main__":
    resuspension_and_seeding()





