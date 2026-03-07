<?php
	require_once __DIR__ . 'nip/web/includes/ai_client.php';
	
	header("Content-Type: application/json");
	
	$message = $_POST["message"] ?? "";
	
	if (!$message) {
		echo json_encode([
			"error" => "Mensagem vazia"
		]);
		exit;
	}
	
	$response  = ask_ai($message);
	
	echo json_encode([
		"response" => $response
	]);