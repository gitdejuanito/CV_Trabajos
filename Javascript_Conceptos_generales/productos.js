///EVENTOS////


const productos =[
{
    id: 1,
    nombre: "Prueba de esfuerzo con banda",
    precio: 80,
    imagen: "https://cardiohealth.com.mx/wp-content/uploads/2018/02/Prueba-de-esfuerzo-1-1200x800.jpg"
},

{
    id:2,
    nombre: "Prueba Holter",
    precio: 300,
    imagen: "https://www.topdoctors.mx/files/Image/large/6e8078f53ea118b334a31994a1ca3da7.jpeg"
},

{
    id: 3,
    nombre: "Presión arterial",
    precio: 500,
    imagen: "https://tucardiologo.com.mx/wp-content/uploads/2019/10/monitoreo-ambulatorio-presion-arterial.jpg"
},

];

const contenedor =document.getElementById("contenedor");
const inputSearch=document.getElementById("input-search")

const dibujarProductos= (productos,contenedor) => {
    let acumulador =" "

    productos.forEach(element => {
        acumulador +=`<div class="card" style="width: 18rem;">
        <img src="${element.imagen}" class="card-img-top" alt="${element.nombre}">
        <div class="card-body">
          <h5 class="card-title">${element.nombre}</h5>
          <p class="card-text">Precio: ${element.precio}</p>
          <a href="#" class="btn btn-primary">Cotizar</a>
        </div>
        </div>`
    });

    contenedor.innerHTML=acumulador
}

dibujarProductos(productos,contenedor)

const handleSearch =(e) => {

    console.log(e.target.value);
    
    const filtrados= productos.filter(productos=> productos.nombre.toLocaleLowerCase().includes(e.target.value.toLocaleLowerCase()))

    dibujarProductos(filtrados,contenedor)
}

inputSearch.addEventListener("input", handleSearch )



///STORAGE AND JSON//////

const miVariable = 100;

localStorage.setItem ("primerdatp", miVariable)