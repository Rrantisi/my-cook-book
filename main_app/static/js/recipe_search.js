document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-recipe');
    const userInput = document.getElementById('user-search');
    let query = ''

    searchForm.addEventListener('submit', function(e){
        e.preventDefault();
        query = userInput.value;
        fetchData()
    })

    function fetchData() {
        fetch('/recipes/find_recipes/?query=' + query, {
            method: "GET",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
            },
        })
            .then(response => response.json())
            .then(data => {
                data.forEach(item => {
                    console.log(item.name)
                    const foundRecipes = document.getElementById('found-recipes');                    
                    foundRecipes.innerHTML += `
                    <a href="/api/recipes/${item.name}">
                        <h3>${item.name}</h3>
                    </a><br>
                    `

                })
                
                })
            .catch(error => {
                console.error(error)
            });
    }
})