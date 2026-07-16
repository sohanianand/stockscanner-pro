TEMPLATES = {

    "RSI_OVERSOLD": {

        "condition": "AND",

        "filters": [

            {

                "field": "rsi",

                "operator": "<",

                "value": 30

            }

        ]

    },

    "RSI_OVERBOUGHT": {

        "condition": "AND",

        "filters": [

            {

                "field": "rsi",

                "operator": ">",

                "value": 70

            }

        ]

    },

    "EMA_BULLISH": {

        "condition": "AND",

        "filters": [

            {

                "field": "ema20",

                "operator": ">",

                "value": "ema50"

            }

        ]

    },

    "EMA_BEARISH": {

        "condition": "AND",

        "filters": [

            {

                "field": "ema20",

                "operator": "<",

                "value": "ema50"

            }

        ]

    }

}
