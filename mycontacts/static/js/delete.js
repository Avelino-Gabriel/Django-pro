const deletar = document.getElementById('delete')

deletar.addEventListener('click', function(e) {
    e.preventDefault()
    var meu_valor = true; // Este é o valor que você quer passar
    
    // Definindo o valor do input escondido
    document.getElementById('meu-valor-input').value = meu_valor;
});