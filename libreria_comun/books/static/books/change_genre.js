select = document.getElementById('inlineFormSelectPref')
form = document.getElementById('genre_list')

function change_genre(event)  {
    if(select.value.startsWith('/')) {
        window.location = select.value;
        event.preventDefault();
    }
}

form.addEventListener("submit", change_genre)
