// script.js

// Array para almacenar los productos seleccionados
var cartItems = [];

// Función para agregar un producto al carrito
function addToCart(productId) {
  cartItems.push(productId);
  updateCart();
}

// Función para actualizar el carrito de compras
function updateCart() {
  var cartList = document.getElementById('cart-items');
  cartList.innerHTML = '';

  for (var i = 0; i < cartItems.length; i++) {
    var productId = cartItems[i];
    var li = document.createElement('li');
    li.textContent = 'Producto ' + productId;
    cartList.appendChild(li);
  }
}

// Función para finalizar la compra
function checkout() {
  if (cartItems.length > 0) {
    alert('¡Gracias por tu compra!');
    cartItems = [];
    updateCart();
  } else {
    alert('El carrito está vacío. Agrega algunos productos antes de finalizar la compra.');
  }
}
