## Flask Application Design for a Toy Shopping Website

### HTML Files

**toy_shop.html (Home page):**
- Displays a list of product categories (e.g., "Soccer," "Basketball," "Swimming") as links.
- Includes a search bar for products.

**product_list.html (Category page):**
- Lists products within a specific category, displaying their name, price, and an "Add to Cart" button.
- Provides filtering options for product attributes (e.g., size, color).

**product_details.html (Product page):**
- Shows detailed information about a specific product, including its description, specifications, and reviews.
- Offers an "Add to Cart" button and recommends similar products.

**cart.html (Shopping cart):**
- Lists the products currently in the user's cart, along with their quantity and subtotal.
- Provides options for removing items, updating quantities, and checking out.

### Routes

**@app.route("/")** (Home page)
- Renders the `toy_shop.html` template.

**@app.route("/category/<category_name>")** (Category page)
- Renders the `product_list.html` template, passing in the specified category name.

**@app.route("/product/<product_id>")** (Product page)
- Renders the `product_details.html` template, passing in the specified product ID.

**@app.route("/add_to_cart/<product_id>")** (Add to cart)
- Adds the specified product to the user's cart and redirects to the `cart.html` page.

**@app.route("/cart")** (Shopping cart)
- Renders the `cart.html` template.

**@app.route("/checkout")** (Checkout)
- Processes the user's order, including payment and address information. Redirects to a confirmation page.

**@app.route("/search")** (Product search)
- Takes a search query as a parameter and renders the `toy_shop.html` template with filtered products.