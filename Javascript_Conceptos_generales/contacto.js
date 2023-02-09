///STORAGE



class Datos {
    constructor(Nombre, email, numero){
    this.Nombre=Nombre;
    this.email=email;
    this.numero=numero;
    }
}

const STORAGE="prestamo"
const formularioDatos = document.getElementById("formulario-datos")
const containerPrestamo =document.getElementById("prestamo")

const mostrarPrestamo =(datos) =>{

containerPrestamo.innerHTML= `<div class="card" style="width: 18rem;">
<div class="card-header"> Datos de ${datos.Nombre} enviados al servicio al cliente </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Email de contacto ${datos.email}</li>
    <li class="list-group-item">Numero telefonico ${datos.numero}</li>
    
  </ul>
</div>`}


const handleSubmit = (event) => {
    event.preventDefault();

    const target =event.target;

    const nuevoDatos = new Datos(target.Nombre.value, target.email.value, target.numero.value)

    console.log(nuevoDatos)

    localStorage.setItem(STORAGE,JSON.stringify( nuevoDatos))

    mostrarPrestamo(nuevoDatos)
    

}

formularioDatos.onsubmit =handleSubmit;

console.log(formularioDatos)

///PROMISE

const datos = new Promise((resolve,rejected) => {
    return setTimeout (()=>{
        if (Datos){
            return resolve("cliente ingreso datos");
        }
        rejected("user mising")
    },10000)
})

datos
.then((res) => {
    console.log(res);
})
.catch ((err)=> {
    console.error(err)
})