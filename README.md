## Flask Application Design for: A website to sell used clothes. Must have browse, search and transaction capabilities.

### HTML Files

- **index.html**: This page is the main storefront, displaying all available used clothes items.
- **search.html**: This page allows users to search for clothes based on filters like size, color, or type.
- **item_detail.html**: This page displays the details of a specific article of clothing, including its description, price, and availability.
- **cart.html**: This page shows the items that the user has added to their shopping cart.
- **checkout.html**: This page allows the user to complete their purchase.

### Routes

- **browse**: This route displays the **index.html** page, which shows all available clothes items.
- **search**: This route accepts search parameters and displays the results on **index.html**.
- **item_detail/:id**: This route displays the **item_detail.html** page, where :id is the unique identifier of the clothing item.
- **add_to_cart/:id**: This route adds the specified clothing item to the user's shopping cart.
- **show_cart**: This route displays the **cart.html** page, showing all items in the user's shopping cart.
- **checkout**: This route displays the **checkout.html** page, where the user can complete their purchase.