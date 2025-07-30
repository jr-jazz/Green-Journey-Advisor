function togglePaymentFields() {
  const paymentMethod = document.getElementById('payment_method').value;
  const creditCardFields = document.getElementById('credit-card-fields');
  const paypalFields = document.getElementById('paypal-fields');
  creditCardFields.classList.add('hidden');
  paypalFields.classList.add('hidden');
  if (paymentMethod === 'Credit Card') {
    creditCardFields.classList.remove('hidden');
  } else if (paymentMethod === 'PayPal') {
    paypalFields.classList.remove('hidden');
  }
}

function updatePrice() {
  const startPoint = document.getElementById('start_point').value;
  const endPoint = document.getElementById('end_point').value;
  const adults = parseInt(document.getElementById('adults').value) || 1;
  const children = parseInt(document.getElementById('children').value) || 0;
  const pricePreview = document.getElementById('price-preview');
  const priceValue = document.getElementById('price-value');

  if (!startPoint || !endPoint || startPoint === endPoint) {
    pricePreview.classList.add('hidden');
    return;
  }

  fetch('/get_price', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `start_point=${encodeURIComponent(startPoint)}&end_point=${encodeURIComponent(endPoint)}`
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        pricePreview.classList.add('hidden');
      } else {
        const basePrice = data.price;
        const totalPrice = (basePrice * adults) + (basePrice * 0.5 * children);
        priceValue.textContent = totalPrice.toFixed(2);
        pricePreview.classList.remove('hidden');
      }
    })
    .catch(error => {
      console.error('Error fetching price:', error);
      pricePreview.classList.add('hidden');
    });
}