document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-recipe');
    const userInput = document.getElementById('user-search');
    const foundRecipes = document.getElementById("found-recipes");
    let query = ''

    searchForm.addEventListener('submit', function(e){
        e.preventDefault();
        query = userInput.value;
        fetchData();
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