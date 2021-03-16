
$(function() {
       
    // Crair uma assossiação entre os horários das paradas, para criar uma relação de retardo entre todas
    var horario_inicio_fixo = $('#horario-inicio').val();

    $('#horario-inicio').blur(() => {
        horario_inicio = new Date('2021-01-01 ' + $('#horario-inicio').val());

        // Conferir se a data é inválida (horario_inicio_fixo)
        
        td_horarios_tabela = $('.horario-tabela');

        horarios = [];

        for(let i = 0; i < td_horarios_tabela.length; i++){
            // horarios.push(new Date('2021-01-01 ' + td_horarios_tabela[i].innerText))
            horario = new Date('2021-01-01 ' + td_horarios_tabela[i].innerText);

            dif = (horario.getTime() - horario_inicio.getTime()) / 1000;

            console.log(dif);
        }

        console.log(horarios);
    });
});
