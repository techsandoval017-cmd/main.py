import csv
import io

def generar_lote_canva_carritos(carritos_abandonados: list) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Cart_ID", "Customer_Name", "Total_USD", "Discount_Code", "Checkout_URL", "Hook_Copy"])
    
    for c in carritos_abandonados:
        descuento = "SAVE10" if c["total_usd"] < 100 else "SAVE20"
        hook = f"Hey {c['customer_name']}, your cart is reserved! Use {descuento} before it expires."
        writer.writerow([
            c["id"],
            c["customer_name"],
            f"${c['total_usd']}",
            descuento,
            f"https://store.myshopify.com/cart/{c['variant_id']}:1?discount={descuento}",
            hook
        ])
    return output.getvalue()

if __name__ == "__main__":
    demo_carts = [
        {"id": "cart_101", "customer_name": "John Doe", "total_usd": 85.0, "variant_id": "4102938"},
        {"id": "cart_102", "customer_name": "Emma Smith", "total_usd": 150.0, "variant_id": "4102940"}
    ]
    csv_resultado = generar_lote_canva_carritos(demo_carts)
    print("✅ MÓDULO GLOBAL OPERATIVO (CSV para Canva Pro Bulk Create):")
    print(csv_resultado)
