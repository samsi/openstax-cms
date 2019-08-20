django.jQuery(function ($) {
    $(document).ready(function(){
        var status = document.getElementById("id_status");
        var resolution = document.getElementById("id_resolution");

        var savebtn = $('input[name="_save"]');
        var savenewbtn = $('input[name="_saveasnew"]');
        var savecontbtn = $('input[name="_continue"]');

        $('#id_status, #id_resolution').change(function(){
            if (!status.options[status.selectedIndex].defaultSelected || !resolution.options[resolution.selectedIndex].defaultSelected) {
                savebtn.val('Save and email user');
                savenewbtn.val('Save as new and email user');
                savecontbtn.val('Save, email user, and continue editing');
            } else {
                savebtn.val('SAVE');
                savenewbtn.val('Save as new');
                savecontbtn.val('Save and continue editing');
            }
        });

        // Commented out as content team does not want to deal with popup.
        // $('form').submit(function() {
        //     if (!status.options[status.selectedIndex].defaultSelected || !resolution.options[resolution.selectedIndex].defaultSelected) {
        //         var c = confirm("User who sent this errata will receive an email. Do you still want to continue?");
        //         return c;
        //     } else {
        //         return true;
        //     }
        // });
    })
})