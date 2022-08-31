#!/usr/bin/env python3
"""
Author : Lawrence Aneshimokha 
Date   : 5/August/2022
Purpose: Get command-line arguments
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article", 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('word', metavar='word', help='A word')
    
    return parser.parse_args()
    

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    word = args.word
    
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")
   


# --------------------------------------------------
if __name__ == '__main__':
    main()
