
;(function () {
  
    const toastElement = document.getElementById("toast")
    const toastBody = document.getElementById("toast-body")
    const toast = new bootstrap.Toast(toastElement,{delay:2000})
    // const toast = bootstrap.Toast.getOrCreateInstance(toastElement)
  
    htmx.on("showMessage", (e) => {
      console.log("showMessage",e)
        toastBody.innerText = e.detail.value
        toast.show()
      })
})()
