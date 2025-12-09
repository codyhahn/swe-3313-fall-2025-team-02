// ===============================
//  LIVE SEARCH
// ===============================
document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.querySelector("#searchInput");
  const cards = document.querySelectorAll(".art-card");

  if (!searchInput || cards.length === 0) return;

  searchInput.addEventListener("input", () => {
    const query = searchInput.value.toLowerCase().trim();

    cards.forEach(card => {
      const title = card.querySelector("h3")?.textContent.toLowerCase() || "";
      const era = card.querySelector(".era")?.textContent.toLowerCase() || "";
      const price = card.querySelector(".price")?.textContent.toLowerCase() || "";

      const match =
        title.includes(query) ||
        era.includes(query) ||
        price.includes(query);

      card.style.display = match ? "block" : "none";
    });
  });
});


// ===============================
//  PRODUCT MODAL + SERVER CART
// ===============================
document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".art-card");
  const modal = document.getElementById("productModal");
  const closeBtn = document.querySelector(".close-btn");

  const modalImage = document.getElementById("modalImage");
  const modalTitle = document.getElementById("modalTitle");
  const modalEra = document.getElementById("modalEra");
  const modalPrice = document.getElementById("modalPrice");
  const modalDescription = document.getElementById("modalDescription");
  const modalProvenance = document.getElementById("modalProvenance");

  const modalAddBtn = document.getElementById("modalAddCart");
  const cartLink = document.querySelector(".cart-link");

  let selectedItemId = null;

  // OPEN MODAL
  cards.forEach(card => {
    const examineBtn = card.querySelector(".examine-btn");

    examineBtn.addEventListener("click", () => {
      const img = card.querySelector("img").src;
      const title = card.querySelector("h3").textContent;
      const era = card.querySelector(".era").textContent;
      const price = card.querySelector(".price").textContent;
      const id = card.dataset.id;

      selectedItemId = id;

      modalImage.src = img;
      modalTitle.textContent = title;
      modalEra.textContent = era;
      modalPrice.textContent = price;

      modalDescription.textContent = "A timeless artifact from an ancient era.";
      modalProvenance.textContent = "Provenance available upon request.";

      modal.style.display = "flex";
      document.body.style.overflow = "hidden";
    });
  });

  // ADD TO CART VIA API
  modalAddBtn.addEventListener("click", async () => {
    if (!selectedItemId) return;

    const res = await fetch("/api/cart/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ inventory_id: selectedItemId })
    });

    const data = await res.json();

    if (data.success) {
      updateCartCount();
      showPopup();
      closeModal();
    } else {
      alert("Error adding to cart: " + data.error);
    }
  });

  // CLOSE MODAL
  function closeModal() {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  }

  closeBtn.addEventListener("click", closeModal);
  window.addEventListener("click", e => {
    if (e.target === modal) closeModal();
  });

  // ===============================
  //  CART COUNT (SERVER)
  // ===============================
  async function updateCartCount() {
    const res = await fetch("/api/cart/count");
    const data = await res.json();

    if (cartLink)
      cartLink.textContent = `Cart (${data.count})`;
  }

  updateCartCount();

  function showPopup() {
    const popup = document.getElementById("cart-popup");
    popup.classList.add("show");
    setTimeout(() => popup.classList.remove("show"), 1500);
  }
});
