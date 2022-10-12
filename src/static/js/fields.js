 $(document).ready(function(){

                $("#unix_socket").parent().hide();
        $('#use_tcp').click(function(e){
            if ($('#use_tcp').prop('checked')){
                $('#unix_socket').parent().hide();
            }else{
                $("#unix_socket").parent().show();
            }
        });
    });