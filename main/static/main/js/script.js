  document.getElementById('property_type').addEventListener('change', function() {
    var propertyType = this.value;
    // Перевіряємо вибір типу нерухомості
    if (propertyType === 'apartment') {
      // Показуємо поля для квартири
      document.getElementById('apartment_fields').style.display = 'block';
      document.getElementById('house_fields').style.display = 'none';
    } else if (propertyType === 'house') {
      // Показуємо поля для будинку
      document.getElementById('apartment_fields').style.display = 'none';
      document.getElementById('house_fields').style.display = 'block';
    }
  });

  // Ініціалізація при завантаженні сторінки, щоб правильно відображалися поля
  window.onload = function() {
    var propertyType = document.getElementById('property_type').value;
    if (propertyType === 'apartment') {
      document.getElementById('apartment_fields').style.display = 'block';
      document.getElementById('house_fields').style.display = 'none';
    } else if (propertyType === 'house') {
      document.getElementById('apartment_fields').style.display = 'none';
      document.getElementById('house_fields').style.display = 'block';
    }
  }
    const categoryField = document.querySelector('[name="category"]');
    const apartmentFields = document.getElementById('apartment_fields');
    const houseFields = document.getElementById('house_fields');

    categoryField.addEventListener('change', function() {
        if (this.value === 'Квартира') {
            apartmentFields.style.display = 'block';
            houseFields.style.display = 'none';
        } else if (this.value === 'Будинок') {
            houseFields.style.display = 'block';
            apartmentFields.style.display = 'none';
        }
    });

    // Початковий стан
    if (categoryField.value === 'Квартира') {
        apartmentFields.style.display = 'block';
        houseFields.style.display = 'none';
    } else {
        houseFields.style.display = 'block';
        apartmentFields.style.display = 'none';
    }