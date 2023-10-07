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
    