/////DOM////

const body =document.body

console.log(body.innerHTML)

const color = document.getElementById('facturas');

console.log(color);

color.innerHTML = '<b style="color: red; font-size: 30px"> Se hacen facturas para cualquier tipo de persona </b>'

const nodo= document.querySelector('#facturas')

let input2=document.getElementById("input3")

///EVENTOS//

input2.onkeyup = () => console.log("keyUp")

let miformulario= document.getElementById("formulario")

miformulario.addEventListener("submit", validarFormulario)

function validarFormulario(e){
    e.preventDefault();
    
    console.log("Formulario enviado")
}

