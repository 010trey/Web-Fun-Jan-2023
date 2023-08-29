// Get all "Add to Cart" buttons
const addToCartButtons = document.querySelectorAll('.add-to-cart');

// Add a click event listener to each button
addToCartButtons.forEach(button => {
    button.addEventListener('click', addToCart);
});

// Function to handle adding a product to the cart
function addToCart(event) {
    const productId = event.target.getAttribute('data-product-id');

    // Send an AJAX request to add the product to the cart
    // You can use libraries like Axios or fetch for the AJAX request
    // Update the cart content dynamically

    // Example of how you might update the cart in the HTML
    const cartBadge = document.getElementById('cart-badge');
    cartBadge.textContent = parseInt(cartBadge.textContent) + 1;
}
