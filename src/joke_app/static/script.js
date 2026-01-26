console.log("script.js loaded"); // <-- keep this for now

document.addEventListener("DOMContentLoaded", () => {
  const deliveryTxt = document.getElementById("delivery");
  const showBtn = document.getElementById("btn-show");

  console.log({ deliveryTxt, showBtn }); // <-- keep this for now

  if (!deliveryTxt || !showBtn) return;

  showBtn.addEventListener("click", () => {
    const isHidden = deliveryTxt.style.display === "" || deliveryTxt.style.display === "none";
    deliveryTxt.style.display = isHidden ? "block" : "none";
    showBtn.textContent = isHidden ? "Hide" : "Show";
  });
});

