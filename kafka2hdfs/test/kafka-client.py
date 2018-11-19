import requests
import datetime
import time


template = {
	"id": "01-123125",
	"type": "order",
	"scope": "acom",
	"event_type": "UPDATE",
	"event_time": "2018-06-12T14:23:09.310Z",
	"action_type": "ENTITY",
	"payload": {
		"id": "01-123125",
		"type": "order",
		"event_time": "2018-06-12T14:23:09.292Z",
		"acom": {
			"order:general": {
				"idOrder": "03-483250173",
				"typeSalesChannel": "tp",
				"idSalesChannel": "SUBA - TELEVENDAS",
				"idBrand": "03",
				"idSalesAssistant": "50272652",
				"location": "003001",
				"nameSalesChannel": "nmc",
				"nameBrand": "SUBMARINO",
				"nameSalesAssistant": "nsa",
				"datePurchase": "2016-02-10T19:40:39Z",
				"valueTotal": 23933.35,
				"valueDiscount": "0",
				"valueDiscountCond": 1399.58,
				"valueDiscountUncond": 2659.3,
				"valueTotalFreight": 19.99,
				"valueChargedFreight": 0,
				"valueDiscountFreight": "value_dec",
				"valueCommercialFreight": "value_dec",
				"valueExpenses": 0,
				"timeDeliveryDays": 5,
				"statusOrder": "PRC",
				"nameStatusOrder": "Em processamento",
				"dateStatusOrder": "2016-02-26T14:07:49Z",
				"qtDeliveriesTotal": 3,
				"dateCreated": "2016-02-10T19:40:39Z",
				"dateDelivered": "2016-02-10T19:40:39Z",
				"dateCanceled": "2016-02-10T19:40:39Z",
				"addressInfoBilling": {
					"idAddress": "03-1999708769-1",
					"idCustomer": "03-4921856337-1",
					"streetName": "av. teste",
					"number": "13",
					"additionalInfo": "teste",
					"city": "Sao Paulo",
					"state": "SP",
					"country": "Brasil",
					"postalCode": "00000-000",
					"reference": "perto de teste",
					"latitude": 1.1,
					"longitude": 1.2
				},
				"addressInfoDelivery": {
					"idAddress": "03-1999708769-1",
					"idCustomer": "03-4921856337-1",
					"streetName": "av. teste",
					"number": "13",
					"additionalInfo": "teste",
					"city": "Sao Paulo",
					"state": "SP",
					"country": "Brasil",
					"postalCode": "00000-000",
					"reference": "perto de teste",
					"latitude": 1.1,
					"longitude": 1.2
				},
				"customerInfo": {
					"idCustomer": "03-4921856337-1",
					"idBrand": "03",
					"personType": "F",
					"name": "Joao da Silva",
					"nameFirst": "Joao",
					"nameLast": "da Silva",
					"nickname": "JS",
					"gender": "M",
					"dateBirth": "2000-02-10T00:00:00Z",
					"email": "joao.silva@teste.com"
				}
			}
		}
	}
}
  
def main():
    count = 0
    time_sleep = 3
    while True:
        time.sleep(time_sleep)
        response = requests.post(
            'https://v2datalakeb2wio-a.akamaihd.net/send-data/juvenal-order/juvenal',
            json = {'count': count, 'test': 'test1'}
        )
        count += 1
        print response.status_code


if __name__ == '__main__':
	print 'ok'