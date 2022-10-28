
let field_count = 1;

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
    });

function add_schema_field(){
                    field_count+=1;
                    var schema_comp = $(`<div id="schema${field_count}" class="flex items-stretch grid gap-6 mb-6 md:grid-cols-5">
                    <input type="text" id="json_key" placeholder="json key" />
                    <input type="text" id="col_name" placeholder="column name"/>
                    <div id="datatype"><label for="datatype">datatype</label>
                    <select>
                     <option value="VARCHAR">VARCHAR</option>    <option value="TEXT">TEXT</option>
                      <option value="INT">INT</option>    <option value="FLOAT">FLOAT</option>
                       <option value="BOOLEAN">BOOLEAN</option>    <option value="DATE">DATE</option>
                         <option value="DATETIME">DATETIME</option>    <option value="TIMESTAMP">TIMESTAMP</option>
                     </select></div><div id="constraint">    <label for="constraint">constraint</label>
                     <select multiple>    <option value="UNIQUE">UNIQUE</option>    <option value="PRIMARY KEY">PRIMARY KEY</option>
                   <option value="FOREIGN KEY">FOREIGN KEY</option>    <option value="AUTO INCREMENT">AUTO INCREMENT</option>
                     <option value="NOT NULL">NOT NULL</option>
                     </select></div><button onclick = "remove_schema_field(this);"
                     type="button" class="text-blue-700 border border-blue-700 hover:bg-blue-700 hover:text-white focus:ring-4
                     focus:outline-none focus:ring-blue-300 font-medium rounded-full text-sm p-2.5 text-center inline-flex
                      items-center dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:focus:ring-blue-800">
                       <svg aria-hidden="true" class="w-5 h-5" fill="currentColor"

                       viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path d="M4.00000017,11 L20,11 C20.5522847,11 21,11.4477153 21,12 C21,12.5522847 20.5522847,13 20,
                        13 L4,13 C3.44771525,13 3,12.5522847 3,12 C3,11.4477153 3.44771525,11 4,11 L4.00000017,11 Z" id="Shape">
                        </path></svg>  <span class="sr-only">Icon description</span></button></div>`);

            $("#schema-wrapper").append(schema_comp);
}

function remove_schema_field(element){
   element.closest("#schema").remove()
}

