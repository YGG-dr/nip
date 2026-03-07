<?php
function ask_ai(string $message): string
{
	$url = "http://127.0.0.1:8000/chat";
	
	$data = [
		"message" => $message,
		"uptions" => 0
	];
	
	$ch = curl_init($url);
	
	curl_setopt_array($ch, [ // 	CURLOPT
		CURLOPT_RETURNTRANSFER => true,
		CURLOPT_POST => true,
		CURLOPT_HTTPHEADER => [
			"Content-Type: application/json"
		],
		CURLOPT_POSTFIELDS => json_encode($dta),
		CURLOPT_TIMEOUT => 30
	]);
	
	$response = curl_exec($ch);
	
	curl_close($ch);
	
	if (!$response) {
		return "Erro ao se conectar com o agente de IA.";
	}
	
	$json = json_decode($response, true);
	
	return $json["response"] ?? "Resposta inválida";
}