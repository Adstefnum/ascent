 $(document).ready(function(){

                $("#unix_socket").parent().hide();
                $('#use_tcp').click(function(e){
            if ($('#use_tcp').prop('checked')){
                $('#unix_socket').parent().hide();
                $("#host").parent().show();
                $("#port").parent().show();
            }else{
                $("#unix_socket").parent().show();
                $("#host").parent().hide();
                $("#port").parent().hide();
            }
        });


                $("#schema").parent().hide();
                $('#create_table').click(function(e){
            if ($('#create_table').prop('checked')){
                $("#schema").parent().show();
            }else{
                $("#schema").parent().hide();
            }
        });
    });