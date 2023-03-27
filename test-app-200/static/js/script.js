const formRegistration = document.querySelector('.form-sizing-registration');
const formAccount = document.querySelector('.form-account');
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const errorLog = document.createElement('div');

// text error generator
function setErrorLog(form, textError){
    errorLog.innerText = textError; 
    const lastElementForm = form.lastElementChild;
    lastElementForm.remove();
    form.append(errorLog);
    form.append(lastElementForm);
}

// form registration input value control
if (formRegistration){
    formRegistration.addEventListener('submit',(e)=>{
        for (let element=0; element<(formRegistration.elements.length)-1; element++){
            if (formRegistration[element].value === '' || formRegistration[element].value === null){
                e.preventDefault();
                setErrorLog(formRegistration);
            }  
        }
        if (!(emailRegex.test(formRegistration['Email'].value))){
            e.preventDefault();
            setErrorLog(formRegistration, 'Informations invalide ou incomplète');
        }
        if (formRegistration['Password'].value !== formRegistration['PasswordConfirm'].value){
            e.preventDefault();
            setErrorLog(formRegistration, 'Informations invalide ou incomplète');
        }
    })
}

// form account input value control
if (formAccount){
    for (let element=0; element<(formAccount.elements.length)-1; element++){
        let userInput = formAccount[element]
        userInput.addEventListener('input',(e)=>{
            userInput.setAttribute('value', e.target.value);
        })
    }

    formAccount.addEventListener('submit',(e)=>{
        for (let element=0; element<(formAccount.elements.length)-1; element++){
            console.log(formAccount[element])
            if (formAccount[element].value === '' || formAccount[element].value === null){
                e.preventDefault();
                setErrorLog(formAccount, 'Informations invalide ou incomplète');
            }  
        }
        if (!(emailRegex.test(formAccount['Email'].value))){
            e.preventDefault();
            setErrorLog(formAccount, 'Informations invalide ou incomplète');
        }
    })
}
