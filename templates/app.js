// OpenWeatherMap API anahtarı
const apiKey = 'YOUR_API_KEY_HERE';

// Hava durumu verisini almak için bir fonksiyon
async function fetchWeatherData(city) {
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        
        if (data.cod === 200) {  // Eğer şehir bulunduysa
            updateWeatherUI(data);
        } else {
            alert('City not found!');
        }
    } catch (error) {
        console.error('Error fetching the weather data:', error);
    }
}

// UI güncelleme fonksiyonu
function updateWeatherUI(data) {
    document.getElementById('temperature').textContent = `${data.main.temp} °C`;
    document.getElementById('cityName').textContent = data.name;
    document.getElementById('weather').textContent = data.weather[0].description;
    document.getElementById('humidity').textContent = `${data.main.humidity}%`;
    document.getElementById('pressure').textContent = `${data.main.pressure} hPa`;

    const dayOfWeek = new Date().toLocaleString('en-us', { weekday: 'long' });
    document.getElementById('day').textContent = dayOfWeek;
}

// Form submit eventine dinleyici ekleyelim
document.getElementById('weatherForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Formun sayfayı yeniden yüklemesini engelle
    const city = document.getElementById('cityInput').value;  // Şehir ismini al
    fetchWeatherData(city);  // API'den veri çek
});
