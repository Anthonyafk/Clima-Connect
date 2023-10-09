/**
 * Asigna una imagen correspondiente a la descripción del clima a un elemento HTML.
 * 
 * @param {string} descripcionClima - Descripción textual del clima.
 * @param {string} idImagen - ID del elemento HTML al que se asignará la imagen.
 */
function asignarImagenClima(descripcionClima, idImagen) {
    var imagenClima = document.getElementById(idImagen); // Obtiene el elemento usando el ID proporcionado.
    var imagenURL = "";

    // Mapea la descripción del clima a una URL de imagen específica.
    switch (descripcionClima.toLowerCase()) {
        case "clear sky":
            imagenURL = "../static/images/clearSky.jpg";
            break;
        case "light rain":
            imagenURL = "../static/images/lightRain.jpg";
            break;
        case "scattered clouds":
            imagenURL = "../static/images/scatteredClouds.jpg"
            break;
        case "few clouds":
            imagenURL = "../static/images/fewClouds.jpg";
            break;
        case "overcast clouds":
            imagenURL = "../static/images/overcastClouds.jpg";
            break;
        case "drizzle":
            imagenURL = "../static/images/drizzle.jpg";
            break;
        case "rain":
            imagenURL = "../static/images/rain.jpg";
            break;
        case "heavy rain":
            imagenURL = "../static/images/showerRain.jpg";
            break;
        case "thunderstorm":
            imagenURL = "../static/images/thunderStorm.jpg";
            break;
        case "snow":
            imagenURL = "../static/images/snow.jpg";
            break;
        case "mist":
            imagenURL = "../static/images/mist.jpg";
            break;
        case "broken clouds":
            imagenURL = "../static/images/broken-clouds.jpg";
            break;
        case "moderate rain":
            imagenURL = "../static/images/moderate-rain.jpg";
            break;
        default:
            // Si la descripción del clima no coincide con ningún caso, muestra la imagen predeterminada
            imagenURL = "../static/images/Welcome.jpg";
            break;
    }

    // Asigna la imagen al elemento con el id proporcionado
    imagenClima.src = imagenURL;
}


    /**
 * Aplica una animación de aparición a un elemento HTML.
 * 
 * @param {HTMLElement} elemento - Elemento al que se aplicará la animación.
 */
    function aplicarAnimaciones(elemento) {
    // Reinicia la animación eliminando la clase "aparecer".
    elemento.classList.remove("aparecer");

    // Activa la animación añadiendo la clase "aparecer".
    elemento.classList.add("aparecer");

    // Después de un breve retraso, aplica las propiedades de animación.
    setTimeout(function () {
        elemento.style.opacity = 1;
        elemento.style.transform = "translateY(0)";
    }, 100); // Duración del retraso antes de aplicar las propiedades de animación.
}
    
