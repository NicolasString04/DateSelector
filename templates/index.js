<script>
  function selecionarLocal(elemento, url) {
    // Remove classe 'selecionado' de todos
    document.querySelectorAll('.local').forEach(el => {
      el.classList.remove('selecionado');
    });

    // Marca este como selecionado
    elemento.classList.add('selecionado');

    // Redireciona para o link do local
    window.open(url, '_blank');
  }
</script>
