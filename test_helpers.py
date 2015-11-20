# -*- coding: utf-8 -*-
import mock

class MockObjects:
    TRANSACTION = mock.Mock(
        id = "my_id",
        type = "sale",
        amount = "10.00",
        status = "authorized",
        created_at = "03/01/1994",
        updated_at = "03/01/1994",
        credit_card_details = mock.Mock(
            token = "ijkl",
            bin = "545454",
            last_4 = "5454",
            card_type = "MasterCard",
            expiration_date = "12/2015",
            cardholder_name = "Bill Billson",
            customer_location = "US",
        ),
        customer_details = mock.Mock(
            id = "h6hh3j",
            first_name = "Bill",
            last_name = "Billson",
            email = "bill@example.com",
            company = "Billy Bobby Pins",
            website = "bobby_pins.example.com",
            phone = "1234567890",
            fax = None,
        )
    )
