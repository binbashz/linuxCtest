
let titulo = document.getElementById("encabezado"); // selecionamos  elemento por id 
console.log(titulo.innerHTML); // innerHTML imprime,no en consola

let info = document.getElementById("info"); 
info.style.color = "red" // indicamos cambiar estilo color
console.log(info);


let moreinfo = document.getElementsByName("moreinfo") // elemento por nombre 
console.log(moreinfo[0].innerHTML); // como los name se pueden repetir y el id no, accedemos con la posicion del nodo , array
