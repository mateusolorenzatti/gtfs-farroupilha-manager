
function alertSuccess(titulo, conteudo){
    halfmoon.initStickyAlert({
        title: titulo,
        content: conteudo,
        alertType: "alert-success",
        fillType: "filled-lm"
      });
}

function alertError(titulo, conteudo){
    halfmoon.initStickyAlert({
        title: titulo,
        content: conteudo,
        alertType: "alert-danger",
        fillType: "filled-lm"
      });
}

function alertWarning(titulo, conteudo){
    halfmoon.initStickyAlert({
        title: titulo,
        content: conteudo,
        alertType: "alert-secondary",
        fillType: "filled-lm"
      });
}