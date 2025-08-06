// static/js/search.js
$(document).ready(function () {
    $('#search-input').on('keyup', function () {
        let query = $(this).val();
        if (query.length > 1) {
            $.ajax({
                url: '/search',
                type: 'GET',
                data: { q: query },
                success: function (data) {
                    $('#search-results').html(data);
                }
            });


 $(document).ready(function () {
    // Handle search
    $('#search-button').click(function () {
        let query = $('#search-input').val();
        $.get('/search', { q: query }, function (data) {
            $('#zone4-content').html(data);
        });
    });

    // Handle option click
    $('.option-btn').click(function () {
        let name = $(this).data('name');
        $.get(`/option/${name}`, function (data) {
            $('#zone4-content').html(data);
        });
    });
});



document.getElementById('search-btn').addEventListener('click', () => {
  const query = document.getElementById('search-input').value.trim();

  if (!query) return;

  fetch(`/search?q=${encodeURIComponent(query)}`)
    .then(response => response.json())
    .then(data => {
      const section = document.getElementById('search-result-section');
      const container = document.getElementById('search-results');

      container.innerHTML = ''; // clear previous
      section.style.display = 'block'; // make it visible

      if (data.results.length === 0) {
        container.innerHTML = '<p>No results found.</p>';
      } else {
        data.results.forEach(item => {
          const p = document.createElement('p');
          p.innerHTML = `<strong>${item}</strong>`;
          container.appendChild(p);
        });
      }
    })
    .catch(error => {
      console.error('Search error:', error);
    });
});