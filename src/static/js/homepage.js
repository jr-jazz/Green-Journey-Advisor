document.addEventListener('DOMContentLoaded', () => {
    // Welcome Modal
    const welcomeModal = document.getElementById('welcomeModal');
    const closeModal = document.getElementById('closeModal');
    if (welcomeModal) {
        welcomeModal.style.display = 'flex';
        closeModal.addEventListener('click', () => {
            welcomeModal.style.display = 'none';
        });
    }

    // Cookie Consent Modal
    const cookieModal = document.getElementById('cookieModal');
    const acceptCookies = document.getElementById('acceptCookies');
    if (cookieModal && !localStorage.getItem('cookiesAccepted')) {
        cookieModal.style.display = 'block';
        acceptCookies.addEventListener('click', () => {
            cookieModal.style.display = 'none';
            localStorage.setItem('cookiesAccepted', 'true');
        });
    }

    // Carousel
    const carouselInner = document.querySelector('.carousel-inner');
    const carouselItems = document.querySelectorAll('.carousel-item');
    let currentIndex = 0;

    function showSlide(index) {
        if (index >= carouselItems.length) index = 0;
        if (index < 0) index = carouselItems.length - 1;
        carouselInner.style.transform = `translateX(-${index * 100}%)`;
        currentIndex = index;
    }

    document.querySelector('.carousel-control.next').addEventListener('click', () => {
        showSlide(currentIndex + 1);
    });

    document.querySelector('.carousel-control.prev').addEventListener('click', () => {
        showSlide(currentIndex - 1);
    });

    // Auto-slide every 5 seconds
    setInterval(() => showSlide(currentIndex + 1), 5000);
});