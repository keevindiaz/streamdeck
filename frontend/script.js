function sendCommand(cmd) {
  fetch(`/command?cmd=${cmd}`)
    .then(res => res.text())
    .then(msg => console.log(msg));
}

// 🕒 Actualizar hora
function updateClock() {
  const now = new Date();
  const clock = document.getElementById('clock');
  clock.textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}
setInterval(updateClock, 1000);
updateClock();

// 🌡️ Clima real (requiere tu API key de OpenWeatherMap)
const API_KEY = 'TU_API_KEY';
const ciudad = 'Villa Ballester';

async function getWeather() {
  try {
    const res = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${ciudad}&appid=${API_KEY}&units=metric`);
    const data = await res.json();
    const temp = Math.round(data.main.temp);
    document.getElementById('temp').textContent = `🌡️ Temp: ${temp}°C`;
  } catch (err) {
    console.error('Error al obtener clima:', err);
  }
}
getWeather();

// 📡 Monitoreo de red
async function getSpeed() {
  try {
    const res = await fetch('/speed');
    const data = await res.json();
    document.getElementById('internet').textContent = `📡 Internet: ${data.download} Mbps`;
  } catch (err) {
    console.error('Error al obtener velocidad:', err);
  }
}
getSpeed();
