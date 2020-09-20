$(document).ready(function() {
    $("#connect-button").click(function() {
        const url = "";
        const info

        $.ajax({
            url: url,
            type: "POST",
            data: JSON.stringify(info),
            processData: false,
            contentType: "application/json; charset=UTF-8",
            complete: function() {
                console.log("request complete!");
                window.location.reload();
            }
        });

    });
});
