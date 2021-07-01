function add_new_sensor() {
    var form = document.getElementsByClassName("form");
    form.css("visibility", "visible");
    var span = document.getElementsByClassName("close");
    span.onclick = function () {
        form.css("visibility", "hidden")
    };
    window.onclick = function (event) {
        if (event.target === form) {
            form.css("visibility", "hidden");
        }
    }
}