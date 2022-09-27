// var updateBtns = document.getElementsByClassName('update-cart')

// for(var i = 0; i < updateBtns.length; i++){
//     updateBtns[i].addEventListener('click',function(){
//         var productId = this.dataset.product 
//         var action = this.dataset.action
//         console.log('productId:',productId,'action:',action)

//     })
// }


// function funcprice(){
//     var price = document.getElementById('productPrice').value
//     return price
// }
function funcQuantity(){
    var quantity = document.getElementById('product_quty').value
    
    console.log(quantity)
    return quantity

}
var quickViewBut = document.getElementsByClassName('addToCart')
    for(var j = 0;j < quickViewBut.length; j++){
        quickViewBut[j].addEventListener('click',function(){
            var productId = this.dataset.product 
            var action = this.dataset.action
            var quantity= funcQuantity();
            // var price = funcprice();
            console.log('productId:',productId,'action:',action,'product_quantity:',quantity)
            if (user === 'AnonymousUser'){
                print('the user doesnot login')
            }
            else{
            updateUserOrder(productId,action,quantity)
            }
        })
    }
function updateUserOrder(productId,action,quantity){
    // var url = 'product/updateItem'
    fetch('product/updateItem', {
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'X-Requested-With':'XMLHttpRequest',
            'X-CSRFToken':csrftoken,

        },
        body:JSON.stringify({'productId':productId,'action':action,'quantity':quantity})
        })
        .then(response=>{
            return response.json()
        })
        .then((data)=>{
            console.log('data:',data)
        })
}