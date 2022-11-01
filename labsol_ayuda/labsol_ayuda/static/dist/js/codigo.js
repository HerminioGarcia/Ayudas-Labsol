const btn_agregar = document.getElementById('agregar');
btn_agregar.addEventListener("click", function( ){
    //crear el div que contiene los 2 sub-divs
    const div_principal = D.create('div');
    //crear el div para el span e input del nombre
    const div_nombre = D.create('div');

    //crear el div para el span e input del campo
    const div_campo = D.create('div');

    //crear los span de nombre y campo
    const span_nombre = D.create('span', { innerHTML: 'Nombre de campo' } );
    const span_campo = D.create('span', { innerHTML: 'Tipo de campo' });

    //crear los inputs de nombre y campo
    const input_nombre = D.create('input', { type: 'text', name: 'nombres[]', autocomplete: 'off', placeholder: 'Nombre del campo' } );

    const input_campo = D.create('input', { type: 'text', name: 'tipos[]', autocomplete: 'off', placeholder: 'Tipo del campo' });

    //crear un botoncito de eliminar este div 
    const borrar = D.create('a', { href: 'javascript:void(0)', innerHTML: 'borrar', onclick: function( ){ D.remove(div_principal); } } );
    
    
    //agregar cada etiqueta a su nodo padre
    D.append(span_nombre, div_nombre);
    D.append(input_nombre, div_nombre);
    D.append([span_campo, input_campo], div_campo);
    D.append([div_nombre, div_campo, borrar], div_principal);
    
    //agregar el div del primer comentario al contenedor con id #container
    D.append(div_principal, D.id('davidlpls') );
    
} );