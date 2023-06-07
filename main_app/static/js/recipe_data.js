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
                    let name = item.strMeal
                    const anchorElem = document.createElement('a');
                    anchorElem.innerText = name
                    anchorElem.setAttribute('href', `/about/${item.idMeal}` )
                    resultDiv.appendChild(anchorElem)                    
                })
                                
                console.log(data)
                data.result.forEach(item => console.log(item.strMeal))
            })
            .catch(error => {
                console.error(error)
            });
    }
})    