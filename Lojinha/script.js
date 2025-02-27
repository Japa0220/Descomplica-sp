document.addEventListener("DOMContentLoaded", () => {
    console.log("Sexy Store está pronta para apimentar sua experiência!");
});

function addToCart(productName) {
    alert(`${productName} foi adicionado ao carrinho!`);
}

// Manipulação do formulário de contato
document.addEventListener("DOMContentLoaded", () => {
    const contactForm = document.querySelector("form");
    
    if (contactForm) {
        contactForm.addEventListener("submit", (event) => {
            event.preventDefault();
            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const message = document.getElementById("message").value;
            
            if (name && email && message) {
                alert("Obrigado por entrar em contato, responderemos em breve!");
                contactForm.reset();
            } else {
                alert("Por favor, preencha todos os campos.");
            }
        });
    }
});

// Efeito de destaque nos produtos
document.querySelectorAll(".product").forEach(product => {
    product.addEventListener("mouseenter", () => {
        product.style.transform = "scale(1.05)";
        product.style.transition = "transform 0.3s";
    });
    
    product.addEventListener("mouseleave", () => {
        product.style.transform = "scale(1)";
    });
});

// Adicionar imagens dos produtos
document.addEventListener("DOMContentLoaded", () => {
    const products = [
        { name: "Vibrador Luxo", image: "img/vibrador-luxo.jpg" },
        { name: "Gel Sensual", image: "img/gel-sensual.jpg" }
    ];

    document.querySelectorAll(".product").forEach((product, index) => {
        const img = product.querySelector("img");
        if (img && products[index]) {
            img.src = products[index].image;
            img.alt = products[index].name;
        }
    });
});
