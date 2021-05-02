function disableButton(event){
     event.target.disabled = true;
     console.log('now')
}

document.getElementById("like").addEventListener('click', disableButton)