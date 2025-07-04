// async: espera a resposta da função para executar o restante do codigo
async function connect() {
    // verifica se a conexao ja foi feita
    if (global.connection && global.connection.state != "disconnected"){
        return global.connection;
    }

    const mysql = require("mysql2/promise");
    const connection = await mysql.createConnection(
        {
            host: "54.91.193.137", user: "libertas",
            password:"123456", database: "libertas5per"
        }
    );
    global.connection = connection;
    return connection;
}

exports.post = async(req, res, next) =>{
    const con = await connect();
    const sql = "INSERT INTO usuario (nome, telefone, email, senha) VALUES (?,?,?,?)";
    const values = [req.body.nome, req.body.telefone, req.body.email, req.body.senha];
    await con.query(sql, values);
    res.status(201).send("INSERIDO COM SUCESSO");
}
exports.put = async(req, res, next) =>{
    let id = req.params.id;
    const con = await connect();
    const sql = "UPDATE usuario SET nome = ?, telefone = ?, email = ?, senha = ? WHERE idusuario = ?";
    const values = [req.body.nome, req.body.telefone, req.body.email, req.body.senha, id];
    await con.query(sql, values);
    res.status(201).send("ALTERADO COM SUCESSO ID:" + id);
}
exports.delete = async(req, res, next) =>{
    let id = req.params.id;
    const con = await connect();
    const sql = "DELETE FROM usuario WHERE idusuario = ?";
    const values = [id];
    await con.query(sql, values);
    res.status(200).send("EXCLUIDO COM SUCESSO ID:" + id);
}
exports.get = async(req, res, next) =>{
    const con = await connect();
    const [rows] = await con.query("SELECT * FROM usuario");
    res.status(200).send(rows);
}
exports.getById = async(req, res, next) =>{
    let id = req.params.id;
    const con = await connect();

    try {
        const [rows] = await con.query("SELECT * FROM usuario WHERE idusuario = ?", [id]);
        if (rows.length != 0) {
            res.status(200).send(rows[0]);
        } else { 
            res.status(404).send("NOT FOUND");
        }
        
    } catch (error) {
        res.status(500).send("ERRO");
    }
}