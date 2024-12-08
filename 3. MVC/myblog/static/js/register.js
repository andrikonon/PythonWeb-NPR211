(() => {
    'use strict'
    
    const forms = document.querySelectorAll('.needs-validation')
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            
            const password1 = document.getElementById('password1').value
            const password2 = document.getElementById('password2').value
            
            if (password1 !== password2) {
                console.log(password1, password2)
                event.preventDefault()
                event.stopPropagation()
                document.getElementById('password2').classList.remove('is-valid')
                document.getElementById('password2').classList.add('is-invalid')
            } else {
                document.getElementById('password2').classList.remove('is-invalid')
                document.getElementById('password2').classList.add('is-valid')
            }
            
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }
            
            form.classList.add('was-validated')
        }, false)
    })
})()