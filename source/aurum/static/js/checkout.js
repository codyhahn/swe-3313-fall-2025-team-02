document.addEventListener("DOMContentLoaded", () => {

  const summaryItems = document.getElementById("summary-items");
  const summaryTotal = document.getElementById("summary-total");
  const checkoutForm = document.getElementById("checkout-form");

  const confirmModal = document.getElementById("confirmModal");
  const confirmYes = document.getElementById("confirmYes");
  const confirmNo = document.getElementById("confirmNo");

  const subtotalElem = document.getElementById("subtotal");
  const taxElem = document.getElementById("tax");
  const shippingElem = document.getElementById("shippingCost");
  const totalElem = document.getElementById("total");

  const shippingOptions = document.querySelectorAll(".shipping-option");

  let cart = [];  // <-- from DATABASE
  let selectedShipping = 29; // default Overnight

  // ============================
  // Load cart from server
  // ============================
  async function loadCart() {
    const res = await fetch("/api/cart/contents");
    const data = await res.json();
    cart = data.items || [];
    renderSummary();
    calculateTotals();
  }

  // ============================
  //  Render cart summary
  // ============================
  function renderSummary() {
    summaryItems.innerHTML = "";

    if (cart.length === 0) {
      summaryItems.innerHTML = "<p>Your cart is empty.</p>";
      summaryTotal.textContent = "$0";
      return;
    }

    let total = 0;

    cart.forEach(item => {
      const price = Number(item.price) || 0;
      total += price;

      const div = document.createElement("div");
      div.classList.add("summary-item");
      div.innerHTML = `
        <p>${item.title} — <strong>$${price.toLocaleString()}</strong></p>
      `;
      summaryItems.appendChild(div);
    });

    summaryTotal.textContent = `$${total.toLocaleString()}`;
  }

  // ============================
  //  Compute totals
  // ============================
  function calculateTotals() {
    const subtotal = cart.reduce((sum, item) => sum + Number(item.price || 0), 0);
    const tax = subtotal * 0.06;
    const total = subtotal + tax + selectedShipping;

    subtotalElem.textContent = `$${subtotal.toLocaleString()}`;
    taxElem.textContent = `$${tax.toFixed(2)}`;
    shippingElem.textContent = `$${selectedShipping.toLocaleString()}`;
    totalElem.textContent = `$${total.toLocaleString()}`;

    return { subtotal, tax, total };
  }

  // Default option
  shippingOptions[0].classList.add("active");

  // Shipping selection
  shippingOptions.forEach(option => {
    option.addEventListener("click", () => {
      shippingOptions.forEach(o => o.classList.remove("active"));
      option.classList.add("active");

      selectedShipping = parseFloat(option.dataset.cost);
      calculateTotals();
    });
  });

  // ============================
  // On submit → show confirmation modal
  // ============================
  checkoutForm.addEventListener("submit", (e) => {
    e.preventDefault();

    if (cart.length === 0) {
      alert("Your cart is empty.");
      return;
    }

    confirmModal.classList.add("show");
  });

  confirmNo.addEventListener("click", () => {
    confirmModal.classList.remove("show");
  });

  // ============================
  // Confirm purchase → API checkout
  // ============================
  confirmYes.addEventListener("click", async () => {
    confirmModal.classList.remove("show");

    try {
      const response = await fetch("/api/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          shipping: selectedShipping
        })
      });

      const result = await response.json();

      if (!response.ok) {
        alert(result.error || "Checkout failed.");
        return;
      }

      const orderId = result.order_id;

      // Redirect to receipt
      window.location.href = `/receipt/${orderId}`;

    } catch (err) {
      console.error(err);
      alert("An unexpected error occurred.");
    }
  });

  // ============================
  // Load DB cart on page load
  // ============================
  loadCart();

});
