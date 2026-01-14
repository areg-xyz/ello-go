document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('carousel');
    const scrollContainer = document.querySelector('.comic-border'); // Or window if body scrolls

    // We want to rotate the carousel based on scroll position
    // Total 360 degrees over some pixel distance

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        // Sensitivity: 1 degree per 5 pixels
        const rotation = scrollY / 5;

        // Rotate the entire carousel container
        // Since the tiles are arranged in a Y-axis ring, we rotate Y.
        // Negative rotation to spin "forward" when scrolling down
        carousel.style.transform = `translateZ(-400px) rotateY(${-rotation}deg)`;
    });
});
