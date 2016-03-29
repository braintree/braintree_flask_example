# -*- coding: utf-8 -*-
import mock
import copy

class MockObjects:
    TRANSACTION_SUCCESSFUL = mock.Mock(
        id = 'my_id',
        type = 'sale',
        amount = '10.00',
        status = 'authorized',
        created_at = '03/01/1994',
        updated_at = '03/01/1994',
        credit_card_details = mock.Mock(
            token = 'ijkl',
            bin = '545454',
            last_4 = '5454',
            card_type = 'MasterCard',
            expiration_date = '12/2015',
            cardholder_name = 'Bill Billson',
            customer_location = 'US',
        ),
        customer_details = mock.Mock(
            id = 'h6hh3j',
            first_name = 'Bill',
            last_name = 'Billson',
            email = 'bill@example.com',
            company = 'Billy Bobby Pins',
            website = 'bobby_pins.example.com',
            phone = '1234567890',
            fax = None,
        )
    )

    TRANSACTION_FAILURE = copy.copy(TRANSACTION_SUCCESSFUL)
    TRANSACTION_FAILURE.status = "processor_declined"

    TRANSACTION_NO_CUSTOMER = copy.copy(TRANSACTION_SUCCESSFUL)
    TRANSACTION_NO_CUSTOMER.customer_details = mock.Mock(
            id = None,
            first_name = None,
            last_name = None,
            email = None,
            company = None,
            website = None,
            phone = None,
            fax = None,
    )

MockObjects.TRANSACTION_SALE_SUCCESSFUL = mock.Mock(
    transaction = MockObjects.TRANSACTION_SUCCESSFUL
)

MockObjects.TRANSACTION_SALE_UNSUCCESSFUL = mock.Mock(
    is_success = False,
    errors = mock.Mock(
        deep_errors = [
            mock.Mock(message='Error: 12345: Transaction was unsuccessful'),
            mock.Mock(message='Error: 67890: Transaction was really unsuccessful'),
        ]
    ),
    transaction = None
)

MockObjects.TRANSACTION_SALE_UNSUCCESSFUL_PROCESSOR = mock.Mock(
    is_success = True,
    transaction = MockObjects.TRANSACTION_FAILURE
)
