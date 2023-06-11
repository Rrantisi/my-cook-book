document.addEventListener('DOMContentLoaded', function() {

    if(document.querySelector('#search-form')){
        /*----- state variables -----*/
        let query = ''

        /*----- cached elements -----*/
        const resultDiv = document.getElementById('result');                    
        const errorDiv = document.getElementById('error');                    
        const form = document.getElementById('search-form');
        const input = document.getElementById('search-input');

        /*----- event listeners -----*/
        form.addEventListener('submit', function(e){
            e.preventDefault();
            query = input.value;
            fetchData()
            resultDiv.innerHTML = '';
            errorDiv.innerHTML = '';
        })

        /*----- function to fetch data from The meal db api using search input -----*/
        function fetchData() {
            fetch('/api/recipes/?s=' + query, {
                method: "GET",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                }
            })
                .then(response => response.json())
                .then(data => {
                    data.result.forEach(item => {
                        resultDiv.innerHTML += `
                        <a href="/api/recipes/${item.strMeal}">
                            <h3>${item.strMeal}</h3>
                        </a><br>
                        `
                    })
                })
                .catch(error => {
                    console.log(error)
                    errorDiv.innerHTML += `
                        <h4>Sorry .. No recipes matched your search. Try something else</h4>
                        `
                });
        }
    }
})    