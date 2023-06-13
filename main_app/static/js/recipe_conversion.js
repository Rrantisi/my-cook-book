document.addEventListener('DOMContentLoaded', function() {
    
    if(document.querySelector('#conversion-form') || document.querySelector('#substitution-form')){

        /*----- cached elements -----*/
        const conversionResult = document.getElementById('conversion-message');  
        const ingredientName = document.getElementById('ingredient-name');
        const sourceAmount = document.getElementById('source-amount');
        const sourceUnit = document.getElementById('source-unit');
        const targetUnit = document.getElementById('target-unit');
        const conversionForm = document.getElementById('conversion-form');
        const substitutionResult = document.getElementById('substitution-message');  
        const sourceName = document.getElementById('source-name');
        const substitutionForm = document.getElementById('substitution-form');
        
        /*----- event listeners -----*/
        conversionForm.addEventListener('submit', function(e){
            e.preventDefault();
            conversionResult.innerHTML = ''
            nameIngredient = ingredientName.value
            amountSrc = sourceAmount.value
            unitSrc = sourceUnit.value
            unitTarget = targetUnit.value
            fetchConversion();
        })

        substitutionForm.addEventListener('submit', function(e){
            e.preventDefault();
            substitutionResult.innerHTML = ''
            nameSrc = sourceName.value
            fetchSubstitution();
        })

        /*----- fetch function for fetching conversion data from spoonacular api -----*/
        const fetchConversion = async () => {
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
                document.getElementById('conversion-error-message').innerHTML = 'Something Went Wrong..'
            }
        }

        const fetchSubstitution = async () => {
            try {
                const response = await fetch(`/api/substitution/?nameSrc=${nameSrc}` , {
                    method: "GET",
                    headers: {
                        "X-Requested-With": "XMLHttpRequest",
                    }    
                });
                const recipeData = await response.json();
                const result = recipeData.data.substitutes
                for(let i = 0; i < result.length; i++){
                    substitutionResult.innerHTML += `
                    <p>${result[i]}</p>
                `
                }
            } catch(error){
                console.log(error)
                document.getElementById('substitution-error-message').innerHTML = 'No substitutes found.'
            }
        }

    }
})    