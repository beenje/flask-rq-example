$(document).ready(function() {

  // flash an alert
  // remove previous alerts by default
  // set clean to false to keep old alerts
  function flash_alert(message, category, clean) {
    if (typeof(clean) === "undefined") clean = true;
    if(clean) {
      remove_alerts();
    }
    var htmlString = '<div class="alert alert-' + category + ' alert-dismissible" role="alert">'
    htmlString += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
    htmlString += '<span aria-hidden="true">&times;</span></button>' + message + '</div>'
    $(htmlString).prependTo("#mainContent").hide().slideDown();
  }

  function remove_alerts() {
    $(".alert").slideUp("normal", function() {
      $(this).remove();
    });
  }

  // submit form
  $("#submit").on('click', function() {
    flash_alert("Running " + $("#task").val() + "...", "info");
    $.ajax({
      url: $SCRIPT_ROOT + "/_run_task",
      data: $("#taskForm").serialize(),
      method: "POST",
      dataType: "json",
      success: function(data) {
        flash_alert(data.result, "success");
      },
      error: function(jqXHR, textStatus, errorThrown) {
        flash_alert(JSON.parse(jqXHR.responseText).message, "danger");
      }
    });
  });

});
