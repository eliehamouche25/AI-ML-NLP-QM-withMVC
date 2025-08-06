 $(document).ready(function () {
    $('#signin-btn').click(function () {
        const username = $('#username').val();
        const password = $('#password').val();

        $.ajax({
            url: '/signin',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ username, password }),
            success: function (response) {
                if (response.status === 'ok') {
                    $('#zone2').html(`
                        <h2>Hello, ${response.username}!</h2>
                        <ul>
                            <li><a href="#" id="go-tools">🔧 Tools</a></li>
                            <li><a href="#" id="go-nlp">💬 NLP Assistant</a></li>
                            <li><a href="#" id="go-ml">📈 ML Predictor</a></li>
                            <li><a href="#" id="go-qm">⚛️ QM Dashboard</a></li>
                        </ul>
                    `);
                    $('#login-form').hide();
                } else {
                    window.location.href = '/signup';
                }
            }
        });
    });

$('#signin-btn').click(function () {
    const username = $('#username').val();
    const password = $('#password').val();

    $.ajax({
        url: '/signin',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ username, password }),
        success: function (response) {
            $('#response').text(response.message);
            if (response.success) {
                window.location.href = '/dashboard';
            }
        },
        error: function (xhr) {
            const error = xhr.responseJSON?.message || 'Sign-in failed.';
            $('#response').text(error);
        }
    });
});

    // Sign Up Logic
    $('#signup-btn').click(function () {
        const username = $('#new-username').val();
        const password = $('#new-password').val();
        const role = $('#new-role').val();

        $.ajax({
            url: '/signup',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ username, password, role }),
            success: function (response) {
                $('#signup-response').text(response.message);
            },
            error: function (xhr) {
                const error = xhr.responseJSON?.message || 'Sign-up failed.';
                $('#signup-response').text(error);
            }
        });
    });
});




