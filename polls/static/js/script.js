$(document).ready(function() {
    $("#myModal").modal('show');
});  

  $('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})
$(document).ready(function(){
// Prepare the preview for profile picture
    $("#wizard-picture").change(function(){
        readURL(this);
    });
});
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#wizardPicturePreview').attr('src', e.target.result).fadeIn('slow');
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$(document).ready(function() {
    $("#input-res-1").fileinput({
        uploadUrl: "/",
        enableResumableUpload: true,
        initialPreviewAsData: true,
        maxFileCount: 5,
        theme: 'fas',
        deleteUrl: '/',
        fileActionSettings: {
            showZoom: function(config) {
                if (config.type === 'pdf' || config.type === 'image') {
                    return true;
                }
                return false;
            }
        }
    });
});