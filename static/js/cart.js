var updateBtns=document.getElementsByClassName('update-cart')

for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productName=this.dataset.product;
        
        var action = this.dataset.action;
        console.log('productName:',productName, 'Action:', action);

        console.log('USER:', user);
        if(user == 'AnonymousUser'){
            addCookieItem(productName,action)
        }else{
            updateUserOrder(productName,action)
           

        }
    });


}

function addCookieItem(productName,action){
    console.log("User not logged in ")
    if (action == 'add'){
        if(cart[productName]== undefined){
            cart[productName]={'quantity':1}
            }else{
            cart[productName]['quantity'] += 1
        }
    }

    if (action == 'remove'){
        cart[productName]['quantity'] -= 1
        if (cart[productName]['quantity'] <= 0) {
            console.log('item should be deleted ')
            delete cart[productName];
        }
    }
    console.log('cart:',cart)
    document.cookie='cart=' +JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}


function updateUserOrder(productName,action){
    console.log('User is authenticated, sending data...')
        var url='/update_item/'

        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'productName':productName,'action':action})
        })
            .then((response)=>{
                    return response.json();
        })
            .then((data)=>{
                    console.log('Data:',data);
                     location.reload();
        });


}

// var updateBtns=document.getElementsByClassName('update-cart')

// for(var i=0;i<updateBtns.length;i++){
//     updateBtns[i].addEventListener('click',function(){
//         var productName=this.dataset.product;
        
//         var action = this.dataset.action;
//         console.log('productName:',productName, 'Action:', action);

//         console.log('USER:', user);
//         if(user == 'AnonymousUser'){
//           addCookieItemab(productName,action);

//         }else{
//             updateUserOrderab(productName,action)
           

//         }
//     });


// }



// function addCookieItemab(productName,action){
//     console.log("User not logged in ")
//     if (action == 'add'){
//         if(cart[productName]== undefined){
//             cart[productName]={'quantity':1}
//             }else{
//             cart[productName]['quantity'] += 1
//         }
//     }

//     if (action == 'remove'){
//             cart[productName]['quantity'] -= 1

//         if (cart[productName]['quantity'] <= 0){
//             console.log('item should be deleted ')
//             delete cart[productName];
//         }
//     }
//     console.log('cart:',cart)
//     document.cookie='cart=' +JSON.stringify(cart) + ";domain=;path=/"
//     location.reload()
// }

// function updateUserOrderab(productName,action){
//     console.log('User is authenticated, sending data...')
//         var url='/update_itemab/'

//         fetch(url, {
//             method:'POST',
//             headers:{
//                 'Content-Type':'application/json',
//                 'X-CSRFToken':csrftoken,
//             },
//             body:JSON.stringify({'productName':productName,'action':action})
//         })
//             .then((response)=>{
//                  return response.json();
//         })
//              .then((data)=>{
//                      console.log('Data:',data);
//                      location.reload();
//         });



// }







