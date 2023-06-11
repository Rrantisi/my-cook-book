document.addEventListener('DOMContentLoaded', function() {
    
    if(document.querySelector('#conversion-form')){

        /*----- cached elements -----*/
        const conversionResult = document.getElementById('conversion-message');  
        const ingredientName = document.getElementById('ingredient-name');
        const sourceAmount = document.getElementById('source-amount');
        const sourceUnit = document.getElementById('source-unit');
        const targetUnit = document.getElementById('target-unit');
        const conversionForm = document.getElementById('conversion-form');
        
        /*----- event listeners -----*/
        conversionForm.addEventListener('submit', function(e){
            e.preventDefault();
            conversionResult.innerHTML = ''
            nameIngredient = ingredientName.value
            amountSrc = sourceAmount.value
            unitSrc = sourceUnit.value
            unitTarget = targetUnit.value
            fetchRecipes();
        })

        /*----- fetch function for fetching conversion data from spoonacular api -----*/
        const fetchRecipes = async () => {
            try {
                const response = await fetch(`/api/conversion/?a=${nameIngredient}&b=${amountSrc}&c=${unitSrc}&d=${unitTarget}` , {
                    method: "GET",
                    headers: {
                        "X-Requested-With": "XMLHttpRequest",
                    }    
                });
                const recipeData = await response.json();
                conversionResult.innerHTML += `
                    <p>${recipeData.data.answer}</p>
                `
            } catch(error){
                console.log(error)
            }
        }
    }
})    