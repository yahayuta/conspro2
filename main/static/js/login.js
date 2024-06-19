$(document).ready(function(){
    const inputElements = document.querySelectorAll('input[type="text"], input[type="password"]');
	inputElements.forEach(inputElement => {
		inputElement.classList.add('form-control');
	});
});
