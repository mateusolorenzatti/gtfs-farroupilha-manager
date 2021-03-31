
var CLASSE_HIDE = "d-none";
var CLASSE_BTN = "btn-success text-white";
var horario_inicio_fixo = $('#horario-inicio').val();

var SUCCESS_IMG = "/static/img/sucesso.svg";

var DEBUG_MODE = false;

$(function () {
    // Crair uma assossiação entre os horários das paradas, para criar uma relação de retardo entre todas

    $('#horario-inicio').blur(atualizaHorarios);

    $('#btn-preview-mapa').click(modoPreviewMapa);
    $('#btn-dados-trip').click(modoDadosTrip);
    $('#btn-paradas-horarios').click(modoParadasHorarios);

    $('#btn-salvar-tudo').click(salvarTudo);
});

function atualizaHorarios() {
    horario_inicio = new Date('2021-01-01 ' + $('#horario-inicio').val());

    // Conferir se a data é inválida (horario_inicio_fixo)
    if (isNaN(horario_inicio.getTime())) {
        $('#horario-inicio').val(horario_inicio_fixo);

        alertError("Horário Inválido! ", "Voltei para o horário que tínhamos no inicio da sessão.");

        return;
    }

    td_deltas_tabela = $('.diferenca-tabela');
    td_horarios_tabela = $('.horario-tabela');

    horarios = [];

    for (let i = 0; i < td_deltas_tabela.length; i++) {
        if (DEBUG_MODE) console.log(" --------------------------------------------------------- ");

        horario_inicio = new Date('2021-01-01 ' + $('#horario-inicio').val());
        if (DEBUG_MODE) console.log(" Horário de Inicio: " + horario_inicio);

        delta = new Date('2021-01-01 0' + td_deltas_tabela[i].innerText.substring(2));
        if (DEBUG_MODE) console.log(" Diferença a ser somada: " + delta);

        horario_inicio.setSeconds(horario_inicio.getSeconds() + delta.getSeconds());
        horario_inicio.setMinutes(horario_inicio.getMinutes() + delta.getMinutes());
        horario_inicio.setHours(horario_inicio.getHours() + delta.getHours());

        horario = new Date(horario_inicio);
        if (DEBUG_MODE) console.log(" Novo horário calculado: " + horario);

        // Altera o horário calculado no respectivo marcador
        td_horarios_tabela[i].innerText = horario.toTimeString().substring(0, 8);
    }

}

function concluiStop(parada_seq, parada_obj, parada_desc) {

    $('#data-stop-' + parada_seq).html(JSON.stringify(parada_obj));

    $('#collapse-panel-' + parada_seq).removeAttr("open");
    $('#status-parada-' + parada_seq).removeClass("badge-secondary").addClass("badge-success text-white").html("Pronto");
    $('#parada-nome-' + parada_seq).html(parada_desc);

    alertSuccess('Tudo certo!', "A parada " + parada_seq + " foi configurada com sucesso!");
    let pronto = true;

    $(".status-parada").each(function (index, element) {
        if ($(this).text().includes("Pendente")) pronto = false;
    });

    if (!pronto) return;

    $('#div-salvar-tudo').removeClass("d-none");
}

function modoPreviewMapa() {
    $('#preview-mapa').removeClass(CLASSE_HIDE);
    $('#dados-trip').addClass(CLASSE_HIDE);
    $('#paradas-horarios').addClass(CLASSE_HIDE);

    $('#btn-preview-mapa').addClass(CLASSE_BTN);
    $('#btn-dados-trip').removeClass(CLASSE_BTN);
    $('#btn-paradas-horarios').removeClass(CLASSE_BTN);
}

function modoDadosTrip() {
    $('#preview-mapa').addClass(CLASSE_HIDE);
    $('#dados-trip').removeClass(CLASSE_HIDE);
    $('#paradas-horarios').addClass(CLASSE_HIDE);

    $('#btn-preview-mapa').removeClass(CLASSE_BTN);
    $('#btn-dados-trip').addClass(CLASSE_BTN);
    $('#btn-paradas-horarios').removeClass(CLASSE_BTN);
}

function modoParadasHorarios() {
    $('#preview-mapa').addClass(CLASSE_HIDE);
    $('#dados-trip').addClass(CLASSE_HIDE);
    $('#paradas-horarios').removeClass(CLASSE_HIDE);

    $('#btn-preview-mapa').removeClass(CLASSE_BTN);
    $('#btn-dados-trip').removeClass(CLASSE_BTN);
    $('#btn-paradas-horarios').addClass(CLASSE_BTN);
}

function salvarTudo() {
    $('#tela-scratch').addClass(CLASSE_HIDE);
    $('#tela-finaliza').removeClass(CLASSE_HIDE);

    let shapes = $('#data-shapes').text();

    // console.log('Enviando Shapes');

    enviarRequestShapes(shapes, (data) => {
        setTimeout(() => {
            $('#imagem-progresso-criacao-shapes').attr("src", SUCCESS_IMG);
            $('#progresso-criacao-trip').removeClass(CLASSE_HIDE);

            // Coletar dados do form da Trip
            trip = {
                route: $('#id_route').val(),
                trip_id: $('#id_trip_id').val(),
                service_id: $('#id_service_id').val(),
                trip_short_name: $('#id_trip_short_name').val(),
                trip_headsign: $('#id_trip_headsign').val(),
                shape_id: $('#id_shape_id').val()
            };

            enviarRequestTrip(trip, (data) => {
                setTimeout(() => {
                    $('#imagem-progresso-criacao-trip').attr("src", SUCCESS_IMG);
                    $('#progresso-criacao-stop-times').removeClass(CLASSE_HIDE);

                    stops = "[";
                    $(".data-stop").each(function (index, element) {
                        stops = stops + ($(this).text().substring(0, $(this).text().length - 1)) + ', "trip_id": "' + $('#id_trip_id').val() + '"} ,';
                    });
                    stops = stops.substring(0, stops.length - 1)
                    stops += "]";

                    enviarRequestStopTimes(stops, (data) => {
                        setTimeout(() => {
                            $('#imagem-progresso-criacao-stop-times').attr("src", SUCCESS_IMG);
                            $('#botoes-navegacao').removeClass(CLASSE_HIDE);
                        }, 2000);
                    });
                    
                }, 2000);
            });
        }, 2000);
    });

}