document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('search-form');
    const input = document.getElementById('search-input');
    let query = ''

    form.addEventListener('submit', function(e){
        e.preventDefault();
        query = input.value;
        fetchData(query)
    })

    function fetchData() {
        fetch('/api/recipes/?query=' + query )
            .then(response => response.json())
            .then(data => {
                data.result.forEach(item => {
                    const resultDiv = document.getElementById('result');
                    resultDiv.innerHTML += `
                    <a href="/api/recipes/${item.strMeal}">${item.strMeal}</a><br>
                    `
                })                    
            })
            .catch(error => {
                console.error(error)
            });
    }
})    