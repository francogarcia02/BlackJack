var aviso = "-La contraseña no debe tener menos de 8 caracteres -No debe contener unicamente numeros"


function AlertError() {
    let p1 = document.getElementById("password1").value;
    let p2 = document.getElementById("password2").value;
    if (p1!=p2){
        alert("Confeccione correctamente su contraseña")
    }
    if (String.length(p1)<8){
        alert("Su contraseña no debe tener menos de 8 caracteres")
    }
    alert(p1);

}