function asignaUsuario(idUsuario, grupos){
    document.getElementById('idUsuario').value = idUsuario;
    grps = grupos.split('-');
    grps.length = grps.length - 1;

    $('#formGrupos input[type=checkbox]').each(function(){
        $(this).prop("checked", false);
        if (grps.includes($(this).prop('name'))){
            $(this).prop("checked", true);
        }
    });
}


$('#id_estado').change(function(e){
    let token = $('[name="csrfmiddlewaretoken"]').val();
    let url = $(this).data('url');
    $.ajax({
        type: 'POST',
        url: url,
        data: {'id_estado':$(this).val(), 'csrfmiddlewaretoken': token},
        success: function(data){
            let html= '';
            $.each(data, function(llave, valor){
                html+=`<option value="${valor.id}">${valor.nombre}</option>`
            });
            $('#id_municipio').html(html); 
        },
    });
});

