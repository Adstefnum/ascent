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


            $('#add_more').click(function(e){
                    var schema_comp = '<div id="schema" class="flex items-stretch"><input type="text" id="json_key" placeholder="json key" /><input type="text" id="col_name" placeholder="column name"/><div id="datatype"><label for="datatype">datatype</label><select>    <option value="VARCHAR"></option>    <option value="TEXT"></option>    <option value="INT"></option>    <option value="FLOAT"></option>    <option value="BOOLEAN"></option>    <option value="DATE"></option>    <option value="DATETIME"></option>    <option value="TIMESTAMP"></option></select></div><!-- i need to add a text option to enter the max amount for some of these fields --><div id="constraint">    <label for="constraint">constraint</label><select multiple>    <option value="UNIQUE"></option>    <option value="PRIMARY KEY"></option>    <option value="ID"></option>    <option value="FOREIGN KEY"></option>    <option value="AUTO INCREMENT"></option>    <option value="NOT NULL"></option></select></div><p>hold down the ctrl (windows) or command (mac) button to select multiple options.</p></div>';

            $("#schema").append("<h1>added</h1>");

            })
        });
    });