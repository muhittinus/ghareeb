document.getElementById('search').addEventListener('input', function () {
    let query = this.value;
    if (query.length > 0) {
        fetch(`/search?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                let resultsContainer = document.getElementById('results');
                resultsContainer.innerHTML = ''; // Clear previous results
                data.forEach(item => {
                    let li = document.createElement('li');

                    // Create the word element
                    let wordElement = document.createElement('div');
                    wordElement.classList.add('word');
                    wordElement.textContent = item.word;

                    // Create the definition element
                    let definitionElement = document.createElement('div');
                    definitionElement.classList.add('definition');
                    definitionElement.textContent = item.definition;

                    // Append both elements to the list item
                    li.appendChild(wordElement);
                    li.appendChild(definitionElement);

                    // Add the list item to the results container
                    resultsContainer.appendChild(li);
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    } else {
        document.getElementById('results').innerHTML = ''; // Clear results if search is empty
    }
});
