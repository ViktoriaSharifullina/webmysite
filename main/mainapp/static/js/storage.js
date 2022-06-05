var langForm = document.getElementById('lang');

langForm.addEventListener('storage', function(event){
    if(!localStorage.getItem('lang')) {
            populateStorage();
    } else {

         setLang();
    }

})
// создаем новый ключ и передаем ему значение
function populateStorage() {
  localStorage.setItem('lang', langForm.value);
  setLang();
}
// если ключ есть то просто меняем стиль на сайте (язык)
function setLang() {
  var currentLang = localStorage.getItem('lang');
  langForm.value = currentLang;

}

langForm.onchange = populateStorage;