// Função para a primeira senha no registrar
document.addEventListener("DOMContentLoaded", function() {
    var senhaInput = document.getElementById("senha1");
    var mostrarSenhaIcon = document.getElementById("mostrar1");

    mostrarSenhaIcon.addEventListener("click", function () {
            if (senhaInput.type === "password") {
                senhaInput.type = "text";
                mostrarSenhaIcon.classList.remove("fa-lock");
                mostrarSenhaIcon.classList.add("fa-unlock-alt");
            } else {
                senhaInput.type = "password";
                mostrarSenhaIcon.classList.remove("fa-unlock-alt");
                mostrarSenhaIcon.classList.add("fa-lock");
            }
        });
    });

// Função para a segunda senha no registrar
document.addEventListener("DOMContentLoaded", function() {
    var senhaInput = document.getElementById("senha2");
    var mostrarSenhaIcon = document.getElementById("mostrar2");

    mostrarSenhaIcon.addEventListener("click", function () {
            if (senhaInput.type === "password") {
                senhaInput.type = "text";
                mostrarSenhaIcon.classList.remove("fa-lock");
                mostrarSenhaIcon.classList.add("fa-unlock-alt");
            } else {
                senhaInput.type = "password";
                mostrarSenhaIcon.classList.remove("fa-unlock-alt");
                mostrarSenhaIcon.classList.add("fa-lock");
            }
        });
    });

var updateBTN = document.getElementsByClassName('update-cart');

    for(var i = 0; i < updateBTN.length; i++){
        updateBTN[i].addEventListener('click', function(){
            var productId = this.getAttribute('data-product');
            var action = this.getAttribute('data-action');
            console.log('productId:', productId, 'action:', action)
            console.log('User:', user)
            UserPedido(productId, action)
            
        })
    };

function UserPedido(productId, action){
    var url = "http://127.0.0.1:8000/jogos/update_cart/"
    
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action':action})
    })
    
    .then((response) =>{
        return response.json()
    })

    .then((data)=>{
        location.reload()
    })
}