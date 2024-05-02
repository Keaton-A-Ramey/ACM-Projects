function getWeather() {
    // GET API KEY FROM openweathermap.org
    const apiKey = 'YOUR-KEY';
    const city = document.getElementById('city').value;

    if (!city) {
        alert('Please enter a city');
        return;
    }

    const currentWeatherURL = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
    const forecastURL = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}`;

    fetch (currentWeatherURL)
        .then(response => response.json())
        .then(data => {
            displayWeather(data);
        })
        .catch(error => {
            console.error('Error fetching current weather data: ', error);
            alert('Error fetching current weather data. Try again.');
        });

    fetch (forecastURL)
        .then(response => response.json())
        .then(data => {
            displayHourlyForecast(data.list);
        })
        .catch(error => {
            console.error('Error fetching current weather data: ', error);
            alert('Error fetching current weather data. Try again.');
        });

}

function displayWeather(data) {

    const tempDivInfo = document.getElementById('temp-div');
    const weatherInfoDiv = document.getElementById('weather-info');
    const weatherIcon = document.getElementById('weather-icon');
    const hourlyForecastDiv = document.getElementById('hourly-forecast');

    // When calling it again, need this for clearing previous output
    weatherInfoDiv.innerHTML = '';
    hourlyForecastDiv.innerHTML = '';
    tempDivInfo.innerHTML = '';
    
    if (data.cod === '404') {
        weatherInfoDiv.innerHTML = `<p>${data.message}</p>`;
    } else {

        const cityName = data.name;
        const temperature = Math.round((item.main.temp - 273.15) * (9 / 5) + 32);
        const description = data.weather[0].description;
        const iconCode = data.weather[0].icon;
        const iconURL = `https://openweathermap.org/img/wn/${iconCode}@4x.png`;

        const temperatureHTML = `<p>${temperature} F</p>`;
        const weatherHTML = `
            <p>${cityName}</p>
            <p>${description}</p>
        `;

        tempDivInfo.innerHTML = temperatureHTML;
        weatherInfoDiv.innerHTML = weatherHTML;
        weatherIcon.src = iconURL;
        weatherIcon.alt = description;

        showImage();
    }
}

function displayHourlyForecast(hourlyData) {
    const hourlyForecastDiv = document.getElementById('hourly-forecast');
    const next24hours = hourlyData.slice(0,8);

    next24hours.forEach(item => {
        const dateTime = new Date(item.dt * 1000);
        const hour = dateTime.getHours();
        const temperature = Math.round((item.main.temp - 273.15) * (9 / 5) + 32);
        const iconCode = item.weather[0].icon;
        const iconURL = `https://openweathermap.org/img/wn/${iconCode}.png`;

        const hourlyItemHTML = `
            <div class="hourly-item">
                <span>${hour}:00</span>
                <img src="${iconURL}" alt="Hourly Weather Icon">
                <span>${temperature} F</span>
            </div>
        `

        hourlyForecastDiv.innerHTML += hourlyItemHTML;
    });
}

function showImage() {
    const weatherIcon = document.getElementById('weather-icon');
    // You have to set the display to block for it to work.
    weatherIcon.style.display = 'block';
}