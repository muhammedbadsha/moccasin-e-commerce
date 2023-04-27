;(function () {
    const modal = new bootstrap.Modal(document.getElementById('modal'));
    console.log('modal')

    htmx.on("htmx:afterSwap", (e) => {
        // Response targeting #dialog => show the modal
        if (e.detail.target.id === "dialog") {
            console.log("show modal")
            modal.show()
        }
      })
    
      htmx.on("htmx:beforeSwap", (e) => {
        // Empty response targeting #dialog => hide the modal
        if (e.detail.target.id === "dialog" && !e.detail.xhr.response) {
            console.log(!e.detail.xhr.response) 
            console.log("hide modal")
            
            modal.hide()
            e.detail.shouldSwap = false
        }
      })

    htmx.on("hidden.bs.modal", (e) => {
        if(e.target === modal) {
            modal.classList.add('fade-out')
        }
        document.getElementById("dialog").innerHTML = ""
    })

})()