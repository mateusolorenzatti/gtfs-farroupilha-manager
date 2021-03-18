
$(function() {
       
    // Crair uma assossiação entre os horários das paradas, para criar uma relação de retardo entre todas
    var horario_inicio_fixo = $('#horario-inicio').val();

    var DEBUG_MODE = false;

    $('#horario-inicio').blur(() => {
        horario_inicio = new Date('2021-01-01 ' + $('#horario-inicio').val());

        // Conferir se a data é inválida (horario_inicio_fixo)
        if (isNaN(horario_inicio.getTime())) {  
            $('#horario-inicio').val(horario_inicio_fixo);

            halfmoon.initStickyAlert({
                content: "Voltei para o horário que tínhamos no inicio da sessão.",
                title: "Horário Inválido! ",
                alertType: "alert-danger",
            });

            return;
        }

        td_deltas_tabela = $('.diferenca-tabela');
        td_horarios_tabela = $('.horario-tabela');

        horarios = [];

        for(let i = 0; i < td_deltas_tabela.length; i++){
            if(DEBUG_MODE) console.log(" --------------------------------------------------------- ");

            horario_inicio = new Date('2021-01-01 ' + $('#horario-inicio').val());
            if(DEBUG_MODE) console.log(" Horário de Inicio: " + horario_inicio);

            delta = new Date('2021-01-01 0' + td_deltas_tabela[i].innerText.substring(2));
            if(DEBUG_MODE) console.log(" Diferença a ser somada: " + delta);

            horario_inicio.setSeconds(horario_inicio.getSeconds() + delta.getSeconds());
            horario_inicio.setMinutes(horario_inicio.getMinutes() + delta.getMinutes());
            horario_inicio.setHours(horario_inicio.getHours() + delta.getHours());

            horario = new Date( horario_inicio );
            if(DEBUG_MODE) console.log(" Novo horário calculado: " + horario);

            // Altera o horário calculado no respectivo marcador
            td_horarios_tabela[i].innerText = horario.toTimeString().substring(0, 8);
        }
    });
});
