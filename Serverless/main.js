module.exports = async function (context, req) {
    const cpf = req.query.cpf || (req.body && req.body.cpf);

    if (!cpf) {
        context.res = {
            status: 400,
            body: "Entre com o CPF: "
        };
        return;
    }

    const isValid = validarCPF(cpf);

    context.res = {
        body: {
            cpf,
            valido: isValid
        }
    };
};

function validarCPF(cpf) {
    cpf = cpf.replace(/[^\d]+/g, ""); 

    if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false;

    for (let t = 9; t < 11; t++) {
        let d = 0;
        for (let i = 0; i < t; i++) {
            d += parseInt(cpf[i]) * (t + 1 - i);
        }
        d = (d * 10) % 11 % 10;
        if (parseInt(cpf[t]) !== d) return false;
    }

    return true;
}