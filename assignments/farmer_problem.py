# The overall sales achieved by Mahesh from his 80 acres of land.

# --- Land Distribution ---
total_land_acres = 80
num_segments = 5
land_per_segment = total_land_acres / num_segments
print(f"Land per segment: {land_per_segment} acres\n")

# --- Crop-wise Sales Calculation ---

# 1. Tomatoes
tomato_acres = land_per_segment
tomato_yield_1 = 10  # tonnes/acre
tomato_yield_2 = 12  # tonnes/acre
tomato_price_per_kg = 7
tomato_land_1 = tomato_acres * 0.30
tomato_land_2 = tomato_acres * 0.70

tomato_sales = (
    (tomato_land_1 * tomato_yield_1 * 1000 * tomato_price_per_kg) +
    (tomato_land_2 * tomato_yield_2 * 1000 * tomato_price_per_kg)
)
print(f"Total Tomato Sales: Rs. {tomato_sales:,.2f}")

# 2. Potatoes
potato_acres = land_per_segment
potato_yield = 10  # tonnes/acre
potato_price_per_kg = 20

potato_sales = potato_acres * potato_yield * 1000 * potato_price_per_kg
print(f"Total Potato Sales: Rs. {potato_sales:,.2f}")

# 3. Cabbage
cabbage_acres = land_per_segment
cabbage_yield = 14  # tonnes/acre
cabbage_price_per_kg = 24

cabbage_sales = cabbage_acres * cabbage_yield * 1000 * cabbage_price_per_kg
print(f"Total Cabbage Sales: Rs. {cabbage_sales:,.2f}")

# 4. Sunflowers
sunflower_acres = land_per_segment
sunflower_yield = 0.7  # tonnes/acre
sunflower_price_per_kg = 200

sunflower_sales = sunflower_acres * sunflower_yield * 1000 * sunflower_price_per_kg
print(f"Total Sunflower Sales: Rs. {sunflower_sales:,.2f}")

# 5. Sugarcane
sugarcane_acres = land_per_segment
sugarcane_yield = 45  # tonnes/acre
sugarcane_price_per_tonne = 4000

sugarcane_sales = sugarcane_acres * sugarcane_yield * sugarcane_price_per_tonne
print(f"Total Sugarcane Sales: Rs. {sugarcane_sales:,.2f}")

# --- Overall Sales ---
overall_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
print("\n" + "="*40)
print(f"Overall Sales Achieved: Rs. {overall_sales:,.2f}")
print("="*40)