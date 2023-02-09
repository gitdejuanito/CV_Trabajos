///DOM///

const body =document.body

console.log(body.innerHTML)

const cambiar = document.getElementById('aclaracion');

console.log(cambiar);

cambiar.innerHTML = '<b style="color: red; font-size: 30px"> Para cualquier duda de la ubicacion nos puede llamar el 994565123  </b>'

const nodoParrafos = document.querySelector('#aclaracion')

console.log(nodoParrafos)