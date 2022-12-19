download = {
	"info": {
		"_postman_id": "5255c381-14f7-4d0b-a804-7bc628058c5d",
		"name": "API - Python com flask",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "Home API",
			"request": {
				"auth": {
					"type": "noauth"
				},
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://192.168.0.33:5000/",
					"protocol": "http",
					"host": [
						"192",
						"168",
						"0",
						"33"
					],
					"port": "5000",
					"path": [
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Produtos cadastrados",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://192.168.0.33:5000/stocks/",
					"protocol": "http",
					"host": [
						"192",
						"168",
						"0",
						"33"
					],
					"port": "5000",
					"path": [
						"stocks",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Procurar um produto",
			"protocolProfileBehavior": {
				"disableBodyPruning": True
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": ""
				},
				"url": {
					"raw": "http://192.168.0.33:5000/stock/ITIU4/",
					"protocol": "http",
					"host": [
						"192",
						"168",
						"0",
						"33"
					],
					"port": "5000",
					"path": [
						"stock",
						"ITIU4",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Novo produto",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"Name\": \"ITI BANCO DIGITAL\",\r\n    \"Symbol\": \"ITIU4\",\r\n    \"Price\": 6\r\n}"
				},
				"url": {
					"raw": "http://192.168.0.33:5000/new/stock/",
					"protocol": "http",
					"host": [
						"192",
						"168",
						"0",
						"33"
					],
					"port": "5000",
					"path": [
						"new",
						"stock",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Update product price",
			"request": {
				"method": "PATCH",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"Price\": 2\r\n}"
				},
				"url": {
					"raw": "http://192.168.0.33:5000/stock/ITIU4/change/price/",
					"protocol": "http",
					"host": [
						"192",
						"168",
						"0",
						"33"
					],
					"port": "5000",
					"path": [
						"stock",
						"ITIU4",
						"change",
						"price",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Deletar produto",
			"request": {
				"method": "DELETE",
				"header": [],
				"url": {
					"raw": "http://192.168.0.33:5000/stock/delete/ITIU4/",
					"protocol": "http",
					"host": [
						"192",
						"168",
						"0",
						"33"
					],
					"port": "5000",
					"path": [
						"stock",
						"delete",
						"ITIU4",
						""
					]
				}
			},
			"response": []
		}
	]
}