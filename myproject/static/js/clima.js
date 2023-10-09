function asignarImagenClima(descripcionClima) {
    var imagenClima = document.getElementById("clima-imagen");
    var imagenURL = "";

    // Realiza un mapeo de la descripción del clima a una imagen específica
    switch (descripcionClima.toLowerCase()) { // Convierte la descripción a minúsculas para evitar problemas de mayúsculas y minúsculas
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
        default:
            // Si la descripción del clima no coincide con ningún caso, muestra la imagen predeterminada
            imagenURL = "../static/images/Welcome.jpg";
            break;
    }

    // Cambia la imagen en la página si se encontró una URL de imagen válida
    if (imagenURL) {
        imagenClima.src = imagenURL;
    }
}

    function aplicarAnimaciones(elemento) {
        // Elimina la clase "aparecer" para reiniciar la animación
        elemento.classList.remove("aparecer");

        // Aplica la clase "aparecer" para activar la animación
        elemento.classList.add("aparecer");

        // Después de un breve retraso, agrega las propiedades de animación
        setTimeout(function () {
            elemento.style.opacity = 1;
            elemento.style.transform = "translateY(0)";
        }, 100); // Ajusta el tiempo de retraso según sea necesario
    }
    