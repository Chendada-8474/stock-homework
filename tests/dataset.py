class ResponseForTest:
    @property
    def headers(self):
        return {
            "server": "nginx",
            "date": "Wed, 19 Jul 2023 04:44:39 GMT",
            "content-type": "application/json",
            "last-modified": "Tue, 18 Jul 2023 21:00:42 GMT",
            "transfer-encoding": "chunked",
            "connection": "keep-alive",
            "eTag": 'W/"64b6fd7a-20ccda"',
            "content-disposition": "attachment;filename=STOCK_DAY_AVG_ALL.json",
            "content-encoding": "gzip",
        }

    def json(self):
        return [
            {
                "Code": "0050",
                "Name": "元大台灣50",
                "ClosingPrice": "132.00",
                "MonthlyAveragePrice": "129.94",
            },
            {
                "Code": "0051",
                "Name": "元大中型100",
                "ClosingPrice": "71.95",
                "MonthlyAveragePrice": "69.15",
            },
            {
                "Code": "0052",
                "Name": "富邦科技",
                "ClosingPrice": "121.30",
                "MonthlyAveragePrice": "117.78",
            },
            {
                "Code": "0053",
                "Name": "元大電子",
                "ClosingPrice": "70.20",
                "MonthlyAveragePrice": "68.20",
            },
            {
                "Code": "0055",
                "Name": "元大MSCI金融",
                "ClosingPrice": "23.80",
                "MonthlyAveragePrice": "23.19",
            },
            {
                "Code": "0056",
                "Name": "元大高股息",
                "ClosingPrice": "",
                "MonthlyAveragePrice": "34.08",
            },
        ]


result_map_for_test = {
    "0050": {
        "Code": "0050",
        "Name": "元大台灣50",
        "ClosingPrice": "132.00",
        "MonthlyAveragePrice": "129.94",
    },
    "0051": {
        "Code": "0051",
        "Name": "元大中型100",
        "ClosingPrice": "71.95",
        "MonthlyAveragePrice": "69.15",
    },
    "0052": {
        "Code": "0052",
        "Name": "富邦科技",
        "ClosingPrice": "121.30",
        "MonthlyAveragePrice": "117.78",
    },
    "0053": {
        "Code": "0053",
        "Name": "元大電子",
        "ClosingPrice": "70.20",
        "MonthlyAveragePrice": "68.20",
    },
    "0055": {
        "Code": "0055",
        "Name": "元大MSCI金融",
        "ClosingPrice": "23.80",
        "MonthlyAveragePrice": "23.19",
    },
    "0056": {
        "Code": "0056",
        "Name": "元大高股息",
        "ClosingPrice": "",
        "MonthlyAveragePrice": "34.08",
    },
}


targeted_answer = [
    {
        "Code": "0050",
        "Name": "元大台灣50",
        "ClosingPrice": 132.00,
        "ClosingDate": "2023-07-18",
    },
    {
        "Code": "0051",
        "Name": "元大中型100",
        "ClosingPrice": 71.95,
        "ClosingDate": "2023-07-18",
    },
    {
        "Code": "0052",
        "Name": "富邦科技",
        "ClosingPrice": 121.30,
        "ClosingDate": "2023-07-18",
    },
]

untarget_answer = [
    {
        "Code": "0050",
        "Name": "元大台灣50",
        "ClosingPrice": 132.00,
        "ClosingDate": "2023-07-18",
    },
    {
        "Code": "0051",
        "Name": "元大中型100",
        "ClosingPrice": 71.95,
        "ClosingDate": "2023-07-18",
    },
    {
        "Code": "0052",
        "Name": "富邦科技",
        "ClosingPrice": 121.30,
        "ClosingDate": "2023-07-18",
    },
    {
        "Code": "0053",
        "Name": "元大電子",
        "ClosingPrice": 70.20,
        "ClosingDate": "2023-07-18",
    },
    {
        "Code": "0055",
        "Name": "元大MSCI金融",
        "ClosingPrice": 23.80,
        "ClosingDate": "2023-07-18",
    },
    {
        "Code": "0056",
        "Name": "元大高股息",
        "ClosingPrice": None,
        "ClosingDate": "2023-07-18",
    },
]
