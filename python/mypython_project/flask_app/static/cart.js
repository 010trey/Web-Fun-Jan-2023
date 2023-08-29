// cart.js

// Array to store cart items
let cartItems = [];

// Function to update the cart UI
function updateCartUI() {
    const cartItemsDiv = document.getElementById('cart-items');
    cartItemsDiv.innerHTML = '';

    cartItems.forEach(item => {
        const cartItemDiv = document.createElement('div');
        cartItemDiv.className = 'cart-item';
        cartItemDiv.innerHTML = `
            <p>${item.name} - Price: $${item.price} - Quantity: ${item.quantity}</p>
            <button class="remove-button" data-product-id="${item.id}">Remove</button>
        `;
        cartItemsDiv.appendChild(cartItemDiv);
    });

    const checkoutButton = document.getElementById('checkout-button');
    checkoutButton.disabled = cartItems.length === 0;
}

// Function to add an item to the cart
function addToCart(product) {
    const existingItem = cartItems.find(item => item.id === product.id);
    if (existingItem) {
        existingItem.quantity++;
    } else {
        cartItems.push({
            id: product.id,
            name: product.name,
            price: product.price,
            quantity: 1
        });
    }
    updateCartUI();
}

// Function to remove an item from the cart
function removeFromCart(productId) {
    cartItems = cartItems.filter(item => item.id !== productId);
    updateCartUI();
}

// Attach event listener to dynamically added remove buttons
document.addEventListener('click', event => {
    if (event.target.classList.contains('remove-button')) {
        const productId = parseInt(event.target.getAttribute('data-product-id'));
        removeFromCart(productId);
    }
});
