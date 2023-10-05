// Supongamos que tienes un elemento <img> con el id "clima-imagen"
var imagenClima = document.getElementById("clima-imagen");

// Llama a la función para obtener datos climáticos y actualizar la imagen
obtenerDatosClimaticosYActualizarImagen("Cuernavaca"); // Puedes pasar la ciudad deseada aquí

// Función para asignar una imagen en función de la descripción del clima
function asignarImagenClima() {
    var imagenClima = document.getElementById("clima-imagen");
    var descripcionClima = imagenClima.getAttribute("data-atributo");

    var imagenURL = "";

    // Realiza un mapeo de la descripción del clima a una imagen específica
    switch (descripcionClima) {
        case "clear sky":
            imagenURL = "../static/images/clearSky.jpg";
            break;
        case "few clouds":
            imagenURL = "../static/images/fewClouds.jpg";
            break;
        case "overcast clouds":
            imagenURL = "../static/images/overcastClouds.jpg"
            break;
        case "drizzle":
            imagenURL = "../static/images/drizzle.jpg"
            break;
        case "rain":
            imagenURL = "../static/images/rain.jpg"
            break;
        case "shower rain":
            imagenURL = "../static/images/showerRain"
            break;
        case "thunderstorm":
            imagenURL = "../static/images/thunderStorm"
            break;
        case "snow":
            imagenURL = "../static/images/snow"
            break;
        case "mist":
            imagenURL = "../static/images/mist"
            break;
        default:
            console.log("Ese clima no existe pa.");
            break;
        }

    // Cambia la imagen en la página
    imagenClima.src = imagenURL;
}