<?php

namespace App\Controllers;

use App\Models\User;

class Home extends BaseController
{
    public function index(): string
    {
        // $user = new User();

        // $usuario = $user->findAll();
        // var_dump($usuario);
        // die();
        $db = db_connect();
        $sql = "select * from users where id > ?";
        $result = $db->query($sql, [10]);
        var_dump($result->getResultObject());
        die();
        return view('welcome_message');
    }
}
