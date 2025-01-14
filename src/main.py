import sys
import os
import json
from utils.helpers import parse_args, fetch_exchange_rates
from dotenv import load_dotenv


def main():
    load_dotenv()
    args = parse_args(sys.argv[1:])
    result_file = os.getenv('RESULT_FILE')
    debug = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

    # Zpracování argumentů a spuštění logiky aplikace
    print(f"Zpracovávám argumenty: {args}")

    # Stáhnout kurzovní lístek ČNB
    exchange_rates = fetch_exchange_rates(args['currencies'], args['start_date'], args['end_date'])

    # Výstup
    if result_file:
        with open(result_file, 'w') as f:
            if debug:
                json.dump(exchange_rates, f, indent=4)
            else:
                json.dump(exchange_rates, f)
    else:
        if debug:
            print(json.dumps(exchange_rates, indent=4))
        else:
            print(json.dumps(exchange_rates))


if __name__ == "__main__":
    main()
