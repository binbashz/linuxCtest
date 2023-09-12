

// Llamamos elementos por id, nombre modificamos y agregamos eventos , tambien visualizamos en html 



let titulo = document.getElementById("encabezado"); // selecionamos  elemento por id 
console.log(titulo.innerHTML); // innerHTML imprime,no en consola

let info = document.getElementById("info"); 
info.style.color = "red" // indicamos cambiar estilo color
console.log(info);


let moreinfo = document.getElementsByName("moreinfo") // elemento por nombre 
console.log(moreinfo[0].innerHTML); // como los name se pueden repetir y el id no, accedemos con la posicion del nodo , array



const miParrafo = document.getElementById("miParrafo");

//  evento de clic al párrafo
miParrafo.addEventListener("click", function() {
  // Agrega aquí el código que deseas que se ejecute cuando se hace clic en el párrafo
  alert("Se hizo click en el párrafo");
});

//  movimiento al párrafo )
miParrafo.style.position = "relative";
miParrafo.style.left = "0px";

//  mover el párrafo
function moverParrafo() {
  let posicionActual = parseInt(miParrafo.style.left) || 0;
  posicionActual += 10; // Cambia la posición por 10 píxeles hacia la derecha
  miParrafo.style.left = posicionActual + "px";
}

// Llama a la función para mover el párrafo cuando se hace clic en él
miParrafo.addEventListener("click", moverParrafo);
