document.addEventListener('DOMContentLoaded', function() {

    if(document.querySelector('#search-recipe')){

        /*----- state variables -----*/
        let query = ''

        /*----- cached elements -----*/
        const searchForm = document.getElementById('search-recipe');
        const userInput = document.getElementById('user-search');
        const foundRecipes = document.getElementById('found-recipes');
    
        /*----- event listeners -----*/
        searchForm.addEventListener('submit', function(e){
            e.preventDefault();
            query = userInput.value;
            fetchData();
            foundRecipes.innerHTML = '';
        })

        /*----- function to fetch recipes from database based on user input -----*/
        async function fetchData() {
            try {
                const response = await fetch('/recipes/find_recipes/?query=' + query, {
                    method: "GET",
                    headers: {
                        "X-Requested-With": "XMLHttpRequest",
                    }
                });
                const data = await response.json()
                data.forEach(item => {
                    foundRecipes.innerHTML += `
                    <a href="/api/recipes/${item.name}">
                        <h3>${item.name}</h3>
                    </a><br>
                    `
                })        
            } catch (error){
                console.error(error)
            }
        }    
    }
})