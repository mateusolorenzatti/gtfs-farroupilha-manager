
var CLASSE_HIDE = "d-none";
var CLASSE_BTN = "btn-success text-white";

$(function () {
    $('#btn-preview-mapa').click(modoPreviewMapa);
    $('#btn-dados-trip').click(modoDadosTrip);
    $('#btn-paradas-horarios').click(modoParadasHorarios);
});

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