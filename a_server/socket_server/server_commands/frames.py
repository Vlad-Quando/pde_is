# 1 – кадр данных обнаружения БПЛА устройством обнаружения и идентификации

DETECTION_DATA_FRAME = {
    "time": 0,                 # (int64) GPS время [наносекунды]
    "packetType": 1,           # (int32) тип команды = 1
    "deviceID": 0,             # (int32) идентификатор устройства

    "deviceType": 0,           # (int32) тип устройства
    "deviceLatitude": 0,       # (float) широта привязки устройства
    "deviceLongitude": 0,      # (float) долгота привязки устройства
    "deviceAltitude": 0,       # (float) высота привязки устройства

    "signalType": 0,           # (int32) тип радиосигнала/принадлежность[усл.ед.]
    "signalFrequency": 0,      # (int64) частота сигнала [Гц]
    "signalAmplitude": 0,      # (int32) амплитуда сигнала [от -150дБм до 20дБм]
    "signalWidth": 0,          # (int32) ширина сигнала [Гц]
    "signalDetectionType": 0,  # (int32) тип обнаружения [усл.ед.]

    "uav": {
        "uavType": '',			    # (string) тип объекта
        "serialNumber": '',		    # (string) серийный номер
        "startUavLatitude": 0,		# (float) широта точки запуска БПЛА
        "startUavLongitude": 0,	    # (float) долгота точки запуска БПЛА
        "uavLatitude": 0,		    # (float) широта текущего положения БПЛА
        "uavLongitude": 0,		    # (float) долгота текущего положения БПЛА
        "uavAltitude": 0,		    # (float) высота текущего положения БПЛА
        "operatorLatitude": 0,		# (float) широта положения оператора БПЛА
        "operatorLongitude": 0		# (float) долгота положения оператора БПЛА
	}
}

# Тип радиосигнала"signalType":
# 1 – Идентифицирован протокол DJI OcuSync 1.0
# 2 – Идентифицирован протокол DJI OcuSync 2.0
# 3 – Идентифицирован протокол DJI OcuSync 3.0
# 4 – Идентифицирован протокол DJI OcuSync 3.0+
# 5 – Идентифицирован протокол DJI OcuSync 4.0
# 6 – Идентифицирован протокол DJI LightBridge 1.0
# 7 – Идентифицирован протокол DJI LightBridge 2.0
# 8 – Идентифицирован протокол Autel SkyLink 2.0
# 9 – Идентифицирован протокол Autel SkyLink 3.0
# 10 – Идентифицирован протокол Analog Video
# 51 – Идентифицирован протокол DJI DroneID
# 52 – Идентифицирован протокол RemoteID

# Тип обнаружения"signalDetectionType":
# 1 – Корреляционная функция.
# 2 – Нейросеть.

# -------------------------------------------------------------------------------------

# 2 – команда установки параметров устройства обнаружения и идентификации

PARAM_SETTING_COMMAND = {
	"time": 0,			                            # (int64) GPS время [наносекунды]
	"packetType": 2,		                        # (int32) тип команды = 2
	"deviceID": 0,			                        # (int32) идентификатор устройства

	"supressMode": 0,		                        # (int32) режим работы устройства обнаружения и идентификации [усл.ед.]

	"params" : [	                                # это массив объектов
      		{
			"centerFrequency": 0,		            # (int64) центральная частота сигнала [Гц]
			"receiveSensitivity": 0,	            # (int32) коэффициент усиления[дБ] (0 – АРУ)
			"detectionBandwidth": 0,	            # (int64) ширина полосы обнаружения [Гц]
		
			"idents" : [	                        # это массив объектов
      		   		{ 
					"signalType": '',		        # (string) тип идентификации
					"signalDetectionType": '',	    # (string) тип обнаружения
	 	   		}
			]
		}
	],
	"additional": ''			                    # (string) дополнительные сведения
}

# Режим работы устройства обнаружения и идентификации "supressMode":
# 1 – Все режимы.
# 2 – Отмена всех режимов.
# 3 – Обнаружение по радиосигналу.
# 4 – Отмена обнаружения по радиосигналу.
# 5 – Обнаружение по ID (wifi).
# 6 – Отмена обнаружения по ID (wifi).

# -------------------------------------------------------------------------------------

# 3 – команда запроса параметров устройства обнаружения и идентификации

QUERY_PARAMS_COMMAND = {
	"time": 0,			    # (int64) GPS время [наносекунды]
	"packetType": 3,		# (int32) тип команды =3
	"deviceID": 0			# (int32) идентификатор устройства
}

# -------------------------------------------------------------------------------------

# 4 – данные параметров устройства обнаружения и идентификации

PARAMS_DATA_COMMAND = {
	"time": 0,			                    # (int64) GPS время [наносекунды]
	"packetType": 4,		                # (int32) тип команды =4
	"deviceID": 0,			                # (int32) идентификатор устройства

	"deviceType": 0,		                # (int32) тип устройства 
	"deviceStatus": 0,		                # (int32) статус устройства 
	"supressMode": 0,		                # (int32) режим работы устройства обнаружения и идентификации [усл.ед.]
	"params": [	                            # это массив объектов
        {
            "centerFrequency": 0,		    # (int64) центральная частота сигнала [Гц]
            "receiveSensitivity": 0,	    # (int32) коэффициент усиления[дБ] (0 – АРУ)
            "detectionBandwidth": 0,	    # (int64) ширина полосы обнаружения [Гц]
        
            "idents": [	                    # это массив объектов
                { 
                "signalType": '',		    # (string) тип идентификации
                "signalDetectionType": '',	# (string) тип обнаружения
            }
        ]
		}
	],
	"additional": ''			            # (string) дополнительные сведения
}

# Статус устройства"deviceStatus":
# 1 – В работе.
# 2 – В режиме ожидания.
# 3 – Аварийная остановка.

# -------------------------------------------------------------------------------------

# 18 – подтверждение приема данных устройством

DATA_RECEPTION_COMMITION = {
	"time": 0,		        # (int64) GPS время [наносекунды]
	"packetType": 18,	    # (int32) тип команды=18
	"deviceID": 0,		    # (int32) идентификатор устройства
	
	"deviceType": 0,	    # (int32) тип устройства
	"confirmCmdTime": 0,	# (int64) время подтверждаемой команды [нсек]
	"result": 0		        # (int32) результат приема команды
}

# Результат приема команды "result":
# 1 – Команда принята без ошибок.
# 2 – Команда не применима к этому устройству.
# 3 – Команда адресована другому устройству.

# -------------------------------------------------------------------------------------

# 19 – маркер активности устройства

DEVICE_ACTIVITY_MARKER = {
	"time": 0,		        # (int64) GPS время [наносекунды]
	"packetType": 19,	    # (int32) тип команды=19
	"deviceID": 0,		    # (int32) идентификатор устройства

	"deviceType": 0,	    # (int32) тип устройства
	"deviceLatitude": 0,	# (float) широта привязки устройства
	"deviceLongitude": 0,	# (float) долгота привязки устройства
	"deviceAltitude": 0	    # (float) высота привязки устройства
}

# 20 – данные о возникновении ошибки в работе устройства

{
	"time": 0,			        # (int64) GPS время [наносекунды]
	"packetType": 20,		    # (int32) тип команды = 20
	"deviceID": 0,			    # (int32) идентификатор устройства

	"deviceType": 0,		    # (int32) тип устройства
	"deviceErrorStatus": 0,	    # (int32) критичность ошибки
	"deviceErrorComment": 0,	# (string) комментарий к ошибке
}

# Критичность ошибки "deviceErrorStatus":
# 1 – Не влияет на функционирование устройства.
# 2 – Частичный отказ аппаратных элементов устройства.
# 3 – Полный отказ аппаратных элементов устройства.
# 4 – Устройство не выполняет свои функции
