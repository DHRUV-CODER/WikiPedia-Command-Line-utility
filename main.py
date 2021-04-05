import argparse
import sys
import requests as r
import colorama#pip install colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def Get_Results(args):
    url = f'https://wiki-api.dhruvnation1.repl.co/wiki/query={args.s}'
    data = r.get(url).json()
    return f"\n {Fore.GREEN}{data['Result']}\n"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=Fore.CYAN+'\n\nCommand Line Utility For Wikipedia Api\n\n'+Fore.WHITE,
        epilog=Fore.YELLOW+"\n\nCredits :- Dhruv\n\n"+Fore.WHITE
    )
    parser.add_argument('--s',type=str,default="wikipedia",
                        help="Search For Api")

    
    args = parser.parse_args()
    sys.stdout.write(str(Get_Results(args)))
    
    
