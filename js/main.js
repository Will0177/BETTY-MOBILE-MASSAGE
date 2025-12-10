document.addEventListener("DOMContentLoaded", () => {
  // Scroll reveal
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("show");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2, rootMargin: "0px 0px -60px 0px" }
  );

  document.querySelectorAll(".fade-up").forEach((el) => observer.observe(el));

  // Chat widget
  const chatToggle = document.querySelector(".chat-toggle");
  const chatWidget = document.querySelector(".chat-widget");
  const chatBody = document.querySelector(".chat-body");
  const sliderTrack = document.querySelector("[data-slider]");
  const prevBtn = document.querySelector(".slider-prev");
  const nextBtn = document.querySelector(".slider-next");

  const defaultMessages = [
    "Hello! 👋 How can we help you today?",
    "Are you interested in our services?",
    "We’ll reply in under 2 minutes.",
    "Would you like a free consultation?",
  ];

  if (chatBody) {
    defaultMessages.forEach((msg, idx) => {
      setTimeout(() => {
        const bubble = document.createElement("div");
        bubble.className = "chat-bubble";
        bubble.textContent = msg;
        chatBody.appendChild(bubble);
        chatBody.scrollTop = chatBody.scrollHeight;
      }, 600 * (idx + 1));
    });
  }

  chatToggle?.addEventListener("click", () => {
    chatWidget?.classList.toggle("open");
  });

  // Simple slider
  if (sliderTrack) {
    let index = 0;
    const cards = Array.from(sliderTrack.children);
    const cardWidth = cards[0]?.getBoundingClientRect().width || 0;
    const visible = Math.floor((sliderTrack.parentElement?.getBoundingClientRect().width || 0) / (cardWidth + 16)) || 1;
    const maxIndex = Math.max(0, cards.length - visible);

    const update = () => {
      sliderTrack.style.transform = `translateX(${-index * (cardWidth + 16)}px)`;
    };

    prevBtn?.addEventListener("click", () => {
      index = index <= 0 ? maxIndex : index - 1;
      update();
    });
    nextBtn?.addEventListener("click", () => {
      index = index >= maxIndex ? 0 : index + 1;
      update();
    });

    // auto-play
    setInterval(() => {
      index = index >= maxIndex ? 0 : index + 1;
      update();
    }, 3600);
  }
});
