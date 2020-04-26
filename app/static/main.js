$(document).ready(function () {
    console.log("ready!");
    $('#try-again').hide();

    $("form").on("submit", function () {
        console.log("Form submitted")

        var valueOne = $('input[name="location"]').val()
        console.log(valueOne)

        $.ajax({
            type: "POST",
            url: "/",
            data: { first: valueOne },
            success: function (results) {
                if (results.items.length > 0) {
                    $('input').hide();
                    $('#try-again').show();
                    $('#search').text("Try again?");
                    
                    // generate random object
                    var randNum = Math.floor(Math.random() * Object.keys(results.items).length)
                    console.log(results.items[randNum]);
                    
                    // get user id and search for city, repos and followers..
                    var user_id = results.items[randNum].login
                    
                    fetch('https://api.github.com/users/' + user_id)
                    .then(response => response.json())
                    .then(data => {
                        console.log(data)
                        $("#results").html(
                            '<a href="' + results.items[randNum].html_url + '">' + results.items[randNum].login +
                            '</a><br><img src="' + results.items[randNum].avatar_url + '" class="avatar">' + '<br>' +
                            data.location + '<br>' + data.public_repos + ' Repos' + '<br>' + data.followers + ' Followers'
                        )
                    })
                    .catch(error => console.error(error))

                } else {
                    $('#results').html('Oops.. Please try again.')
                    $("input").val("")
                }
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    $('#try-again').on('click', function () {
        $('#search').text("Find me a developer!");
        $('input').val('').show();
        $('#try-again').hide();
        $('#results').html('');
    });

});
