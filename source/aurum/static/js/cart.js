// ===============================
//   LOAD CART FROM SERVER
// ===============================
async function fetchCartItems() {
  const res = await fetch("/api/cart/contents");
  const data = await res.json();
  return data.items || [];
}

async function fetchCartCount() {
  const res = await fetch("/api/cart/count");
  const data = await res.json();
  return data.count || 0;
}

function currency(num) {
  return `$${Number(num).toLocaleString()}`;
}

// ===============================
//   RENDER CART PAGE
// ===============================
async function renderCart() {
  const items = await fetchCartItems();
  const itemsEl = document.getElementById("cart-items");
  const totalEl = document.getElementById("cart-total");

  itemsEl.innerHTML = "";
  let total = 0;

  if (items.length === 0) {
    itemsEl.innerHTML = `<p>Your cart is empty.</p>`;
    totalEl.textContent = "$0";
    updateCartCount(0);
    return;
  }

  items.forEach(item => {
    total += item.price;

    const row = document.createElement("div");
    row.className = "cart-item";
    row.innerHTML = `
      <img src="/static/images/${item.image || ""}" alt="${item.title}">
      <div class="cart-item-info">
        <h3>${item.title}</h3>
        <p>${item.era || ""}</p>
        <p>${currency(item.price)}</p>
      </div>
      <button class="remove-btn" data-id="${item.id}">Remove</button>
    `;
    itemsEl.appendChild(row);
  });

  totalEl.textContent = currency(total);
  updateCartCount(items.length);
}

// ===============================
//   UPDATE NAV CART COUNT
// ===============================
async function updateCartCount(forceCount = null) {
  const cartLink = document.querySelector(".cart-link");
  const count = forceCount ?? await fetchCartCount();
  if (cartLink) cartLink.textContent = `Cart (${count})`;
}

// ===============================
//   REMOVE A SINGLE ITEM
// ===============================
document.addEventListener("click", async (e) => {
  const btn = e.target.closest(".remove-btn");
  if (!btn) return;

  const id = btn.dataset.id;

  await fetch("/api/cart/remove", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ inventory_id: id })
  });

  renderCart();
});

// ===============================
//   CLEAR CART
// ===============================
const clearBtn = document.getElementById("clear-cart");
if (clearBtn) {
  clearBtn.addEventListener("click", async () => {
    await fetch("/api/cart/clear", { method: "POST" });
    renderCart();
  });
}

// ===============================
//   INIT
// ===============================
document.addEventListener("DOMContentLoaded", () => {
  renderCart();
  updateCartCount();
});
