document.addEventListener('DOMContentLoaded', function() {
    const resultDiv = document.getElementById('result');                    
    const errorDiv = document.getElementById('error');                    
    const form = document.getElementById('search-form');
    const input = document.getElementById('search-input');
    let query = ''

    input.addEventListener('input', () => {      
        resultDiv.innerHTML = '';
        errorDiv.innerHTML = '';
    })

    form.addEventListener('submit', function(e){
        e.preventDefault();
        query = input.value;
        fetchData()
    })

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
                    <h4>Sorry .. No recipes matched your search. Try something else</h4>`
            });
    }
})    