# 代码生成时间: 2025-10-06 17:50:42
import gradio as gr
def calculate_discount(percentage, base_price):
    """Calculates the discount based on the percentage and base price.
    
    Args:
        percentage (float): The discount percentage.
        base_price (float): The original price of the item.
    
    Returns:
        float: The discounted price.
    """
    if percentage < 0 or percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    return base_price * (1 - (percentage / 100.0))


def apply_promotion(promotion_type, price):
    """Applies the specified promotion to the given price.
    
    Args:
        promotion_type (str): The type of promotion.
        price (float): The price to apply the promotion to.
    
    Returns:
        float: The final price after applying the promotion.
    """
    if promotion_type == "percent":
        percentage = 10  # Default percentage for percent promotion
        return calculate_discount(percentage, price)
    elif promotion_type == "fixed":
        discount_amount = 5  # Default fixed discount amount
        return max(0, price - discount_amount)
    else:
        raise ValueError("Invalid promotion type.")


def main():
    """Sets up the Gradio interface for the promotion engine."""
    demo = gr.Interface(
        fn=apply_promotion,
        inputs=[gr.Dropdown(["percent", "fixed"]), gr.Number()],
        outputs="number",
        examples=[["percent", 20], ["fixed", 30]],
        title="Promotion Engine"
    )
    demo.launch()

if __name__ == "__main__":
    main()