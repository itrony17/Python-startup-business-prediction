import time

# Expanded database of industry averages (Simulated data based on global market trends)
# Margin = Average Profit Margin % | Growth = Annual Industry Growth % 
# Global_Demand = Out of 10 | Scaling_Difficulty = Out of 10 (Higher = harder to grow globally)
INDUSTRY_DATA = {
    # Tech & Services
    "it": {"margin": 30, "growth": 15, "global_demand": 9, "scaling_difficulty": 4},
    "tech": {"margin": 30, "growth": 15, "global_demand": 9, "scaling_difficulty": 4},
    "consulting": {"margin": 25, "growth": 10, "global_demand": 8, "scaling_difficulty": 5},
    "online learning": {"margin": 35, "growth": 18, "global_demand": 8, "scaling_difficulty": 3},
    "edtech": {"margin": 35, "growth": 18, "global_demand": 8, "scaling_difficulty": 3},
    "product sourcing": {"margin": 20, "growth": 8, "global_demand": 7, "scaling_difficulty": 5},
    
    # Retail & E-commerce
    "ecommerce": {"margin": 20, "growth": 12, "global_demand": 9, "scaling_difficulty": 5},
    "e-commerce": {"margin": 20, "growth": 12, "global_demand": 9, "scaling_difficulty": 5},
    "grocery": {"margin": 5, "growth": 3, "global_demand": 10, "scaling_difficulty": 6},
    "online book shop": {"margin": 20, "growth": 8, "global_demand": 7, "scaling_difficulty": 5},
    "pet shop": {"margin": 25, "growth": 10, "global_demand": 7, "scaling_difficulty": 5},
    
    # Food & Beverage
    "food": {"margin": 10, "growth": 5, "global_demand": 9, "scaling_difficulty": 7},
    "restaurant": {"margin": 8, "growth": 4, "global_demand": 9, "scaling_difficulty": 8},
    "online coffee shop": {"margin": 25, "growth": 10, "global_demand": 8, "scaling_difficulty": 5},
    "street food": {"margin": 30, "growth": 5, "global_demand": 8, "scaling_difficulty": 9},
    
    # Travel & Tourism
    "tourism": {"margin": 15, "growth": 6, "global_demand": 8, "scaling_difficulty": 7},
    "travel agency": {"margin": 10, "growth": 5, "global_demand": 7, "scaling_difficulty": 6},
    
    # Agriculture & Farming
    "agriculture": {"margin": 15, "growth": 7, "global_demand": 9, "scaling_difficulty": 8},
    "agri business": {"margin": 15, "growth": 7, "global_demand": 9, "scaling_difficulty": 8},
    "online farming": {"margin": 20, "growth": 14, "global_demand": 7, "scaling_difficulty": 7},
    "fish farming": {"margin": 15, "growth": 9, "global_demand": 7, "scaling_difficulty": 8},
    "cow fattening": {"margin": 12, "growth": 5, "global_demand": 8, "scaling_difficulty": 8},
    "gardening": {"margin": 25, "growth": 8, "global_demand": 6, "scaling_difficulty": 6},
    "nursery": {"margin": 25, "growth": 8, "global_demand": 6, "scaling_difficulty": 6},
    
    # Manufacturing
    "manufacturing": {"margin": 15, "growth": 6, "global_demand": 8, "scaling_difficulty": 9},
    "contract manufacturing": {"margin": 15, "growth": 6, "global_demand": 7, "scaling_difficulty": 8},
}

def calculate_profitability(idea: str):
    idea_lower = idea.lower()
    matched_category = None
    
    # Match input to our database
    for category in INDUSTRY_DATA:
        if category in idea_lower:
            matched_category = category
            break
            
    if not matched_category:
        return "Unknown", 0, "No data available for this specific industry. Try using keywords like 'IT', 'street food', 'cow fattening', 'ecommerce', etc."

    data = INDUSTRY_DATA[matched_category]
    
    # Calculate Score (Higher margin & growth = good, Higher difficulty = bad)
    # Formula: (Margin * 2 + Growth * 3 + Global_Demand * 2) - (Scaling_Difficulty * 2)
    raw_score = (data["margin"] * 2) + (data["growth"] * 3) + (data["global_demand"] * 2) - (data["scaling_difficulty"] * 2)
    
    # Normalize score to 100
    max_possible_score = (40 * 2) + (20 * 3) + (10 * 2) 
    percentage_score = int((raw_score / max_possible_score) * 100)
    
    # Generate Explanation based on category
    explanation = f"""
    Category Matched: {matched_category.capitalize()}
    - Average Profit Margin: ~{data['margin']}%
    - Annual Industry Growth: ~{data['growth']}%
    - Global Demand Level: {data['global_demand']}/10
    - Scaling Difficulty: {data['scaling_difficulty']}/10 (Higher = harder to expand globally)
    
    Why it can succeed globally:
    """
    
    if matched_category in ["it", "tech", "consulting", "online learning", "edtech"]:
        explanation += "Digital and knowledge-based businesses have incredibly high margins and low scaling difficulty. You can serve a global customer base instantly via the internet with minimal physical infrastructure, making it highly profitable globally."
    
    elif matched_category in ["ecommerce", "e-commerce", "online book shop", "pet shop", "product sourcing"]:
        explanation += "E-commerce and retail platforms have strong global demand. By leveraging global shipping networks and drop-shipping models, you can reach worldwide audiences without the overhead of physical stores, driving solid profitability."
        
    elif matched_category in ["online coffee shop", "street food", "food", "restaurant"]:
        explanation += "Food and beverage have massive global demand. While street food has great margins locally, scaling food businesses globally is tough due to supply chain logistics and local food regulations. Success globally requires franchising or packaged goods models."
        
    elif matched_category in ["tourism", "travel agency"]:
        explanation += "The travel industry thrives on global experience demand. However, it is highly susceptible to global events (pandemics, economy). Success globally requires strong digital marketing and B2B partnerships with global hospitality networks."
        
    elif matched_category in ["agriculture", "agri business", "online farming", "fish farming", "cow fattening"]:
        explanation += "Agriculture and farming are essential, ensuring massive global demand. However, they have high scaling difficulty due to land, climate, and supply chain requirements. Global success comes from exporting to nations with food deficits or integrating 'AgriTech' for higher yields."
        
    elif matched_category in ["gardening", "nursery"]:
        explanation += "With the global rise in urbanization and mental health awareness, the demand for plants and gardening is growing. While scaling globally is tough due to agricultural export laws, specializing in rare seeds, equipment, or digital gardening guides can unlock global markets."
        
    elif matched_category in ["manufacturing", "contract manufacturing"]:
        explanation += "Manufacturing offers decent margins and steady global demand. It has high scaling difficulty due to capital requirements. Global success relies heavily on moving production to low-cost regions and exporting to high-consumption markets."

    return matched_category, percentage_score, explanation

def run_offline_predictor():
    print("="*50)
    print("📊 EXPANDED STARTUP PROFITABILITY CALCULATOR 📊")
    print("="*50)
    user_idea = input("\nEnter your business product/idea: ")
    
    print("\nCalculating profitability based on industry averages...")
    time.sleep(2) # Simulate calculation time
    
    category, score, explanation = calculate_profitability(user_idea)
    
    print("\n" + "="*50)
    print("📈 FEASIBILITY REPORT 📈")
    print("="*50)
    
    if score == 0:
        print(explanation)
    else:
        print(f"💡 Business Idea: {user_idea}")
        print(f"🎯 Profitability/Feasibility Score: {score}/100")
        print(f"🏷️ Category: {category.capitalize()}")
        print(explanation)
    print("="*50)

# (Keep all the INDUSTRY_DATA and calculate_profitability function exactly the same as before)
import streamlit as st

st.title("📊 Startup Profitability Predictor")
st.write("Enter your business idea to calculate its feasibility score and global market potential.")

user_idea = st.text_input("Enter your business product/idea (e.g., IT consulting, Fish farming):")

if st.button("Analyze Startup"):
    if user_idea:
        category, score, explanation = calculate_profitability(user_idea)
        st.subheader("📈 Feasibility Report")
        
        if score == 0:
            st.warning(explanation)
        else:
            st.metric(label="Profitability Score", value=f"{score}/100")
            st.markdown(f"**Category Matched:** {category.capitalize()}")
            st.markdown(explanation)
    else:
        st.error("Please enter a business idea first.")


if __name__ == "__main__":
    run_offline_predictor()
    
    
