// Smooth scrolling between snap sections
document.addEventListener("DOMContentLoaded", () => {
  const sections = document.querySelectorAll(".snap-section");
  let isScrolling = false;
  let currentSection = 0;

  const scrollToSection = (index) => {
    if (index < 0 || index >= sections.length) return;
    isScrolling = true;
    sections[index].scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
    setTimeout(() => {
      isScrolling = false;
    }, 1200);
  };

  window.addEventListener(
    "wheel",
    (e) => {
      e.preventDefault();
      if (isScrolling) return;

      if (e.deltaY > 0) {
        currentSection = Math.min(currentSection + 1, sections.length - 1);
      } else {
        currentSection = Math.max(currentSection - 1, 0);
      }
      scrollToSection(currentSection);
    },
    { passive: false }
  );
});
