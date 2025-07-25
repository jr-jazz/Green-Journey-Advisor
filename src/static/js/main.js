document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('addOptionForm');
    if (form) {
        form.addEventListener('submit', (e) => {
            const carbonFootprint = document.getElementById('carbon_footprint').value;
            if (carbonFootprint <= 0) {
                e.preventDefault();
                alert('Carbon footprint must be greater than 0.');
            }
        });
    }
});